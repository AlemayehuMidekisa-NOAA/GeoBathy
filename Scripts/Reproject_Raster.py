# This script is used to reproject a raster tile.

import arcpy, os, time
from arcpy import env
from arcpy.ia import *


#Start time
start = time.process_time()

arcpy.env.overwriteOutput = True

env.workspace = 'input directory'
outws = 'output directory'

rasterlist = arcpy.ListDatasets("*", "Raster")
for i in rasterlist:
    print(i)
    name = i.split(".")
    #Apply fill

    outname = os.path.join(outws, str(name[0]) + "_Proj.tif")
    
    # reproject the input raster 
    reprojected_raster = arcpy.ia.Reproject(i, {"wkid" : 4326})

    # verify the new coordinate system
    prj = print(arcpy.Describe(reprojected_raster).spatialReference.name)

    # save the output
    reprojected_raster.save(outname) 

   
print("Done processing!")

#End time
end = time.process_time()
total_seconds = end - start
total_minutes = int(total_seconds // 60)
print(total_minutes)
