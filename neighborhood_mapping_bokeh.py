# This script will map the properites owned by a given entity (assuming the mailing address is a proxy for ownership)- you just need too input the mailing address .
from shapely.geometry import Point, Polygon
import geopandas as gpd
import geojsonio
from datetime import datetime
import matplotlib.pyplot as plt
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure, gmap
from bokeh.models import GeoJSONDataSource, LinearColorMapper, CategoricalColorMapper, GMapOptions, HoverTool
from bokeh.palettes import brewer
import os
import numpy as np
from dotenv import load_dotenv
load_dotenv()

LandlordAddress = "1333 PARK AVE EMERYVILLE CA 94608"

# parcels = gpd.read_file("https://opendata.arcgis.com/datasets/b55c25ae04fc47fc9c188dbbfcd51192_0.geojson") # full Alameda county data from API:

parcels = gpd.read_file('parcels_94608.geojson') # geojson for a small zip code - much faster than using full county data above

parcels['highlight'] = np.where(parcels['MailingAddress'] == LandlordAddress, 'yes', 'no') # prepares us to highlight parcels with a particular mailing address (our proxy for ownership)

map_options = GMapOptions(lat=37.84, lng=-122.2835, map_type="hybrid", zoom=15)

API_KEY = os.getenv('GMAP_API_KEY')
p = gmap(API_KEY, map_options,plot_width=1000, plot_height=1000) #creates our map!

p.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
p.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks
p.xaxis.major_tick_line_color = None  # turn off y-axis major ticks
p.xaxis.minor_tick_line_color = None  # turn off y-axis minor ticks
p.xaxis.major_label_text_font_size = '0pt'  # turn off x-axis tick labels
p.yaxis.major_label_text_font_size = '0pt'  # turn off y-axis tick labels


mapper = CategoricalColorMapper(palette=["purple"], factors=['yes']) # will map "highlight" field yes values to purple

geo_source = GeoJSONDataSource(geojson=parcels.to_json()) #map will contain our parcel data
p.patches('xs', 'ys', fill_color = {'field' :'highlight', 'transform' : mapper}, fill_alpha=0.5, source=geo_source) # creates "patches" (ie shapes) based on our geo data

TOOLTIPS = [
    ('APN', '@APN'),
    ('Address', '@SitusAddress'),
    ('Buildings', '@Buildings'),
    ('Beds', '@Beds')
]

p.add_tools( HoverTool(tooltips=TOOLTIPS))

show(p)
