def CITYlink(City1,City2):
    '''This function takes two user defined cities in the form of strings, creates a linestring from them, and draws a line between those cities.
    
    '''
#This creates a GeoPandas DataFrame called city_points
city_points = gpd.read_file('/Users/rubinbaskir/Desktop/Cities_feature/Cities_feature.shp')

#This creates the shapely Points citypoint_1 and citypoint_2
citypoint_1 = city_points.loc[City1, 'geometry']
citypoint_2 = city_points.loc[City2, 'geometry']

#This tests that citypoint values are shapley Points
#assert type(citypoint_1) and type(citypoint_2) == Point

#This converts citypoint_1 and citypoint_2 from shapley Points to tuples
start, end = [(citypoint_1.x, citypoint_1.y), (citypoint_2.x, citypoint_2.y)]

#This tests that this converstion has happened
#assert start != citypoint_1 and end != citypoint_2

#This creates a linestring from the tuples start and end. Linestring won't work with Points
linker_linestring = LineString([start, end])

#This plots linker_linestring using matplotlib
plt.plot(linker_linestring)
