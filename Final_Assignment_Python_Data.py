import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from matplotlib.pyplot import title, legend

url = "https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv"
df = pd.read_csv(url)
print(df.head())
print(df.isna().sum())
df.dropna(inplace=True)
df_filtered = df[(df['date'] >= '2016-01-01') & (df['date'] <= '2019-12-31')]
popular_items = df_filtered.groupby(['zip_code', 'item_number'])['bottles_sold'].sum()
popular_items = popular_items.reset_index().sort_values(['zip_code', 'bottles_sold'], ascending=[True, False])
print(popular_items.head(10))
store_sales = df_filtered.groupby('store_number')['sale_dollars'].sum()
total_sales = store_sales.sum()
store_sales_percentage = (store_sales / total_sales) * 100
print(store_sales_percentage.sort_values(ascending=False).head(10))
top_products = popular_items.groupby('item_number')['bottles_sold'].sum().nlargest(10)
plt.figure(figsize=(10, 5))
top_products.plot(kind='bar', color='b')
plt.title('top 10 Best-Selling Products')
plt.xlabel('Product ID')
plt.ylabel('Bottles Sold')
plt.show()
store_sales = df.groupby('store_name')['sale_dollars'].sum()
total_sales = store_sales.sum()
store_sales_percentage = (store_sales / total_sales) * 100
sorted_sales = store_sales_percentage.sort_values(ascending=True)
top_stores = sorted_sales.tail(20)
plt.figure(figsize=(12, 8))
sns.barplot(y=top_stores.index, x=top_stores.values, hue=top_stores.index, palette="coolwarm", legend=False)
plt.title("Top 20 Stores by Sales Percentage", fontsize=14)
plt.xlabel("Percentage of Salers", fontsize=12)
plt.ylabel("Store Name", fontsize=12)
plt.yticks(fontsize=10)
plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(df['zip_code'], df['bottles_sold'], alpha=0.5, c=df['bottles_sold'], cmap='viridis')
plt.colorbar(label='Bottle Sold')
plt.xlabel("Zipcode")
plt.ylabel("Bottles Sold")
plt.title("Bottles Sold per Zipcode")
plt.show()
store_sales = df.groupby('store_name')['sale_dollars'].sum()
top_stores = store_sales.nlargest(20)
fig = px.bar(top_stores.reset_index(), y="store_name", x="sale_dollars", color="sale_dollars", text=top_stores.round(2), color_continuous_scale="viridis")
fig.update_layout(title="Top 20 Stores by Sales", xaxis_title="Sales in Dollars", yaxis_title="Store Name", coloraxis_colorbar_title="Total Sales")
fig.show()
store_sales = df.groupby('store_name')['sale_dollars'].sum()
total_sales = store_sales.sum()
store_sales_percentage = (store_sales / total_sales) * 100
sorted_sales = store_sales_percentage.sort_values(ascending=True)
top_stores = sorted_sales.tail(20)
plt.figure(figsize=(12, 6))
sns.barplot(y=top_stores.index, x=top_stores.values, hue=top_stores.index, palette="tab10", legend=False)
plt.title("Percentage of Sales per Store")
plt.xlabel("Percentage of Sales")
plt.ylabel("Store Name")
plt.show()
store_sales = df.groupby('store_name')['sale_dollars'].sum()
total_sales = store_sales.sum()
store_sales_percentage = (store_sales / total_sales) * 100
sorted_sales = store_sales_percentage.sort_values(ascending=True)
top_stores = sorted_sales.tail(20)
fig = px.bar(top_stores.reset_index(), x="sale_dollars", y="store_name", color="sale_dollars", text=top_stores.round(2), orientation="h", color_continuous_scale="plasma", title="% Sales by Store")
fig.update_layout(xaxis_title="% Sales", yaxis_title="Store Name", coloraxis_colorbar_title="Sale dollars")
fig.show()
bottles_sold_per_zipcode = df.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
fig = px.scatter(bottles_sold_per_zipcode, x="zip_code", y="bottles_sold", color="item_number", hover_data=["item_number", "bottles_sold"], color_continuous_scale="plasma")
fig.update_layout(title="Bottles Sold per Zipcode", xaxis_title="Zipcode", yaxis_title="Sum of Bottles Sold", legend_title="Item Number", coloraxis_colorbar_title="Bottles Sold")
fig.show()