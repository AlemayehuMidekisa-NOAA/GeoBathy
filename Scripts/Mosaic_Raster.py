# This script is used to mosaic multiple raster tiles into a single raster.

import arcpy, os, time
from arcpy import env
from arcpy.sa import *


#Start time
start = time.process_time()

import os, arcpy


workspace  = 'input directory'
list_raster = [] # the list must exist before you can append

walk = arcpy.da.Walk(workspace, type="TIF")
output_location  = 'output directory'

for dirpath, dirnames, filenames in walk:
    for file in filenames:
        if ".tif" in file.lower():
            print(str(file))
            list_raster.append(os.path.join(dirpath,file)) 
            
           

ras_list = ";".join(list_raster)
arcpy.MosaicToNewRaster_management(ras_list, output_location, "input raster", "", "32_BIT_FLOAT", "", "1", "MEAN", "REJECT")
print("Done processing!")

#End time
end = time.process_time()
total_seconds = end - start
total_minutes = int(total_seconds // 60)
print(total_minutes)
