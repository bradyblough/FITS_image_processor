import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt  

files = ['data\image0.fits', 'data\image1.fits', 'data\image2.fits', 'data\image3.fits', 'data\image4.fits', 'data\image5.fits', 'data\image6.fits', 'data\image7.fits', 'data\image8.fits', 'data\image9.fits', 'data\image10.fits', 'data\image11.fits']   

def median_fits(files):
    if not files:  
        raise ValueError('No files provided. Please provide at least one valid FITS file.')

    data_list = []

    for file in files:
        try:
            with fits.open(file) as hdulist:
                data_list.append(hdulist[0].data)
        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue

    stacked_data = np.stack(data_list, axis=0)
    median_data = np.median(stacked_data, axis=0)

    return median_data

median_data = median_fits(files)

plt.imshow(median_data, cmap='plasma')  
plt.xlabel('Right Ascension (RA)')  
plt.ylabel('Declination (Dec)')  
plt.colorbar()  
plt.show()  
