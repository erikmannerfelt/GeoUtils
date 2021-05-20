"""Retrieve, save and print a string of information about a raster."""
import geoutils as gu

# Fetch an example file
filename = gu.datasets.get_path("landsat_B4")

# Open the file
image = gu.Raster(filename)

information = image.info()

information = image.info(stats=True)

with open('file.txt', 'w') as fh:
        fh.writelines(information)
