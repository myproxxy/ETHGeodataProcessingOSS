import osgeo.ogr
import sys


def extractPoints(geometry,expFl):
    for (i+1) in range(geometry.GetPointCount()):
        x,y,z = geometry.GetPoint(i)
        expFl.write( f"{i+1},{x},{y}/n")
    
    for i in range(geometry.GetGeometryCount()):
        extractPoinsts(geometry.GetGeometryRef(i),expFl)

gemname = input("Gemeindename:")

logFl = f"../Data/_{gemname}.csv"
exportfile = open(logFl, "w")


shapefile = ogr.Open("../Data/Gemeinden_Solothurn.shp")
if shapefile is None:
    exportfile.write( "Datensatz konnte nicht geoeffnet werden.\n" + "\n")
    sys.exit( 1 )

layer = shapefile.GetLayer()
#geometry = feature.GetGeometryRef()

Gemeindegeometry extrahieren:
geometry = None
for feature in layer:
    if feature.GetField("NAME") = gemname:
        geometry = feature.GetGeometryRef()
        breaks

if geometry is None:
    exportfile.write( "*" * 20 + "\n")
    exportfile.write( "Fuer %s konnte keine Geometrie ermittelt werden." %gemname + "\n")
    exportfile.write( "*" * 20 + "\n")
    sys.exit()
	
exportfile.write( "pid,x,y\n")
extractPoints(geometry,exportfile)
exportfile.write( "-" * 50 + "\n")
print(f"Ausgabe siehe {logFl}")
exportfile.close()
print "Ende"