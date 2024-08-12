import pandas as pd
import numpy as np

df = pd.read_csv('Cleaned_data.csv')
# Calculate the quartiles and the interquartile range (IQR)
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

# Define the outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
df = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]

#drop the columns no need
del df['Url']
del df['flooding_zone']
del df['garden_area']
del df['kitchen']
del df['postal_code']
del df['region']
del df['PEB']
del df['state_of_building']
del df['subtype_of_property']
del df['terrace']
del df['toilet_count']
del df['type_of_sale']

filtered_df = df[df['type_of_property'] == 2]
facades_distribution_appartment = filtered_df['number_of_facades'].value_counts()
print(facades_distribution_appartment)

from sklearn.preprocessing import OneHotEncoder
#convert 'type_of_property'] into str
df.loc[df['type_of_property'] == 1, 'type_of_property'] = 'house'
df.loc[df['type_of_property'] == 2, 'type_of_property'] = 'appartment'
df.to_csv("Data for Machine Learning.csv", index = True)

#creat OneHot vector for 'type_of_property'
df_type = df[['type_of_property']]
encoder_type = OneHotEncoder()
df_type_1hot = encoder_type.fit_transform(df_type)
df_type_1hot_array = df_type_1hot.toarray()# 获取独热编码后的列名
encoded_columns = encoder_type.get_feature_names_out(['type_of_property'])

df_type_1hot_df = pd.DataFrame(df_type_1hot_array, columns=encoded_columns)
df = pd.concat([df, df_type_1hot_df], axis=1)


#creat OneHot vector for 'distict'
df_district = df[['district']]
encoder_district = OneHotEncoder()
df_district_1hot = encoder_district.fit_transform(df_district)
df_district_1hot_array = df_district_1hot.toarray()

encoded_columns = encoder_district.get_feature_names_out(['district'])
df_district_1hot_df = pd.DataFrame(df_district_1hot_array, columns=encoded_columns)
df = pd.concat([df, df_district_1hot_df], axis=1)

del df['Unnamed: 0.1']
del df['Unnamed: 0']
del df['district']
del df['district_nan']

del df['property_id']
del df['province']
del df['type_of_property']

df.to_csv("Data for Machine Learning.csv", index = True)