import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "P:/Fall_2015/Python_Programing/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "P:/Fall_2015/Python_Programing/Python/Data/Exercise08"
newfc = "Results/HawaiiBoundBox.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
infile = "P:/Fall_2015/Python_Programing/Python/Data/Exercise08/Hawaii.shp"

xs = []
ys = []
cursor = arcpy.da.SearchCursor(infile, ["SHAPE@"])
for polygon in cursor:
    H = polygon[0]
    for part in range(H.partCount):
        for point in H.getPart(part):
            xs.append(point.X)
            ys.append(point.Y)
del cursor
print min(xs)
print max(xs)
print min(ys)
print max(ys)

cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
coords = [[min(xs), min(ys)], [min(xs), max(ys)], [max(xs), max(ys)], [max(xs), min(ys)], [min(xs), min(ys)]]
for coord in coords:
    X, Y = coord
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
del cursor
