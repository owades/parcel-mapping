import geopandas as gpd

# parcels = gpd.read_file("https://opendata.arcgis.com/datasets/b55c25ae04fc47fc9c188dbbfcd51192_0.geojson")
# parcels = gpd.read_file('Parcels.geojson')
parcels = gpd.read_file('parcels_94608.geojson')
is_neighbor = parcels['SitusZip'] == "94608"
parcels = parcels[is_neighbor]
is_owned = parcels['MailingAddress'] == "1333 PARK AVE EMERYVILLE CA 94608"
parcels = parcels[is_owned]
parcels.to_file("parcels_small.geojson", driver='GeoJSON')