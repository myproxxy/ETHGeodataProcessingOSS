def analyzeGeometry(geometry, indent=0):
    s = []
    s.append("  " * indent)
    s.append(geometry.GetGeometryName())
    if geometry.GetPointCount() > 0:
        s.append(" mit %d Stuetzpunkten" % geometry.GetPointCount())
    if geometry.GetGeometryCount() > 0:
        s.append(" enthaelt:")

    print ("".join(s))

    for i in range(geometry.GetGeometryCount()):
        analyzeGeometry(geometry.GetGeometryRef(i), indent+1)
