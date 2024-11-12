# Argifts Data Analysis

This repository contains data analysis conducted for Argifts, an online retail company based in Switzerland. The Python scripts in this repository provide detailed analysis of Argifts’ sales, customer behaviors, and product performance.

### Data

The dataset is accessible upon request through this [link](https://tinyurl.com/datachallengefulldata). Please note that the repository creator does not manage dataset permissions.

### Data Format

- **orders.csv** - Contains order details, including order dates, products purchased, and customer IDs.
- **products.csv** - Contains detailed product information, including name, category, and price.
- **return.csv** - Tracks product returns, including return dates and reasons for each product and order.
- **clients.csv** - Contains customer information, including names, addresses, and contact details.
- **rating.csv** - Contains customer ratings (1-5) for products in each order.

### Key Metrics & Definitions

- **QUANTITY PURCHASED** - Number of items ordered per product per order.
- **QUANTITY RETURNED** - Number of items returned per product per order.
- **SALES** - `sale_price * quantity_purchased`
- **MARGIN** - `(sale_price - base_price) * quantity_purchased`
- **REVENUE** - `sale_price * (quantity_purchased - quantity_returned)`
- **AVERAGE BASKET** - `SUM(sales) / NUMBER(orders)`
- **NET PROFIT** - `(sale_price - base_price) * (quantity_purchased - quantity_returned)`
- **PROFIT RATIO** - `net_profit / revenue`

### Visualizations

The presentation slides for this analysis, given to the company’s executives, can be found at this [link](https://docs.google.com/presentation/d/1_c7IZb49wdvDYUheXbegSxknV_etB4VkabCfzpdcfRM/edit?usp=sharing).
