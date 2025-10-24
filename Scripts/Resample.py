# This script is used to resample a DEM to a different spatial resolution (e.g. 30m).

import arcpy, os, time
from arcpy import env
from arcpy.sa import *


#Start time
start = time.process_time()

env.workspace = 'input directory'
outws = 'output directory'

rasterlist = arcpy.ListDatasets("*", "Raster")
for i in rasterlist:
    print(i)
    name = i.split(".")
    #Apply fill

    outname = os.path.join(outws, str(name[0]) + "_Res_30m.tif")
    arcpy.Resample_management(i, outname, "30", "BILINEAR")
    

   
print("Done processing!")

#End time
end = time.process_time()
total_seconds = end - start
total_minutes = int(total_seconds // 60)
print(total_minutes)
