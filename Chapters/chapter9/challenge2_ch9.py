import arcpy
from arcpy import env
env.workspace = "P:/Fall_2015/Python_Programing/Python/Data/Exercise09"

arcpy.CreateFileGDB_management("P:/Fall_2015/Python_Programing/Python/Data/Exercise09/Results", "Challenge2")

Input_Rasters = arcpy.ListRasters()
for raster in Input_Rasters:
    arcpy.RasterToGeodatabase_conversion(raster, "P:/Fall_2015/Python_Programing/Python/Data/Exercise09/Challenge2.gdb")
