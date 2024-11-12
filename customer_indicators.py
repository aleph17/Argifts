import numpy as np
import pandas as pd
from utils import orders, returns, products, ratings, clients
from datetime import datetime
from definitions import products

#best customers by generated net_profit and order numbers
products_5 = products.groupby('client_id', as_index=False)['net_profit'].sum()
best_client_id = products_5.sort_values(by='net_profit').tail(1)['client_id'].iloc[0]
best_client_products = products[products['client_id']==best_client_id]

products_5_2 = products.groupby('client_id', as_index=False)['order_id'].nunique()
best_client_id_2 = products_5_2.sort_values(by='order_id').tail(1)['client_id'].iloc[0]
best_client_products_2 = products[products['client_id']==best_client_id_2]

# top and bottom 5 cantons by net_profit
products = pd.merge(products, clients[['client_id', 'address_canton']], on='client_id', how='left')
products_6 = products.groupby('address_canton', as_index=False)['net_profit'].sum()
top_cantons = products_6.sort_values(by='net_profit').tail(5)
bottom_cantons = products_6.sort_values(by='net_profit').head(5)

# canton with the highest net_profit and average_basket higher
best_canton = products_6.sort_values(by='net_profit').tail(1)['address_canton'].iloc[0]
average_basket = products.groupby('address_canton', as_index=False).agg(
    sales_sum=('sales', 'sum'),
    unique_orders=('order_id', 'nunique')
)
average_basket['average_basket'] = average_basket['sales_sum'] / average_basket['unique_orders']
best_canton_ab = average_basket[average_basket['address_canton']==best_canton]['average_basket'].iloc[0]