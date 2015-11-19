import arcpy
def countstringfields(table):
    count = 0
    fields = arcpy.ListFields(table)
    for field in fields:
        if field.type == 'String':
            count += 1
    print count
