def MEAmap(City1,City2):
    '''This function plots a map of the US that also contains state borders, plots two cities defined as strings City1 and City, and plots a line connecting these points.
    ex: MEAmap(City1,City2)
    MEAmap('St. Louis', 'New York')
    '''
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

#This loads a GeoDataFrame usa using a shape file called "states_21basic"
usa = gpd.read_file('/Users/rubinbaskir/Desktop/states_21basic/states.shp')
city_points = gpd.read_file('/Users/rubinbaskir/Desktop/Cities_feature/Cities_feature.shp')

#This codeblock creates a plot of the US using plt.subplots()
fig, ax = plt.subplots(figsize=(100,100))
for state in usa.STATE_ABBR:
   usa[usa.STATE_ABBR == state].plot(ax=ax, edgecolor='r', linewidth = 4)
city_points.set_index("CITY_NAME", inplace=True)
city_points.loc[[City1, City2]].plot(ax=ax, color = 'white', linewidth = 20)

#assert usa.iloc[0,0] == 'Hawaii'
def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color='r', alpha=0.7, linewidth=30, solid_capstyle='round', zorder=2)
    
citypoint_1 = city_points.loc[City1, 'geometry']
citypoint_2 = city_points.loc[City2, 'geometry']
start, end = [(citypoint_1.x, citypoint_1.y), (citypoint_2.x, citypoint_2.y)]
linker_linestring = LineString([start, end])
plot_line(ax,linker_linestring)