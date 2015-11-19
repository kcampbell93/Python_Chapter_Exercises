import arcpy
from arcpy import env
env.workspace ="P:/Fall_2015/Python_Programing/Python/Data/Exercise05/"
arcpy.Dissolve_management("parks.shp", "P:/Fall_2015/Python_Programing/Python/Data/Exercise05/parks_dissolve.shp","PARK_TYPE", "", "single_part", "")
