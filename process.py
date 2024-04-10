import pandas as pd

# Read the CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Filter rows containing only Pink Morsels
df1 = df1[df1['product'] == 'pink morsel']
df2 = df2[df2['product'] == 'pink morsel']
df3 = df3[df3['product'] == 'pink morsel']

df1['price'] = df1['price'].str.replace('$', '').astype(float)
df2['price'] = df2['price'].str.replace('$', '').astype(float)
df3['price'] = df3['price'].str.replace('$', '').astype(float)

# Combine quantity and price into a single field 'sales'
df1['sales'] = df1['quantity'] * df1['price']
df2['sales'] = df2['quantity'] * df2['price']
df3['sales'] = df3['quantity'] * df3['price']

# Select required fields
df1 = df1[['sales', 'date', 'region']]
df2 = df2[['sales', 'date', 'region']]
df3 = df3[['sales', 'date', 'region']]

# Concatenate the dataframes
result = pd.concat([df1, df2, df3])

# Write the result to a new CSV file
result.to_csv("data/output.csv", index=False)
