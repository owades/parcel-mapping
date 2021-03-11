import geopandas as gpd
import pandas as pd

# parcels = gpd.read_file("https://opendata.arcgis.com/datasets/b55c25ae04fc47fc9c188dbbfcd51192_0.geojson")
parcels = gpd.read_file('parcels_94608.geojson')
is_neighbor = parcels['SitusZip'] == "94608" 
# is_neighbor = parcels['SitusCity'] == "OAKLAND" 
parcels = parcels[is_neighbor]

# filter out bad address data:
notblank = parcels['SitusStreetNumber'] != "" 
notth = ~parcels['SitusStreetNumber'].str.endswith('TH')
parcels = parcels[notblank]
parcels = parcels[notth]

# this is a bit ugly - only run with the below two lines if you are pulling from the API, since the existing file already has the owner column
# landlords = pd.read_csv('landlord_mapping.csv')
# parcels = parcels.merge(landlords, how='left',left_on='MailingAddress',right_on='Mailing Address')
parcels['Owner'] = parcels['Owner'].fillna("TBD")

# The idea here was to bundle addresses in the same building, but in hindsight I'm seeing that there are many owners for the same building.
# parcels['Units'] = parcels['Units'] + 1
# parcels.loc[(parcels.SitusAddress.str.startswith('3300 POWELL ST')),'SitusAddress']='3300 POWELL ST EMERYVILLE CA 94608'
# parcels['TotalUnits'] = parcels.groupby(['SitusAddress', 'MailingAddress'])['Units'].transform('sum')
# parcels = parcels.drop_duplicates(subset=['SitusAddress', 'MailingAddress'])

parcels.to_file("parcels_94608.geojson", driver='GeoJSON')
print("done!")
# parcels = parcels[parcels['SitusAddress'] == "  SKYLINE BLVD OAKLAND 94608"]
# print(parcels['SitusStreetNumber'])