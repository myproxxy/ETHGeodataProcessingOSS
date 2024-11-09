# Extraktion aller Zentroide der Gemeinden
centroidFl = os.path.join('Data','centroidsGemSo.csv')
print(path2ds)
with open(centroidFl, 'w', encoding='utf-8') as centroidFl:
    centroidFl.write("GemName,X,Y\n")
    for feature in layer:
        geometry = feature.GetGeometryRef()
        minEasting,maxEasting,minNorthing,maxNorthing = geometry.GetEnvelope()
        centerX = (minEasting + maxEasting)/2
        centerY = (minNorthing + maxNorthing)/2
        gemName = feature.GetField('gmde_name')
        ftrInfo = f"{gemName},{centerX},{centerY}\n"
        centroidFl.write(ftrInfo)



# Lösung Lukas

import csv

dict = [['Gemeinde', 'Centroid']]

for feature in layer:
    name = feature.GetField("name")
    polygon = feature.GetGeometryRef()
    centroid = polygon.Centroid()
    dict.append([name, centroid])
    
with open('solothurn_center.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(dict)

with open('solothurn_center.csv', 'r', encoding='utf-8') as csvfile:
    for row in csvfile:
        print(row)