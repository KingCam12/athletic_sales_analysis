# Import necessary libraries
import pandas as pd

# Load the data into DataFrames

df_2020 = pd.read_csv('athletic_sales_2020.csv')
df_2021 = pd.read_csv('athletic_sales_2021.csv')

# Check columns for consistency
print(df_2020.columns)
print(df_2021.columns)

# Combine the two DataFrames
df_combined = pd.concat([df_2020, df_2021], ignore_index=True)

# Check for null values
print(df_combined.isnull().sum())

# Convert invoice_date to datetime
df_combined['invoice_date'] = pd.to_datetime(df_combined['invoice_date'])

# Verify the changes
print(df_combined.dtypes)

# Group by region, state, and city to find which sold the most products
grouped_products = df_combined.groupby(['region', 'state', 'city']).agg({'quantity_ordered': 'sum'}).reset_index()

# Rename the aggregated column
grouped_products = grouped_products.rename(columns={'quantity_ordered': 'total_quantity'})

# Sort to get the top 5 regions
top_regions = grouped_products.sort_values(by='total_quantity', ascending=False).head(5)
print(top_regions)


# Group by region, state, and city to find the regions with the highest sales
grouped_sales = df_combined.groupby(['region', 'state', 'city']).agg({'total_sales': 'sum'}).reset_index()

# Rename the aggregated column
grouped_sales = grouped_sales.rename(columns={'total_sales': 'total_revenue'})

# Sort to get the top 5 regions
top_sales_regions = grouped_sales.sort_values(by='total_revenue', ascending=False).head(5)
print(top_sales_regions)

# Group by retailer, region, state, and city to find the retailer with the most sales
grouped_retailers = df_combined.groupby(['retailer', 'region', 'state', 'city']).agg({'total_sales': 'sum'}).reset_index()

# Rename the aggregated column
grouped_retailers = grouped_retailers.rename(columns={'total_sales': 'total_revenue'})

# Sort to get the top 5 retailers
top_retailers = grouped_retailers.sort_values(by='total_revenue', ascending=False).head(5)
print(top_retailers)

# Filter the DataFrame for women's athletic footwear
womens_footwear_df = df_combined[df_combined['product'].str.contains('Women\'s Athletic Footwear')]

# Group by retailer, region, state, and city to find which retailer sold the most
grouped_womens_footwear = womens_footwear_df.groupby(['retailer', 'region', 'state', 'city']).agg({'total_sales': 'sum'}).reset_index()

# Rename the aggregated column
grouped_womens_footwear = grouped_womens_footwear.rename(columns={'total_sales': 'total_revenue'})

# Sort to get the top 5 retailers
top_womens_retailers = grouped_womens_footwear.sort_values(by='total_revenue', ascending=False).head(5)
print(top_womens_retailers)

# Pivot table for invoice_date and total_sales for women's footwear
pivot_womens_footwear = womens_footwear_df.pivot_table(index='invoice_date', values='total_sales', aggfunc='sum')

# Resample the pivot table to daily bins
daily_sales = pivot_womens_footwear.resample('D').sum()

# Sort the results to find the top 10 days
top_10_days = daily_sales.sort_values(by='total_sales', ascending=False).head(10)
print(top_10_days)

# Resample the pivot table to weekly bins
weekly_sales = pivot_womens_footwear.resample('W').sum()

# Sort the results to find the top 10 weeks
top_10_weeks = weekly_sales.sort_values(by='total_sales', ascending=False).head(10)
print(top_10_weeks)

#code by cameron burgess
