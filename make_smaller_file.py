import geopandas as gpd

# parcels = gpd.read_file("https://opendata.arcgis.com/datasets/b55c25ae04fc47fc9c188dbbfcd51192_0.geojson")
parcels = gpd.read_file('Parcels.geojson')
# parcels = gpd.read_file('parcels_94608.geojson')
is_neighbor = parcels['SitusZip'] == "94608"
parcels_local = parcels[is_neighbor]
parcels_local.to_file("parcels_94608.geojson", driver='GeoJSON')