import pandas as pd
import numpy as np

##################
##### INTRODUCTION

##### DataFrame 1

df1 = pd.DataFrame({
'Product ID': [1, 2, 3, 4],
'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
'Color': ['blue', 'green', 'red', 'black']
})

print(df1)

##### DataFrame 2

df2 = pd.DataFrame([
[1, 'San Diego', 100],
[2, 'Los Angeles', 120],
[3, 'San Francisco', 90],
[4, 'Sacramento', 115]], columns=['Store ID', 'Location', 'Number of Employees'])

print(df2)

##### DataFrame 3

df = pd.DataFrame([
['January', 100, 100, 23, 100],
['February', 51, 45, 145, 45],
['March', 81, 96, 65, 96],
['April', 80, 80, 54, 180],
['May', 51, 54, 54, 154],
['June', 112, 109, 79, 129]
], columns=['month', 'clinic_east', 'clinic_north', 'clinic_south', 'clinic_west'])

clinic_north = df.clinic_north # or use clinic_north = df['clinic_north']
print(type(clinic_north))

clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))

##### Select rows for April - June
april_may_june = df.iloc[3:6]
print(april_may_june)

##### Select January row
january = df[df.month == 'January']
print(january)

##### Select March or April rows
march_april = df[(df.month == "March") | (df.month == "April")]
print(march_april)

##### Using isin() function
january_february_march = df[df.month.isin(["January", "February", "March"])]
print(january_february_march)

##### Reset row indexes after using iloc()
df2 = df.loc[[1, 3, 5]]
print(df2)
df3 = df2.reset_index()
print(df2)
print(df3)
##### drop removes the old index column, inplace modifies the existing DataFrame
df2.reset_index(drop=True, inplace=True)
print(df2)

##########################
##### MODIFYING DATAFRAMES

df = pd.DataFrame([
[1, '3 inch screw', 0.5, 0.75],
[2, '2 inch nail', 0.10, 0.25],
[3, 'hammer', 3.00, 5.50],
[4, 'screwdriver', 2.50, 3.00]
], columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price'])

##### Add extra column
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
df['Is taxed?'] = 'Yes' # sets all rows to Yes
df['Revenue'] = df['Price'] - df['Cost to Manufacture']
print(df)

##### Column operations

df = pd.DataFrame([
['JOHN SMITH', 'john.smith@gmail.com'],
['Jane Doe', 'jdoe@yahoo.com'],
['joe schmo', 'joeschmo@hotmail.com']
], columns=['Name', 'Email'])

df['Lowercase Name'] = df.Name.apply(lambda x: x.lower())
print(df)

##### Review lambda functions
mylambda = lambda x: x[0] + x[len(x)-1] if (len(x) >= 2) else None
print(mylambda('Andreas'))

mylambda = lambda x: 'Welcome to BattleCity!' if x >= 13 else 'You must be over 13'
print(mylambda(12))
print(mylambda(14))

##### Apply lambda to a column (comment out as this will give an error)
# get_last_name = lambda x: x.split(' ')[1]
# df['last_name'] = df.name.apply(get_last_name)

##### Apply lambda to a row (comment out as this will give an error)
# total_earned = lambda row: (row['hourly_wage'] * 40) + (1.5 * row['hourly_wage'] * (row['hours_worked'] - 40)) if row['hours_worked'] >= 40 else row['hourly_wage'] * row['hours_worked']
# df['total_earned'] = df.apply(total_earned, axis=1)

##### Rename column names
df = pd.DataFrame({
'name': ['John', 'Jane', 'Sue', 'Fred'],
'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age'] # renames all columns
print(df)

df.rename(columns={
'name': 'First Name',
'age': 'Age'}, inplace=True) # allows one to rename only specific columns

################################
##### INVENTORY - PANDAS PROJECT

##### This project uses inventory.csv from CodeCademy

inventory = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/inventory.csv')

# print(inventory.head(10))

staten_island = inventory.iloc[:11]

product_request = staten_island.product_description

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

stock_lambda = lambda x: True if x > 0 else False

inventory['in_stock'] = inventory.quantity.apply(stock_lambda)

value_lambda = lambda row: row.quantity * row.price

inventory['total_value'] = inventory.apply(value_lambda, axis=1)

##### The following lambda function combines product_type and product_description into a single string
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

inventory.columns = map(str.upper, inventory.columns)
##### Can also use: inventory.columns = [x.lower() for x in inventory.columns]

print(inventory.head(10))
