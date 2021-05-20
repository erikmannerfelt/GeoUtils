"""Example script to load a vector file."""
import geoutils as gu

filename = gu.datasets.get_path("glacier_outlines")

outlines = gu.Vector(filename)
# TEXT
# Load an example Landsat image
filename = gu.datasets.get_path("landsat_B4")
image = gu.Raster(filename)

# Generate a boolean mask from the glacier outlines.
mask = outlines.create_mask(image)
