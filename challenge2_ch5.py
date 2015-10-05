Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import arcpy
>>> from arcpy import env
>>> env.workspace = "P:/Fall 2015/Python Programing/Python/Data/Exercise05"
>>> arcpy.Copy_management("hospitals.shp", "hospitalsXYptstaketwo.shp")
<Result 'P:/Fall 2015/Python Programing/Python/Data/Exercise05\\hospitalsXYptstaketwo.shp'>
>>> """I named the output location as hospitalsXYptstaketwo.shp because I had previously executed this code in ArcMap and needed to change the name inorder to save it in Python.

"""
