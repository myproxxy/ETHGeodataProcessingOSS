# obtained from http://www.gis.usu.edu/~chrisg/python/2009/lectures/ospy_slides4.pdf and adapted
# script to get pixel values at a set of coordinate by reading in one pixel at a time

import os, sys, numpy, time
from osgeo import gdal
from osgeo.gdalconst import *

# start timing
startTime = time.time()
# coordinates to get pixel values for
xValues = [594000.0, 604000.0, 613500.0,599594.0]
yValues = [229500.0, 231000.0, 222800.0,226081.0]

# register all of the drivers
gdal.AllRegister()
# open the image
ds = gdal.Open('Data/ortho14_5m_rgb_solothurn.tif', GA_ReadOnly)
if ds is None:
    print ('Could not open image')
    sys.exit()

# get image size
rows = ds.RasterYSize
cols = ds.RasterXSize
bands = ds.RasterCount
# get georeference info
transform = ds.GetGeoTransform()
xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = transform[5]
print('X | Y | xOffset | yOffset | Wert Band 1 | Wert Band 2 | Wert Band 3 ')

# loop through the coordinates
#for i in range(3):
for i in range(len(xValues)):
    # get x,y
    x = xValues[i]
    y = yValues[i]
    # compute pixel offset
    xOffset = int((x - xOrigin) / pixelWidth)
    yOffset = int((y - yOrigin) / pixelHeight)
    # create a string to print out
    s = str(x) + ' ' + str(y) + ' ' + str(xOffset) + ' ' + str(yOffset) + ' '
    # loop through the bands
    for j in range(bands):
        band = ds.GetRasterBand(j+1) # 1-based index
        #read data and add the value to the string
        data = band.ReadAsArray(xOffset, yOffset, 1, 1)
        value = data[0,0]
        #print(data)
        #value2 = numpy.median(data)
        s = s + str(value) + ' '

    #print out the data string
    print(s)
# figure out how long the script took to run
endTime = time.time()
print()
print ('The script took %.3f seconds' %(endTime - startTime))