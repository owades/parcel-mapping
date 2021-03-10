import geopandas as gpd

# full Alameda county data from API:
# parcels = gpd.read_file("https://opendata.arcgis.com/datasets/b55c25ae04fc47fc9c188dbbfcd51192_0.geojson")

# geojson for a small zip code - much faster than using full county data above
# parcels = gpd.read_file('parcels_oakland.geojson')
parcels = gpd.read_file('parcels_94608.geojson')


#convert count output to dataframe!
landlord_counts = parcels['MailingAddress'].value_counts().rename_axis('Property Owner Address').reset_index(name='Number of Properties')
is_major_owner = landlord_counts['Number of Properties'] >= 4
landlord_counts = landlord_counts[is_major_owner]
landlord_counts.to_csv('landlords_94608.csv',index=False,header=True)

