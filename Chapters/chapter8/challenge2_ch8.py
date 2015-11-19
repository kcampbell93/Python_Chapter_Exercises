import arcpy
SR = "P:/Fall_2015/Python_Programing/Python/Data/Exercise08/Hawaii.shp"
units = SR.linearUnitName

fc = SR = "P:/Fall_2015/Python_Programing/Python/Data/Exercise08/Hawaii.shp"
SR = arcpy.Describe(fc).spatialReference
units = SR.linearUnitName
 
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for OID, shape in cursor:
    print "Feature: {}/tTotal Area: {} {}^2".format(OID, shape.area, units)
    partnum = 0
    for part in shape:
        pn = arcpy.Polygon(part, SR)
	print "\tPart: {}\t Area: {} {}^2\tPerimeter: {} {}".format(partnum, pn.area, units, pn.length, units)
	partnum += 1
