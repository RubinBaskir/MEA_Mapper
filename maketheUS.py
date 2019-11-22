def mapmea():
    '''This is a module that takes addresses as arguements and plots them on a map of the US'''
    import geopandas
    import geoplot
    
    world = geopandas.read_file(
    geopandas.datasets.get_path('naturalearth_lowres')
)

    geoplot.polyplot(world, figsize=(8, 4))