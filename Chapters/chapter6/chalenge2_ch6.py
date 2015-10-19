
import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "P:/Fall_2015/Python_Programing/Python/Data/Exercise06"
arcpy.CreateFileGDB_management("P:/Fall_2015/Python_Programing/Python/Data/Exercise06/Results", "NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "P:/Fall 2015/Python_Programing/Python/Data/Exercise06/Results/NM.gdb/" + fcdesc.basename)
