import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "P:/Fall_2015/Python_Programing/Python/Data/Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    goodlandcover = RemapValue([[41,1], [42,1], [43,1]])
    outreclass = Reclassify("landcover.tif", "VALUE", goodlandcover, "NODATA")
    outreclass.save("P:/Fall_2015/Python_Programing/Python/Data/Exercise09/Results/good_lc")
    goodlc = "P:/Fall_2015/Python_Programing/Python/Data/Exercise09/Results/good_lc"
    slope = "P:/Fall_2015/Python_Programing/Python/Data/Exercise09/Slope"
    aspect = "P:/Fall_2015/Python_Programing/Python/Data/Exercise09/Aspect"
    idealslope = RemapRange([[0, 5, 0], [5, 20, 1], [20, 75, 0]])
    goodslope = Reclassify(slope, "VALUE", idealslope, "NODATA")
    idealaspect = RemapRange([[0, 150, 0], [150, 270, 1], [270, 360, 0]])
    goodaspect = Reclassify(aspect, "VALUE", idealaspect, "NODATA")    
    tempraster = Plus(goodlc, goodslope)
    tempraster2 = Plus(tempraster, goodaspect)
    outraster = Divide(tempraster2, 3)
    outraster.save("P:/Fall_2015/Python_Programing/Python/Data/Exercise09/Results/final")      
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
