from osgeo import ogr
import shapely.wkt

shapefile = ogr.Open("Data/Gemeinden_Solothurn.shp")
if shapefile is None:
    print ("Datensatz konnte nicht geoeffnet werden.\n")
    sys.exit()

layer = shapefile.GetLayer(0)

#Gemeindegeometry extrahieren:
geometry = None
cnt = 0
for feature in layer:
    while cnt < 1:
        #Extract Gemeinde-Name
        gemname = feature.GetField("gmde_name")
        #Get Geometry (Polygon)
        gemgeometry = feature.GetGeometryRef()
        #"Convert" Geometry to shapely-geometry
        gemgeomaswkt = gemgeometry.ExportToWkt()
        shapelypolygon = shapely.wkt.loads(gemgeomaswkt)
        #Extract Centroid
        centroid_point = shapelypolygon.centroid
        x=centroid_point.x
        y=centroid_point.y
        area = shapelypolygon.area
        #Printout Information
        print ("Gemeinde %s hat folgenden Zentroid: (%f, %f) und folgende Flaeche %fm2" %(gemname, x, y, area))
        cnt += 1