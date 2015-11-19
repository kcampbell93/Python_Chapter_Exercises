import arcpy
mxd = arcpy.mapping.MapDocument("P:/Fall_2015/Python_Programing/Python/Data/Exercise10/Austin_TX.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[1]
df2 = arcpy.mapping.ListDataFrames(mxd)[0]
addLayer = arcpy.mapping.Layer("P:/Fall_2015/Python_Programing/Python/Data/Exercise10/Austin/parks.shp")
arcpy.mapping.AddLayer(df, addLayer)
arcpy.mapping.AddLayer(df2, addLayer)
mxd.saveACopy("P:/Fall_2015/Python_Programing/Python/Data/Exercise10/Austin_TX2.mxd")
del mxd, addLayer
