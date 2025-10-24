# This script is used to extract topobathy values from a raster using model meshes.

import arcpy, os, time
from arcpy import env
from arcpy.sa import *


#Start time
start = time.process_time()

env.workspace = 'input directory'

#Select "Z" filed (elevation) with null values
shape = 'model mesh directory'

selection = arcpy.management.SelectLayerByAttribute(shape, "NEW_SELECTION", '"Z" IS NULL')
result = arcpy.management.GetCount(selection)

# Print the number of features using the Result object
print('{} has {} records'.format(selection, result[0]))

rasterlist = arcpy.ListDatasets("*", "Raster")
for i in rasterlist:
    print(i)
    name = i.split(".")

    AddSurfaceInformation(selection, i, "Z", "BILINEAR")
    

   
print("Done processing!")

#End time
end = time.process_time()
total_seconds = end - start
total_minutes = int(total_seconds // 60)
print(total_minutes)
