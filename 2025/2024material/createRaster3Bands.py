from osgeo import gdal
from osgeo import osr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg
cmap = mpl.colormaps['viridis']

fn_create = "Data/gdalCreateRaster3.tif"  # filename for new raster
driver_gtiff = gdal.GetDriverByName('GTiff')
ds_create = driver_gtiff.Create(fn_create, xsize=10, ysize=10, bands=3, eType=gdal.GDT_Byte)

srs = osr.SpatialReference()
srs.ImportFromEPSG(21781)
ds_create.SetProjection(srs.ExportToWkt())

geot_create = [600000, 10.0, 0.0, 200000, 0.0, -10.0]
ds_create.SetGeoTransform(geot_create)
print(ds_create.GetGeoTransform())

data_createR = np.zeros((10, 10))
data_createR[:3, :10] = 255  # values to 1, leave outer as 0 (no data)
data_createG = np.zeros((10, 10))
data_createG[3:6, :10] = 255  # values to 1, leave outer as 0 (no data)
data_createB = np.zeros((10, 10))
data_createB[6:10, :10] = 255  # values to 1, leave outer as 0 (no data)

ds_create.GetRasterBand(1).WriteArray(data_createR)  # write the array to the raster
ds_create.GetRasterBand(1).SetNoDataValue(0)  # set the no data value
ds_create.GetRasterBand(2).WriteArray(data_createG)  # write the array to the raster
ds_create.GetRasterBand(2).SetNoDataValue(0)  # set the no data value
ds_create.GetRasterBand(3).WriteArray(data_createB)  # write the array to the raster
ds_create.GetRasterBand(3).SetNoDataValue(0)  # set the no data value

ds_create = None  # properly close the raster

image = mpimg.imread(fn_create)
# plot the data values we created
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.colorbar()