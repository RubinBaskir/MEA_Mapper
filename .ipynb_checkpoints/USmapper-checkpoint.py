def USmap(mapsize):
    '''This function plots a map of the US that also contains state borders.
    '''
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline

#This loads a GeoDataFrame usa using a shape file called "states_21basic"
usa = gpd.read_file('/Users/rubinbaskir/Desktop/states_21basic/states.shp')

#This codeblock creates a plot of the US using plt.subplots() with a size of z
fig, ax = plt.subplots(figsize=(mapsize,mapsize))
for state in usa.STATE_ABBR:
   usa[usa.STATE_ABBR == state].plot(ax=ax, edgecolor='r', linewidth = 4)

#This tests that the mapsize input is an integer
#assert type mapsize == int