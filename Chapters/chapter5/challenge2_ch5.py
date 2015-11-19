import arcpy
from arcpy import env
env.workspace = "P:/Fall_2015/Python_Programing/Python/Data/Exercise05"
arcpy.Copy_management("hospitals.shp", "hospitalsXYpts.shp")
arcpy.AddXY_management("hospitals.shp")
