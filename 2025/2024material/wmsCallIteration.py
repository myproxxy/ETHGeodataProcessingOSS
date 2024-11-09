# -*- coding: utf-8 -*-
import os, shutil, sys
import urllib.request
from osgeo import gdal
from osgeo.gdalconst import *

def download(url, dest, fileName=None):
    try:
        r= urllib.request.urlopen(url)
        fileName = os.path.join(dest, fileName)
        with open(fileName, 'wb') as f:
            shutil.copyfileobj(r,f)
        r.close()
        print("Successfully downloaded resource {}".format(url))
    except:
        print("ERROR Downloading resource {}".format(url))

path2save2 = "Data/" #Zielpfad
for i in range(len(xList)):
    x = xList[i]
    y = yList[i]
    bb = f"{x},{y},{x+5000},{y+5000}"

    wmsfile = f"wms{bb}.gif"
    wmslink = f"https://wms.geo.admin.ch/?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=ch.bafu.bundesinventare-bln&STYLES=default&CRS=EPSG:21781&BBOX={bb}&WIDTH=800&HEIGHT=582&FORMAT=image/png"
    download(wmslink,path2save2,wmsfile)
