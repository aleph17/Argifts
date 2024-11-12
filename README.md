# Argifts
 This repository contains data anaylsis carried out for Argifts company. Python files contain all scripts written to analyze. Argifts - is an online retalier company based in Switzerlan.
 
 ### Data
  The data can be accessed throught this [link](HTTPS://TINYURL.COM/DATACHALLENGEFULLDATA) upon request. The creator of this repository is not in charge for the dataset.
  
 ### Fomrmat of the data
 orders.csv - Orders dataset indicating when the order was placed, the products purchased and the client who made the purchase
 
 products.csv - Detailed information about the products, including name, categories and price
 
 return.csv - Return dates and return reasons for different products in different orders
 
 clients.csv - Names, address, contact information and other details for each client
 
 rating.csv - Customer ratings (1-5) for products in each order
 

 ### Definitions used
 QUANTITY PURCHASED - number of rows per order and product in the orders dataset
 
 QUANTITY RETURNED - number of rows per order and product in the returns dataset
 
 SALES - sale_price * quantity_purchased
 
 MARGIN - (sale_price - base_price) * quantity_puchased
 
 REVENUE - sale_price * (quantity_purchased - quantity_returned)
 
 AVERAGE BASKET - SUM(sales) / NUMBER(orders)
 
 NET PROFIT - (sale_price - base_price) * (quantity_purchased - quantity_returned)
 
 PROFIT RATIO - net_profit / revenue
 
### Visualizations
 This [link](https://docs.google.com/presentation/d/1_c7IZb49wdvDYUheXbegSxknV_etB4VkabCfzpdcfRM/edit?usp=sharing) contains the slides given in the pitch for the CEO's of the company.


