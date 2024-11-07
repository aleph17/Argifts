import numpy as np
import pandas as pd
from utils import orders, returns, products
from datetime import datetime
today = datetime.today().date()

# defining variable to be used
quantity_purchased = orders.groupby(['order_id', 'product_id'], as_index = False)['order_date'].count().rename(columns = {"order_date":"quantity_purchased"})
quantity_returned = returns.groupby(['order_id', 'product_id'], as_index = False)['return_date'].count().rename(columns = {'return_date': 'quantity_returned'})

# merging orders with quantity purchase and returned to have clear idea of dynamics
quantity_purchased = pd.merge(quantity_purchased, quantity_returned, on = ['order_id', 'product_id'], how = 'left')
orders = pd.merge(orders, quantity_purchased, on = ['order_id', 'product_id'], how = 'left')
orders = orders.drop_duplicates()

# updating dates
products['start_date'] = pd.to_datetime(products['start_date'])
products['end_date'].fillna(today, inplace= True)
products['end_date'] = pd.to_datetime(products['end_date'])
orders['order_date'] = pd.to_datetime(orders['order_date'])

# mergine products with orders with a condtion on dates
products.rename({'id':'product_id'}, axis = 1, inplace = True)
products = pd.merge(products, orders, on = 'product_id', how = 'left')
products = products[(products.order_date <= products.end_date) & (products.order_date >= products.start_date)]

# defining sales, margin, revenue
products['sales'] = products['sale_price'] * products['quantity_purchased']
products['margin'] = (products['sale_price'] - products['base_price']) * products['quantity_purchased']
products['quantity_returned'].fillna(0, inplace = True)
products['revenue'] = products['sale_price'] * (products['quantity_purchased'] - products['quantity_returned'])

# defining average_basket, net_profit, profit_ratio
average_basket = products.sales.sum()/products.shape[0]
products['net_profit'] = (products['sale_price'] - products['base_price']) * (products['quantity_purchased'] - products['quantity_returned'])
products['profit_ratio'] = products['net_profit']/products['revenue']
products['profit_ratio'].fillna(0, inplace= True)
checkpoint = products.revenue.sum()


