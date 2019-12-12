##### This is the MEA Mapper
    
### Background
    
I work for the All of Us Research Program, a longitidinal research study funded by the National Institutes of Health looking to enroll a million or more people for 10 years or more. This program has many moving parts and many assets to help acheive its goals.
    
One of those assets is the Mobile Engagement Asset (MEA), mobile vehicles that can meet people where they are. People can learn about the program, create an account onboard, and even constribute physical measurements and biospecimens on the vehicle.
    
### Why this exists
    
Sounds great, right? It is! 
    
This vehicle is a great way for communtities who are underrepresented in biomedical research to engage with the research community.
    
**So why create a project around it?**
    
The vehicles have lots of metrics recorded on board. One of the things I'm most interested in is looking at how the vehicles perform at each of their stops throughout the US (as I'm writing this, the MEAs have visited over 500 stops). This is difficult to do with exisiting graphing software
    
### What this should do
    
This program should do the following:
1. Upon execution, take two user defined cities
2. Plots these cities on a map of the US
3. Connect each dot with a line indicating the path of the vehicle from one city to another

        
### Step 1: Plot US Map
I used this approach: https://medium.com/@erikgreenj/mapping-us-states-with-geopandas-made-simple-d7b6e66fa20d



First, you'll need to download the following modules:
1. geopandas
2. shapely
3. matplotlib
4. pandas

Geopandas is important because its how you'll create your US map:
[GeoPandas Install](http://geopandas.org/install.html)

This is done using the following command:

 `conda install -c conda-forge geopandas`
 
I had lots of trouble here because my path was incorrect, so be sure to check this if you're having trouble.

Once you have geopandas installed, download the shape file containing state information here:
[US map](https://www.arcgis.com/home/item.html?id=b07a9393ecbd430795a6f6218443dccc)

Once I have this file downloaded, I created a GeoPandas DataFrame from it called `usa`:
`usa = gpd.read_file('/Users/rubinbaskir/Desktop/states_21basic/states.shp')`

A good check here is `print(usa)` - this gave me a sense of what information was contained in the DataFrame.

Next, I created a figure using matplotlib:
`fig, ax = plt.subplots(figsize=(100,100))`

I then created a for loop that plots each state in `usa` using the state abbreviation column:
```
for state in usa.STATE_ABBR:
   usa[usa.STATE_ABBR == state].plot(ax=ax, edgecolor='r', linewidth = 4)
```

I now had a US map with every state outlined.

### Step 2: Plot cities
I loaded cities using a shape file shown here: https://hub.arcgis.com/datasets/b71337fab097494daa725fb0d75758ef_0?geometry=61.175%2C-8.444%2C72.776%2C74.580

This webpage on geopandas was also helpful:http://geopandas.org/gallery/create_geopandas_from_pandas.html

```
fig, ax = plt.subplots(figsize=(100,100))
for state in usa.STATE_ABBR:
   usa[usa.STATE_ABBR == state].plot(ax=ax, edgecolor='r', linewidth = 4)
city_points.plot(ax=ax, color = 'black')
```

This plots all cities easily - but I wanted a plot of two cities.

The instructor recommended this approach:

```
city_points.loc[]
city_points.apply(lambda row: row.plot(ax=ax, color = 'white', linewidth = 20), axis =0)
```

I couldn't figure out the `apply` approach, so I tried focusing on how to retrieve my information through indexing. 

I was struggling with this until I used the following command:

```
city_points.set_index("CITY_NAME", inplace=True)
```
This places the column CITY_NAME as the first column and allows `loc` to index off of a city name. 

Once I figured that out, this code block worked:

```
fig, ax = plt.subplots(figsize=(100,100))
for state in usa.STATE_ABBR:
   usa[usa.STATE_ABBR == state].plot(ax=ax, edgecolor='r', linewidth = 4)
city_points.loc[['St. Louis', 'New York', 'Austin', 'Chicago']].plot(ax=ax, color = 'white', linewidth = 20)
```

### Connect cities

I used these websites as some background (in order of usefullness):
1. http://ryan-m-cooper.com/blog/gps-points-to-line-segments.html
2. https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972
3. https://stackoverflow.com/questions/51071365/convert-points-to-lines-geopandas



To connect the two cities, I created a module called CITYlinker with the function CITYlink that creates a linestring from the geometries found attached to the citypoints GeoPandas DataFrame.

I first created citypoint_1 and citypoint_1, which are the values found in the geometry column of the user defined cities City1 and City2,

```
citypoint_1 = city_points.loc[City1, 'geometry']
citypoint_2 = city_points.loc[City2, 'geometry']
```
Right now, citypoint_1 and citypoint_2 are Points. To make them a linestring, we need to convert them into tuples.
```
start, end = [(citypoint_1.x, citypoint_1.y), (citypoint_2.x, citypoint_2.y)]
```
Now we can create a linestring out of the tuples `start` and `end`.
```
linker_linestring = LineString([start, end])
```
Graphing `linker_linestring` was a little tricky.

The most useful website for this turned out to be the documentation on LineStrings:
https://shapely.readthedocs.io/en/stable/manual.html#linestrings

This codeblock from the shapely documentation was esstential in figuring out how to plot a linestring:
```
from matplotlib import pyplot
from shapely.geometry import LineString

from figures import SIZE

COLOR = {
    True:  '#6699cc',
    False: '#ffcc33'
    }

def v_color(ob):
    return COLOR[ob.is_simple]

def plot_coords(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, 'o', color='#999999', zorder=1)

def plot_bounds(ax, ob):
    x, y = zip(*list((p.x, p.y) for p in ob.boundary))
    ax.plot(x, y, 'o', color='#000000', zorder=1)

def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=v_color(ob), alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)

fig = pyplot.figure(1, figsize=SIZE, dpi=90)

# 1: simple line
ax = fig.add_subplot(121)
line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])

plot_coords(ax, line)
plot_bounds(ax, line)
plot_line(ax, line)
```
The code here that we're interested in is the code for the function `plot_line`:
```
def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=v_color(ob), alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)
```
Once we have `plotline` created, we can use it to plot `linker_linestring`:
`plot_line(ax,linker_linestring)`

## A note on modules and functions
I went about this backwards, and made all my code first, and then modularized it afterward, which is the opposite of what you're supposed to do.

For Part 1, I made the module `USmapper` with the function `USmap`. This makes the US map.
For Part 2, I made the module `CITYmapper` with the function `CITYmap`. This plots cities that the user specifies.
For Part 3 - if I can get it to work - I made `CITYlinker` with the function `CITYlink` that connects cities specified in `CITYmapper`.

## A note on pytest and testing

I had some difficulty using pytest, but for the sake of trying, I added some small tests for each module.

1. `USmapper` has code to test that the user is entering an integer when defining the figure size:
```assert type mapsize == int```
2. `CITYmapper` has code to test that user entered cities are not duplicates and that they are entered as strings:
```
assert x != y
assert type(x) == str
assert type(y) == str
```
3. `CITYlinker` has code to test that citypoint values are Points and tests that these Points are converted to tuples that can be converted into a linestring:
```
assert type(citypoint_1) and type(citypoint_2) == Point
assert start != citypoint_1 and end != citypoint_2
```
## The final project
If none of my functions work, this code below can be run as a proof of concept:
```
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
fig, ax = plt.subplots(figsize=(100,100))
for state in usa.STATE_ABBR:
   usa[usa.STATE_ABBR == state].plot(ax=ax, edgecolor='r', linewidth = 4)
city_points.loc[['Anchorage', 'Fort Worth']].plot(ax=ax, color = 'black', linewidth = 80)
def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color='r', alpha=0.7, linewidth=30, solid_capstyle='round', zorder=2)
citypoint_1 = city_points.loc['Anchorage', 'geometry']
citypoint_2 = city_points.loc['Fort Worth', 'geometry']
start, end = [(citypoint_1.x, citypoint_1.y), (citypoint_2.x, citypoint_2.y)]
linker_linestring = LineString([start, end])
plot_line(ax,linker_linestring)
```
