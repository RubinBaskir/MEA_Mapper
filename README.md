#### This is the MEA Mapper
    
### Background
    
I work for the All of Us Research Program, a longitidinal research study funded by the Instistutes of Health looking to enroll a million or more people for 10 years or more. This program has many moving parts and many assets to help acheive its goals.
    
One of those assets is the Mobile Engagement Asset (MEA), mobile vehicles that can meet people where they are. People can learn about the program, create an account onboard, and even constribute physical measurements and biospecimens on the vehicle.
    
### Why this exists
    
Sounds great, right? It is! 
    
This vehicle is a great way for communtities who are underrepresented in biomedical research to engage with the research community.
    
**So why create a project around it?**
    
The vehicles have lots of metrics recorded on board to help optimize them. One of the things I'm most interested in is looking at how the vehicles perform at each of their stops throughout the US (as I'm writing this, the MEAs have visited over 500 stops). This is difficult to do with exisiting graphing software
    
### What this should do
    
This program should do the following:
1. Upon execution, take a static dictionary of addresses
2. Plots these addresses on a map of the US
3. Connects each dot with a line indicating the path of the vehicle

        
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

 conda install -c conda-forge geopandas
 
I had lots of trouble here because my path was incorrect, so be sure to check this if you're having trouble.

Once you have geogandas installed, download the shape file containing state information here:
[US map](https://www.arcgis.com/home/item.html?id=b07a9393ecbd430795a6f6218443dccc)

Once I have this file downloaded, I created a GeoPandas DataFrame from it called `usa`:
'usa = gpd.read_file('/Users/rubinbaskir/Desktop/states_21basic/states.shp')'

A good check here is 'print(usa)' - this gave me a sense of what information was contained in the DataFrame.

Next, I created a figure using matplotlib:
'fig, ax = plt.subplots(figsize=(100,100))'

I then created a for loop that plots each state in 'usa' using the state abbreviation column:
'for state in usa.STATE_ABBR:
   usa[usa.STATE_ABBR == state].plot(ax=ax, edgecolor='r', linewidth = 4)'

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

This plots all cities easily - but I wanted to plot two of cities.

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

I used these websites as some background:
1. http://ryan-m-cooper.com/blog/gps-points-to-line-segments.html
2. https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972
3. https://stackoverflow.com/questions/51071365/convert-points-to-lines-geopandas

## A note on modules and functions
I went about this backwards, and made all my code first, and then modularized it afterward, which is the opposite of what you're supposed to do.

For Part 1, I made the module `USmapper` with the function `USmap`. This makes the US map.
For Part 2, I made the module `CITYmapper` with the function `CITYmap`. This plots cities that the user specifies.
For Part 3 - if I can get it to work - I made `CITYlinker` with the function `CITYlink` that connects cities specified in `CITYmapper`.

## A note on pytest and testing

I had some difficulty using pytest, but for the sake of trying, I added some small tests for each module.

1. `USmapper` has code to test that the user is entering an integer when defining the figure size:
```assert type mapsize == int```
2. `CITYmapper` had code to test that user entered cities are not duplicates and that they are entered as strings:
```
assert x != y
assert type(x) == str
assert type(y) == str
```
3. `CITYlinker` will have some testing code, when I finally write it - or remove it from the project!


