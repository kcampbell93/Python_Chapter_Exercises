"""Identify errors in following script:
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
FC = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
if fields.name == "NAME"
for row in rows:
print "Name = {0}".format(row.getValue(field.name))
"""

    #Error1: FC needs to be lowercase.
    #Error2: Make sure the env.workspace is correct pathway to shp.file.
    #Error3: Take off the .name in the if statement.
    #Error4: There should be a colon after the if statement.

#Correct Script:
import arcpy
from arcpy import env
env.workspace = "P:/Fall_2015/Python_Programing/Python/Data/Exercise07"
fc = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    if fields == "NAME":
        for row in rows:
            print "Name = {0}".format(row.getValue(field.name))            
