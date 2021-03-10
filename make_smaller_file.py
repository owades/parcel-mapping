import geopandas as gpd


# parcels = gpd.read_file("https://opendata.arcgis.com/datasets/b55c25ae04fc47fc9c188dbbfcd51192_0.geojson")
parcels = gpd.read_file('parcels_94608.geojson')
# is_neighbor = parcels['SitusZip'] == "94608" 
# is_neighbor = parcels['SitusCity'] == "OAKLAND" 
# parcels = parcels[is_neighbor]
notblank = parcels['SitusStreetNumber'] != "" 
parcels = parcels[notblank]

# The idea here was to bundle addresses in the same building, but in hindsight I'm seeing that there are many owners for the same building.
# parcels['Units'] = parcels['Units'] + 1
# parcels.loc[(parcels.SitusAddress.str.startswith('3300 POWELL ST')),'SitusAddress']='3300 POWELL ST EMERYVILLE CA 94608'
# parcels['TotalUnits'] = parcels.groupby(['SitusAddress', 'MailingAddress'])['Units'].transform('sum')
# parcels = parcels.drop_duplicates(subset=['SitusAddress', 'MailingAddress'])

parcels.to_file("parcels_94608.geojson", driver='GeoJSON')
print("done!")
# parcels = parcels[parcels['SitusAddress'] == "  SKYLINE BLVD OAKLAND 94608"]
# print(parcels['SitusStreetNumber'])