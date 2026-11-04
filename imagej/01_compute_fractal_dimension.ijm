// 01_compute_fractal_dimension.ijm
//
// Computes the box-counting fractal dimension (D) of the nasal turbinates on
// every slice of one specimen's micro-CT stack (Supplementary methods,
// "Slice analysis for fractal dimension measurement"; Figure 8C-D).
//
// Input:  a folder containing the turbinate ROI of ONE specimen, exported from
//         Dragonfly as a stack of 8-bit binary TIFF files (one file per slice).
// Output: a CSV file with two columns:
//             slice_index        1-based position of the slice in the stack
//             fractal_dimension  D value for that slice
//
// How to run (Fiji / ImageJ):
//   Plugins > Macros > Run... and select this file.
//   You will be asked for (1) the folder of TIFF slices, (2) the folder where
//   the CSV is saved and (3) a specimen name used as the CSV file name.
//   Run once per specimen.
//
// IMPORTANT: slices are processed in alphabetical order of their file names.
// File names must therefore be zero-padded (e.g. slice_0001.tif, not
// slice_1.tif), otherwise the slice order will be scrambled.
//
// Tested with: ImageJ 1.53q (Java 1.8.0_322)

// Settings 

// Box sizes (in pixels) used for box counting, as reported in the
// supplementary methods.
box_sizes = "2,3,4,6,8,12,16,32,64";

// Choose input and output 

input_folder  = getDirectory("Choose the folder of TIFF slices for ONE specimen");
output_folder = getDirectory("Choose the folder where the CSV will be saved");
specimen_name = getString("Specimen name (used as CSV file name)", "RM2728-1_mummy");
output_csv    = output_folder + specimen_name + ".csv";

// Process every slice 

setBatchMode(true);  // run without displaying images (much faster)

list = getFileList(input_folder);
Array.sort(list);    // alphabetical order = slice order (see note above)

f = File.open(output_csv);  // note: overwrites an existing file of that name
print(f, "slice_index,fractal_dimension");
count = 0;

for (i = 0; i < list.length; i++) {
    if (endsWith(list[i], ".tif") || endsWith(list[i], ".tiff")) {
        count++;
        open(input_folder + list[i]);

        // Invert so that the turbinate ROI corresponds to the foreground
        // pixels counted by the box count (see supplementary methods).
        run("Invert");

        // Built-in ImageJ tool (Analyze > Tools > Fractal Box Count).
        // D is read from the first row of the results table.
        run("Fractal Box Count...", "box_sizes=" + box_sizes);
        d_value = Table.get("D", 0);
        print(f, count + "," + d_value);

        run("Clear Results");
        close();

        if (count % 50 == 0) print("  " + count + " slices done");
    }
}

File.close(f);
setBatchMode(false);
print("Done! " + count + " slices written to " + output_csv);
