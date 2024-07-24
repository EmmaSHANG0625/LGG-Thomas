import pandas as pd 

df = pd.read_json('final_dataset.json')
df.to_csv('final_dataset.csv')
df2 = pd.read_csv('final_dataset.csv')

#drop duplicates
df = df2.drop_duplicates()

#change column names
new_column_names = {

    'BathroomCount': 'bathroom_count',
    'BedroomCount': 'bedroom_count',
    'ConstructionYear': 'construction_year',
    'Country': 'country',
    'District': 'district',
    'Fireplace': 'fireplace',
    'FloodingZone': 'flooding_zone',
    'Furnished': 'furnished',
    'Garden': 'garden',
    'GardenArea': 'garden_area',
    'Kitchen': 'kitchen',
    'LivingArea': 'living_area',
    'Locality': 'locality',
    'MonthlyCharges': 'monthly_charges',
    'NumberOfFacades': 'number_of_facades',
    'PEB': 'PEB',
    'PostalCode': 'postal_code',
    'Price': 'price',
    'PropertyId': 'property_id',
    'Province': 'province',
    'Region': 'region',
    'RoomCount': 'room_count',
    'ShowerCount': 'shower_count',
    'StateOfBuilding': 'state_of_building',
    'SubtypeOfProperty': 'subtype_of_property',
    'SurfaceOfPlot': 'surface_of_plot',
    'SwimmingPool': 'swimming_pool',
    'Terrace': 'terrace',
    'ToiletCount': 'toilet_count',
    'TypeOfProperty': 'type_of_property',
    'TypeOfSale': 'type_of_sale'
}

df = df.rename(columns=new_column_names)
df.to_csv("Cleaned_data.csv", index = True)

#drop column 'price' for KNNimputer input null values
column_to_drop = 'price'
dropped_column = df[column_to_drop]
df = df.drop(columns=[column_to_drop])

#check and fill each column

#delete Fireplace and update
del df['fireplace']
del df['furnished']


#fill empty value of 'bathroom'
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=20)
df[['bathroom_count']] = imputer.fit_transform(df[['bathroom_count']])

df['bathroom_count'] = df['bathroom_count'].round().astype(int)

#check 'construction_year'
df = df.drop(df[df['construction_year'] > 2034].index)
#fill empty value of 'construction_year'
imputer = KNNImputer(n_neighbors=20)
df[['construction_year']] = imputer.fit_transform(df[['construction_year']])
df['construction_year'] = df['construction_year'].round().astype(int)

#Check 'garden'
df.loc[df['type_of_property'] == 2, 'garden'] = 0
condition = df['garden'].isnull() & (df['surface_of_plot'] != df['living_area'])
df.loc[condition, 'garden'] = 1
df['garden'].fillna(0, inplace=True)

#check 'living_area'
#delete wrong values
df = df.drop(df[df['living_area'] > 1000].index)
#fill empty value of 'living_area'
imputer = KNNImputer(n_neighbors=20)
df[['living_area']] = imputer.fit_transform(df[['living_area']])
df['living_area'] = df['living_area'].round().astype(int)


del df['monthly_charges']
del df['shower_count']
del df['locality']
del df['country']

#check 'number_of_facades'
df = df.drop(df[df['number_of_facades'] > 4].index)
#fill empty value of 'number_of_facades'
imputer = KNNImputer(n_neighbors=20)
df[['number_of_facades']] = imputer.fit_transform(df[['number_of_facades']])
df['number_of_facades'] = df['number_of_facades'].round().astype(int)

#fill empty value of 'district'
df.at[61035, 'district'] = 'Bruge'
df.at[61042, 'district'] = 'Bruge'

#fill empty value of 'room_count'
imputer = KNNImputer(n_neighbors=20)
df[['room_count']] = imputer.fit_transform(df[['room_count']])
df['room_count'] = df['room_count'].round().astype(int)

#check 'PEB'
#Clean the tricky PEB data
df = df.drop(df[df['PEB'].isin(["B_A", "A_A+", "F_C", "F_D", "G_C", "F_E", "E_D", "E_C", "G_F"])].index)
#Grade the PEB
PEB_grade = {
   'A++': 9,
 'A+': 8,
 'A': 7,
 'B': 6,
 'C': 5,
 'D': 4,
 'E': 3,
 'F': 2,
 'G': 1
}
df['PEB_grade'] =df['PEB'].map(PEB_grade)
#fill empty values of 'PEB'
imputer = KNNImputer(n_neighbors=20)
df[['PEB_grade']] = imputer.fit_transform(df[['PEB_grade']])
df['PEB_grade'] = df['PEB_grade'].round().astype(int)

#grade 'state_of_building'
Building_state_grade = {
    'GOOD': 4, 
'AS_NEW': 6,
'TO_RENOVATE': 2, 
'TO_BE_DONE_UP': 3,
'JUST_RENOVATED': 5,
'TO_RESTORE': 1
}
df['Building_state_grade'] =df['state_of_building'].map(Building_state_grade)
#fill empty value of 'building_state_grade'
imputer = KNNImputer(n_neighbors=20)
df[['Building_state_grade']] = imputer.fit_transform(df[['Building_state_grade']])

df['Building_state_grade'] = df['Building_state_grade'].round().astype(int)

#check 'surface_of_plot'
condition = df['surface_of_plot'].isnull() & (df['type_of_property'] == 2)
df.loc[condition, 'surface_of_plot'] = df['living_area']
#fill empty balue of 'building_state_grade'
imputer = KNNImputer(n_neighbors=20)
df[['surface_of_plot']] = imputer.fit_transform(df[['surface_of_plot']])
df['surface_of_plot'] = df['surface_of_plot'].round().astype(int)
df.loc[df['surface_of_plot'] < df['living_area'], 'surface_of_plot'] = df['living_area']

#check the 'swimming_pool'
df["swimming_pool"].fillna(0, inplace = True)

df[column_to_drop] = dropped_column
df.to_csv('Cleaned_data.csv', index = True)