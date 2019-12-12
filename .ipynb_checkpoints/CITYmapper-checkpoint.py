def CITYmap(City1,City2):
    '''This function takes two cities (written as two seperate stings), and plots them on an existing map. Note that is must be used after the USmapper() function, and must use the same integer USfiguresize 
    '''
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline

#This loads a GeoDataFrame city_points using a shape file called "Cities_feature"
city_points = gpd.read_file('/Users/rubinbaskir/Desktop/Cities_feature/Cities_feature.shp')

#This codeblock plots the two user defined cities "x" and "y"
fig, ax = plt.subplots(figsize=(100,100))
city_points.set_index("CITY_NAME", inplace=True)
city_points.loc[[City1, City2]].plot(ax=ax, color = 'white', linewidth = 20)

#These test that the City1 and City2 cities are not duplicates, and that they are entered as strings
#assert x != y
#assert type(x) == str
#assert type(y) == str
