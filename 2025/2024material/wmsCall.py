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
wmsfile = "wms.gif"
wmslink = "https://wms.geo.admin.ch/?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=ch.bafu.bundesinventare-bln&STYLES=default&CRS=EPSG:2056&BBOX=2550000,1060000,2660000,1140000&WIDTH=800&HEIGHT=582&FORMAT=image/png"
download(wmslink,path2save2,wmsfile)
