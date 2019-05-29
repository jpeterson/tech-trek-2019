from arcgis.gis import GIS

# Connect to my GIS
gis = GIS(profile='joshdbs')
print('\n')
print('User:')
print(gis.users.me)
print('\n')

# Search my GIS
result = gis.content.search('DC')
print('Search Result:')
print(result)
