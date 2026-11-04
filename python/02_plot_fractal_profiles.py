"""
02_plot_fractal_profiles.py

Plots the fractal dimension (D) of the nasal turbinates along the nasal cavity
for the four cat specimens, reproducing Figure 8C (no smoothing) and
Figure 8D (smoothing window = 45% of slices).

Input:  csv/*.csv  (one file per specimen, produced by
        imagej/01_compute_fractal_dimension.ijm)
Output: figures/fig8C_smoothing_0.png
        figures/fig8D_smoothing_45.png

Usage (from the repository root or from the python folder):
    python python/02_plot_fractal_profiles.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Paths (relative to the repository root) 

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "csv"
FIG_DIR = REPO_ROOT / "figures"

# Specimens 
# Plotting order and colours as in Figure 8 (last item is drawn on top).

SPECIMENS = [
    {"label": "RM 2728.1 (mummified cat)",  "file": "RM2728-1_mummy.csv",        "color": "#ff7f2a80"},
    {"label": "RM 2018.14.01 (domestic)",   "file": "RM2018-14-01_domestic.csv", "color": "#94a3ff80"},
    {"label": "RM 7303 (African cat)",      "file": "RM7303_african.csv",        "color": "#d4aa0080"},
    {"label": "RM 2018.07.01 (domestic)",   "file": "RM2018-07-01_domestic.csv", "color": "#00af9980"},
]

# Figures to produce 
# Smoothing = width of the centred rolling-mean window, as a fraction of each
# specimen's total number of slices. Scaling the window to the slice count
# gives the same relative smoothing for skulls of different lengths.
# 0.0 means no smoothing (window of 1 slice).

FIGURES = [
    {"smoothing": 0.0,  "output": "fig8C_smoothing_0.png"},
    {"smoothing": 0.45, "output": "fig8D_smoothing_45.png"},
]


def smooth(d, fraction):
    """
    Centred rolling mean of a 1-D series.

    Args:
        d:        fractal dimension values, ordered by slice
        fraction: window width as a fraction of len(d) (e.g. 0.45)
    Returns:
        pandas Series of the same length as d.

    Note: min_periods=1 keeps the ends of the curve. Near both ends the window
    is only partly filled, so the first and last points are averaged over
    fewer slices than points in the middle.
    """
    window = max(1, int(len(d) * fraction))
    return pd.Series(d).rolling(window=window, center=True, min_periods=1).mean()


def plot_profiles(smoothing, output_path):
    """Plot D along the turbinates for all specimens and save to output_path."""
    fig, ax = plt.subplots(figsize=(20, 8))

    for spec in SPECIMENS:
        df = pd.read_csv(DATA_DIR / spec["file"])
        d = df["fractal_dimension"].values

        # Normalise slice position to 0-100% so that specimens with different
        # nasal cavity lengths can be compared.
        x = np.linspace(0, 100, len(d))

        ax.plot(x, smooth(d, smoothing), color=spec["color"],
                linewidth=2.5, label=spec["label"])

    ax.set_xlabel("Position along nasal turbinates (%)", fontsize=30, labelpad=15)
    ax.set_ylabel("Fractal dimension (D)", fontsize=30, labelpad=15)
    ax.tick_params(axis="both", labelsize=20)
    ax.grid(True, linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)
    print(f"Saved {output_path}")


if __name__ == "__main__":
    FIG_DIR.mkdir(exist_ok=True)
    for f in FIGURES:
        plot_profiles(f["smoothing"], FIG_DIR / f["output"])
