def MEAmap(x,y):
    '''This function plots a map of the US that also contains state borders.
    '''
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline

#This loads a GeoDataFrame usa using a shape file called "states_21basic"
usa = gpd.read_file('/Users/rubinbaskir/Desktop/states_21basic/states.shp')
city_points = gpd.read_file('/Users/rubinbaskir/Desktop/Cities_feature/Cities_feature.shp')

#This codeblock creates a plot of the US using plt.subplots()
fig, ax = plt.subplots(figsize=(100,100))
for state in usa.STATE_ABBR:
   usa[usa.STATE_ABBR == state].plot(ax=ax, edgecolor='r', linewidth = 4)
city_points.set_index("CITY_NAME", inplace=True)
city_points.loc[[x, y]].plot(ax=ax, color = 'white', linewidth = 20)

#assert usa.iloc[0,0] == 'Hawaii'