import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "P:/Fall_2015/Python_Programing/python_data_and_exercises/Data/Exercise08"
env.overwriteOutput = True
outpath = "P:/Fall_2015/Python_Programing/python_data_and_exercises/Data/Exercise08/Results"
newfc = "newpolygon.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
coords = [[0, 0], [0, 1000], [1000, 1000], [1000, 0], [0, 0]]
cursor = arcpy.da.InsertCursor(outpath + '/' + newfc, ["SHAPE@"])
array = arcpy.Array()
for coord in coords:
    X, Y = coord
    array.add(arcpy.Point(X, Y))
    cursor.insertRow([arcpy.Polygon(array)])
del cursor 

