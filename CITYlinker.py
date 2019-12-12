def CITYlink(City1,City2):
    '''This function takes two user defined cities in the form of strings, creates a linestring from them, and draws a line between those cities.
    
    '''
#This creates a GeoPandas DataFrame called city_points
city_points = gpd.read_file('/Users/rubinbaskir/Desktop/Cities_feature/Cities_feature.shp')

#%matplotlib inline renders a figure in a Jupyter Notebook. It makes things easier to plot upon executing this function
%matplotlib inline

#This creates a function called plot_line that plots an object passed to it as an array
def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color='r', alpha=0.7, linewidth=30, solid_capstyle='round', zorder=2)
    
#This creates the shapely Points citypoint_1 and citypoint_2
citypoint_1 = city_points.loc[City1, 'geometry']
citypoint_2 = city_points.loc[City2, 'geometry']

#This tests that citypoint values are shapley Points
#assert type(citypoint_1) and type(citypoint_2) == Point

#This converts citypoint_1 and citypoint_2 from shapley Points to tuples
#I think the reason why I get two lines vs one has to do with this step
start, end = [(citypoint_1.x, citypoint_1.y), (citypoint_2.x, citypoint_2.y)]

#This tests that this converstion has happened
#assert start != citypoint_1 and end != citypoint_2

#This creates a linestring from the tuples start and end. Linestring won't work with Points
linker_linestring = LineString([start, end])

#This plots linker_linestring using matplotlib and the plot_line function
plot_line(ax,linker_linestring)
