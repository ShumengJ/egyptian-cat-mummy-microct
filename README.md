<div align="center">

# The life and afterlife of an ancient Egyptian cat reconstructed by µCT

**Alexandre V. Demers-Potvin<sup>1</sup>, Shumeng Jia<sup>1</sup>, Maris Schneider<sup>2,3</sup>, Antonios Giakoumis<sup>4</sup>, Seyedmahdi Hosseinitabatabaei<sup>1</sup>, Teagan Chow<sup>5</sup>, Isa Shafique<sup>4</sup>, Mazen Asali<sup>6</sup>, Vladimir Brailovski<sup>7</sup>, Anthony Howell<sup>8</sup>, Annie Lussier<sup>9</sup>, Nicholas Piche<sup>7</sup>, Benjamin Provencher<sup>10</sup>, Andrew J. Nelson<sup>2</sup>, Natalie Reznikov<sup>1,</sup><sup>11</sup>**

<sup>\*</sup> Corresponding author: Natalie Reznikov  
Repository contact: Shumeng Jia

*Companion repository for a manuscript prepared for the* **Journal of the Royal Society Interface**

<details>
<summary><b>Affiliations</b></summary>
<br>
<sup>1</sup> Department of Bioengineering, McGill University, Montréal, Québec, Canada<br>
<sup>2</sup> Department of Anthropology, Western University, London, Ontario, Canada<br>
<sup>3</sup> Collaborative Specialization in Musculoskeletal Health Research, Bone and Joint Institute, Western University, London, Ontario, Canada<br>
<sup>4</sup> Department of Electrical and Computer Engineering, McGill University, Montréal, Québec, Canada<br>
<sup>5</sup> Peter Guo-Hua Fu School of Architecture, McGill University, Montréal, Québec, Canada<br>
<sup>6</sup> School of Computer Science, McGill University, Montréal, Québec, Canada<br>
<sup>7</sup> Département de génie mécanique, École de technologie supérieure, Montréal, Québec, Canada<br>
<sup>8</sup> Natural History, Redpath Museum, McGill University, Montréal, Québec, Canada<br>
<sup>9</sup> World Cultures, Redpath Museum, McGill University, Montréal, Québec, Canada<br>
<sup>10</sup> Comet Technologies Canada Inc., Montréal, Québec, Canada<br>
<sup>11</sup> Department of Anatomy and Cell Biology, McGill University, Montréal, Québec, Canada
</details>

</div>

<!--
HERO FIGURE: enable this block after figures/overview.png has been added.
<p align="center">
  <img src="figures/overview.png" alt="Overview of the ancient Egyptian cat mummy µCT study" width="850">
  <br>
  <sub><i>Figure 1. [Replace this text with the final caption.]</i></sub>
</p>
-->

## Overview

This repository accompanies our µCT investigation of an ancient Egyptian cat mummy. It contains the ImageJ macro, tabular outputs, and Python script used to quantify and visualize variation in nasal-turbinate fractal dimension, together with the figures they produce (Figure 8C–D) and the [supplementary text](supplementary-text.md).

The repository supports the computational slice-analysis portion of the study. Volumetric image data and trained Dragonfly model folders are distributed separately because of their size.

> **Related research**  
> Discover the wider story of our animal-mummy research through the École de technologie supérieure articles in [English](https://www.etsmtl.ca/en/news/devoiler-les-secrets-des-momies-animales-de-legypte-ancienne) and [French](https://www.etsmtl.ca/actualites/devoiler-les-secrets-des-momies-animales-de-legypte-ancienne). If you are in Montréal, we warmly invite you to view the Egyptian cat at the [Redpath Museum](https://museesmontreal.org/en/museums/redpath-museum). A [virtual museum exhibit](https://www.chamberofserendipity.ca/index.php) offers another way to explore this work from afar. 

## Materials and availability

### Dragonfly segmentation models

Eight trained model **folders** will be archived on Zenodo. These are Dragonfly 3D World model folders, not neural-network weights or checkpoint files. Download each complete folder, then in [Dragonfly 3D World](https://dragonfly.comet.tech/) open **Deep Learning → Import Folders** and select the downloaded folder.

Readers who need help with the import can consult or search the official [Dragonfly 3D World online manual](https://www.theobjects.com/dragonfly/dfhelp/2025-1/Default.htm).

Eligible academic users can request a free non-commercial [Dragonfly academic licence](https://dragonfly.comet.tech/en/products/license-models/academic-license).

Demers-Potvin, A. V., Jia, S., & Reznikov, N. (2026). Trained neural networks and slice analysis material for 'The life and afterlife of an ancient Egyptian cat reconstructed by µCT' [Dataset]. Zenodo. (https://doi.org/10.5281/zenodo.23924408)


### Images and CT stacks

The source images and CT stacks will be made available through the Federated Research Data Repository (FRDR), which is operated by the Digital Research Alliance of Canada (DRAC).

> <sub><i>Availability placeholder — add the FRDR collection link when the deposit is available.</i></sub>

## Reproducing the slice analysis

### Slice analysis

| Data file | Specimen | Description |
|---|---|---|
| `csv/RM2728-1_mummy.csv` | RM 2728.1 | Mummified cat |
| `csv/RM7303_african.csv` | RM 7303 | African cat |
| `csv/RM2018-07-01_domestic.csv` | RM 2018.07.01 | Domestic cat |
| `csv/RM2018-14-01_domestic.csv` | RM 2018.14.01 | Domestic cat |

1. **Fractal dimension per slice** — `imagej/01_compute_fractal_dimension.ijm`

   Run in Fiji/ImageJ (*Plugins > Macros > Run...*) once per specimen, on the
   8-bit binary TIFF stack of the turbinate ROI exported from Dragonfly.
   Slice files must be zero-padded (e.g. `slice_0001.tif`) so they are
   processed in order. Output: one CSV per specimen (`slice_index`,
   `fractal_dimension`), saved in `csv/`.

2. **Plots** — `python/02_plot_fractal_profiles.py`

   From the repository root:
   ```bash
   pip install -r requirements.txt
   python python/02_plot_fractal_profiles.py
   ```
   Produces Figure 8C (no smoothing) and Figure 8D (rolling mean over 45% of
   slices) in `figures/`.

See [supplementary-text.md](supplementary-text.md) for the scientific rationale, image preparation, box sizes, and processing details.

## Software versions

- Dragonfly 3D World: **2025.1**
- ImageJ: **1.53q** (Java 1.8.0_322)
- Python: **3.13**
- Python packages: **numpy 2.5.3, pandas 3.0.5, matplotlib 3.11.2** (see [requirements.txt](requirements.txt))

## Citation

If you use this material, please cite the article:

> Demers-Potvin, A. V., Jia, S., Schneider, M., Giakoumis, A., Hosseinitabatabaei, S., Chow, T., Shafique, I., Asali, M., Brailovski, V., Howell, A., Lussier, A., Nelson, A. J., & Reznikov, N. *The life and afterlife of an ancient Egyptian cat reconstructed by µCT*. Manuscript prepared for the *Journal of the Royal Society Interface*.

> <sub><i>Citation placeholder — replace the manuscript citation with the final year, volume, pages or article number, and DOI after publication.</i></sub>
