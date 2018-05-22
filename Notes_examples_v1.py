'''
Installing packages in python

Open cmd windio 
Type following code:

python  -m pip install holoviews

'''
from osgeo import ogr

shapefile = ogr.Open(r"E:\#Python\Datasets\TM_WORLD_BORDERS-0.3\TM_WORLD_BORDERS-0.3.shp")
layer = shapefile.GetLayer(0)

countries = [] # List of (code,name,minLat,maxLat,
# minLong,maxLong) tuples.

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    countryCode = feature.GetField("ISO3")
    countryName = feature.GetField("NAME")
    geometry = feature.GetGeometryRef()
    minLong,maxLong,minLat,maxLat = geometry.GetEnvelope()

    countries.append((countryName,countryCode,minLat,maxLat,minLong,maxLong))

countries.sort()

for name,code,minLat,maxLat,minLong,maxLong in countries:
    print "%s (%s) lat=%0.4f..%0.4f, long=%0.4f..%0.4f" \
          % (name,code,minLat,maxLat,minLong,maxLong)



