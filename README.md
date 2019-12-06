This is the MEA Mapper
    
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
3. Connects each dot with a line that has an arrow on the end indicating the direction of the vehicle
4. Seperate the paths of the two MEAs that are currently in operation
        
### Step 1: Import address
### Step 2: 
### Step 3: Plot US Map

This is done using the following command:

 conda install -c conda-forge geopandas
 
 [GeoPandas Install](http://geopandas.org/install.html)
    
Some Magic stuff with condas happens here

I basically used this approach: https://medium.com/@erikgreenj/mapping-us-states-with-geopandas-made-simple-d7b6e66fa20d

#### How to plot cities

I loaded cities using a shape file shown here: https://hub.arcgis.com/datasets/b71337fab097494daa725fb0d75758ef_0?geometry=61.175%2C-8.444%2C72.776%2C74.580

This webpage on geopandas was also helpful:http://geopandas.org/gallery/create_geopandas_from_pandas.html

Could plot an individual city and all cities easily - but I wanted to plot a series of cities instead.

The instructor recommended this approach:

'''
city_points.loc[]
city_points.apply(lambda row: row.plot(ax=ax, color = 'white', linewidth = 20), axis =0)
'''

Haven't really figured that out yet. He also recommended using 'seaborn': https://seaborn.pydata.org/introduction.html

#### How to create a line segment

Not sure about this yet, but the following websites may be the answer:
1. http://ryan-m-cooper.com/blog/gps-points-to-line-segments.html
2. https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972
3. https://stackoverflow.com/questions/51071365/convert-points-to-lines-geopandas




