import arcpy
from arcpy import env
env.workspace =  "P:/Fall 2015/Python_Programing/Python/Data/Exercise05"

extensions = ['Spatial', '3d', 'Network']
print("The following extensions are available:")
for extension in extensions:
    if arcpy.CheckExtension(extension) == "Available":
        print("{} is available.".format(extension))
