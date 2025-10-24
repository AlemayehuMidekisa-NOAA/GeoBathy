# This script is used to mask or subset a raster tile using a polygon or shapefile.

# Import system modules
import arcpy
import os
from arcpy import env
from arcpy.sa import *

#Start time
start = time.process_time()

arcpy.env.overwriteOutput = True

env.workspace = 'input directory'
outws = 'output directory'
inMaskData = 'mask file'


rasterlist = arcpy.ListDatasets("*", "Raster")
for i in rasterlist:
    print(i)
    name = i.split(".")
    #Apply fill

    outname = os.path.join(outws, str(name[0]) + "_Mask.tif")
    

    # Set local variables
    extraction_area = "INSIDE"
    
    # Execute ExtractByMask
    outExtractByMask = ExtractByMask(i, inMaskData, extraction_area)

    # Save the output 
    outExtractByMask.save(outname)



   
print("Done processing!")

#End time
end = time.process_time()
total_seconds = end - start
total_minutes = int(total_seconds // 60)
print(total_minutes)
