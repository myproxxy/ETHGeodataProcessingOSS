from osgeo import ogr
import sys

def metadataFromGisLayer(lyr,printOption=False):
    drv = ogr.GetDriverByName("ESRI Shapefile")
    path2ds = lyr
    datasource = drv.Open(path2ds)

    mylayer = datasource.GetLayer()
    print(f"Nun gesetzt: {mylayer.GetName()}")

    ftrcnt = mylayer.GetFeatureCount()
    mylayerDef = mylayer.GetLayerDefn()
    numatts = mylayerDef.GetFieldCount()
    if printOption:
        print("Der Datensatz '%s' hat %i Länder mit je %i Attributen" %(mylayer.GetName(),int(ftrcnt),int(numatts)))
    for i in range(numatts):
        fieldDef = mylayerDef.GetFieldDefn(i)
        if printOption:
            print("Attribut  %s ist vom Typ %s" %(fieldDef.GetName(),fieldDef.GetType()))
    sRs = mylayer.GetSpatialRef()
    if printOption:
        print("Layer %s hat folgendes Räumliches Bezugssytem: %s" %(mylayer.GetName(),sRs))

    extent = mylayer.GetExtent()
    if printOption:
        print(extent)
    ulx = round(float(extent[0]),4)
    uly = round(float(extent[2]),4)
    orx = round(float(extent[1]),4)
    ory = round(float(extent[3]),4)
    if printOption:
        print(f"Ausdehnung des Datensatzes '{mylayer.GetName()}':\nUnten links: ({ulx},{uly}) und oben rechts: ({orx},{ory})")
    
    print(mylayer)
    return mylayer
    
def getAttValsFromFeatureXY(curlyr,ftrNr):
    print("start...")
    feature = curlyr.GetFeature(ftrNr)
    print(curlyr.GetName())
    attributes = feature.items()
    print(attributes)
    for key,value in attributes.items():
        print(f"{key}: {value}")    
        
def main():
    myDataset = sys.argv[1]
    lyrInstance = metadataFromGisLayer(myDataset)
    print(lyrInstance.GetName()) 
    print("Attributevalues:")
    getAttValsFromFeatureXY(lyrInstance,0)
    
if __name__ == '__main__':
    main()