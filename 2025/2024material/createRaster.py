from osgeo import gdal
from osgeo import osr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
cmap = mpl.colormaps['viridis']

fn_create = "Data/gdalCreateRaster.tif"  # filename for new raster
driver_gtiff = gdal.GetDriverByName('GTiff')
ds_create = driver_gtiff.Create(fn_create, xsize=10, ysize=10, bands=1, eType=gdal.GDT_Byte)

srs = osr.SpatialReference()
srs.ImportFromEPSG(21781)
ds_create.SetProjection(srs.ExportToWkt())

geot_create = [600000, 10.0, 0.0, 200000, 0.0, -10.0]
ds_create.SetGeoTransform(geot_create)
print(ds_create.GetGeoTransform())

data_create = np.zeros((10, 10))
data_create[1:-1, 1:-1] = 1  # values to 1, leave outer as 0 (no data)
data_create[3:-3, 3:-3] = 2  # set center group as 2
data_create[4:-4, 4:-4] = 3  # set center pixels to 3

ds_create.GetRasterBand(1).WriteArray(data_create)  # write the array to the raster
ds_create.GetRasterBand(1).SetNoDataValue(0)  # set the no data value
ds_create = None  # properly close the raster
# plot the data values we created
plt.figure(figsize=(10, 10))
plt.imshow(data_create, cmap='Oranges')
plt.colorbar()