import arcpy
from arcpy import env
env.workspace = "P:/Fall_2015/Python_Programing/Python/Data/Exercise07"

unique_name = arcpy.CreateUniqueName("Results/airportbuf.shp")
arcpy.Select_analysis("P:/Fall_2015/Python_Programing/Python/Data/Exercise07/airports.shp", unique_name, """"FEATURE" = 'Airport'""")

unique_name = arcpy.CreateUniqueName("Results/seaplanebuf.shp")
arcpy.Select_analysis("P:/Fall_2015/Python_Programing/Python/Data/Exercise07/airports.shp", unique_name, """"FEATURE" = 'Seaplane Base'""")

unique_name = arcpy.CreateUniqueName("Results/buffer_airports.shp")
arcpy.Buffer_analysis("P:/Fall_2015/Python_Programing/Python/Data/Exercise07/Results/airportbuf.shp", unique_name, "15000 METERS")

unique_name = arcpy.CreateUniqueName("Results/buffer_seaplanebase.shp")
arcpy.Buffer_analysis("P:/Fall_2015/Python_Programing/Python/Data/Exercise07/Results/seaplanebuf.shp", unique_name, "7500 METERS")
