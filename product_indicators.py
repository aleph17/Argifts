import numpy as np
import pandas as pd
from utils import orders, returns, products, ratings
from datetime import datetime
from definitions import products


# top& worst 3 products in terms of revenue
product_revenue = products.groupby(['product_id', 'name'], as_index= False)['revenue'].sum()
product_revenue = product_revenue.sort_values('revenue')


# the category with the highest net_profit and corresponding net_profit and revenues
product_2 = products.groupby(['category_1'], as_index = False)[['net_profit', 'revenue']].sum()
best_category = product_2.sort_values(by='net_profit').tail(1)['category_1'].values[0]
product_3 = products[products['category_1']== best_category]


# within the category with the highest net_profit the product that is top
product_3 = products[products['category_1']== best_category]
product_3_revenue = product_3.groupby(['product_id', 'name'], as_index = False)['net_profit'].sum()
product_3_revenue = product_3_revenue.sort_values('net_profit')


# average rating of products and the average of all averages. the highest deviation from mean
products = pd.merge(products, ratings, on = ['order_id', 'product_id'], how = 'left')
product_4 = products[products['category_1']==best_category]
product_4 = product_4[product_4['rating'].notna()]
product_4_mean = product_4.groupby(['product_id', 'name'], as_index = False)['rating'].mean()
m = product_4_mean['rating'].mean()
