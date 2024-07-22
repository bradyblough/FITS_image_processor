# FITS Image Processor

This Python script processes a series of FITS (Flexible Image Transport System) files to compute the median image. This technique is useful in astronomical imaging for reducing noise and improving the quality of the final image. The script uses the `astropy.io.fits` library to handle FITS files and `numpy` for numerical operations.

## Features

- **File Processing**: Handles multiple FITS files to extract image data.
- **Error Handling**: Gracefully skips files that cannot be processed, logging an error message.
- **Median Calculation**: Computes the median of the stacked images to reduce noise.
- **Visualization**: Displays the median image using `matplotlib`, with a color map of 'plasma'.

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.x
- `numpy`
- `matplotlib`
- `astropy`

You can install the required packages using pip:

```bash
pip install numpy matplotlib astropy
```

## Usage

1. **Prepare FITS Files**: Place your FITS files in a directory. The script currently expects files to be in a `FITS_image_processor\data` subdirectory.
2. **Run the Script**: Execute the script with Python.

```bash
python main.py
```

3. **View the Result**: The script will display the median image using the`matplotlib` library. 

## Additional Info
This project was inspired by the course "Data-Driven Astronomy" on Coursera. This was my first foray into the astronomical research space, and so this project means a lot to me.
