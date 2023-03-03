from osgeo import ogr
from osgeo import osr
from osgeo import gdal
from osgeo import gdalconst
from osgeo import ogr
import sys,os

if len(sys.argv)  < 5 :
    print ("Verwendung: python extractMBR.py <Ausgangs-SHP> <ZielLayer> <ZielFormat> <ZielAttribut> <Attributfilter (optional)>")
    print ('z.B. python extractMBR.py ../Daten/Gemeinden_Solothurn.shp areaMBR.tab "MapInfo File" Name "Name like \'A%\'"')
    sys.exit(1)

sourcelayer = sys.argv[1]
destinationlayername = sys.argv[2]
destinationformat = sys.argv[3]
sourcefieldname = sys.argv[4]
if len(sys.argv)>5:
    filtercondition = sys.argv[5]
else:
    filtercondition = None

shapefile = ogr.Open(sourcelayer)
if shapefile is None:
        print("Datensatz konnte nicht geoeffnet werden.\n")
        sys.exit()

sourcelayer = shapefile.GetLayer(0)
srs = osr.SpatialReference()
srs.ImportFromProj4(sourcelayer.GetSpatialRef().ExportToProj4())

driver = ogr.GetDriverByName(destinationformat)
destinationFile = driver.CreateDataSource(destinationlayername)
destinationLayer = destinationFile.CreateLayer(destinationlayername[0:len(destinationlayername)-4], srs)

#Create Field to store the name
fieldDef = ogr.FieldDefn(sourcefieldname, ogr.OFTString)
fieldDef.SetWidth(100)
destinationLayer.CreateField(fieldDef)

if filtercondition is not None:
    sourcelayer.SetAttributeFilter(filtercondition)
feature = sourcelayer.GetNextFeature()
while feature:
    #Get value of Feature-Name
    ftrName = feature.GetField(sourcefieldname)
    #Get MBR
    geometry = feature.GetGeometryRef()
    minEasting,maxEasting,minNorthing,maxNorthing = geometry.GetEnvelope()
    print("*"*20)
    print(geometry.GetEnvelope())

    linearRing = ogr.Geometry(ogr.wkbLinearRing)
    linearRing.AddPoint(minEasting, minNorthing)
    linearRing.AddPoint(maxEasting, minNorthing)
    linearRing.AddPoint(maxEasting, maxNorthing)
    linearRing.AddPoint(minEasting, maxNorthing)
    linearRing.AddPoint(minEasting, minNorthing)
    mbr = ogr.Geometry(ogr.wkbPolygon)
    mbr.AddGeometry(linearRing)
    mbrfeature = ogr.Feature(destinationLayer.GetLayerDefn())
    mbrfeature.SetGeometry(mbr)
    mbrfeature.SetField(sourcefieldname, ftrName)
    destinationLayer.CreateFeature(mbrfeature)
    mbrfeature.Destroy()

    feature = sourcelayer.GetNextFeature()

shapefile.Destroy()
destinationFile.Destroy()
print ("Datei wurde erstellt: %s" %(destinationlayername))
