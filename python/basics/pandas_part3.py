###################
##### PANDAS PART 3

import pandas as pd
import numpy as np

sales = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/sales.csv')
print(sales)
targets = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/targets.csv')
print(targets)
men_women = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/men_women_sales.csv')
print(men_women)

##### Merge 2 dataframes
df = pd.merge(sales, targets)
print(df)

##### Merge multiple dataframes
all_data = sales.merge(targets).merge(men_women)
print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]
print(results)

orders = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/orders2.csv')
print(orders)
products = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/products.csv')
print(products)

##### Rename id column to product_id to avoid dataframes being wrongly merged
orders_products = pd.merge(orders, products.rename(columns={'id':'product_id'}))
print(orders_products)

"""
In the example below, the “left” table is the one that comes first (orders), and the “right” table is the one that comes second (customers).

This syntax says that we should match the customer_id from orders to the id in customers.

The new column names id_x and id_y aren’t very helpful for us when we read the table. We can help make them more useful by using the keyword suffixes. We can provide a list of suffixes to use instead of “_x” and “_y”.

pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id',
    suffixes=['_order', '_customer']
    )
"""

orders_products = pd.merge(
    orders,
    products,
    left_on='product_id',
    right_on='id',
    suffixes=['_orders', '_products']
    )
print(orders_products)

"""
When we merge two DataFrames whose rows don’t match perfectly, we lose the unmatched rows. This type of merge (where we only include matching rows) is called an inner merge.
For an outer merge use: pd.merge(df1, df2, how='outer')
"""

#####

"""
Left Merge
Suppose we want to identify which customers are missing phone information. We would want a list of all customers who have email, but don’t have phone.

We could get this by performing a Left Merge. A Left Merge includes all rows from the first (left) table, but only rows from the second (right) table that match the first table.

For this command, the order of the arguments matters. If the first DataFrame is company_a and we do a left join, we’ll only end up with rows that appear in company_a.

By listing company_a first, we get all customers from Company A, and only customers from Company B who are also customers of Company A.

Use the following command: pd.merge(df1, df2, how='left')

Right merge applies the exact opposite approach.
"""

#####

"""
When we need to reconstruct a single DataFrame from multiple smaller DataFrames, we can use the method pd.concat([df1, df2, df2, ...]). This method only works if all of the columns are the same in all of the DataFrames.

Use the following: pd.concat([df1, df2])
Note that a LIST of dataframes is passed into pd.concat()
"""

#########################################
##### Page Visits Funnel - Pandas Project

visits = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/visits.csv', parse_dates=[1])

cart = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/cart.csv', parse_dates=[1])

checkout = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/checkout.csv', parse_dates=[1])

purchase = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/purchase.csv', parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

##### Merge visits and cart

visits_cart = pd.merge(visits, cart, how='left')
print(visits_cart.head())
print(len(visits_cart)) # number of rows
print(len(visits_cart[visits_cart.cart_time.isnull()])) # number of null timestamps

pct_no_t = (len(visits_cart[visits_cart.cart_time.isnull()]) * 100)/len(visits_cart)

print("\n%d%% percent of users who visited the site did not place a t-shirt in their cart\n" % pct_no_t)

##### Merge cart and checkout

cart_checkout = pd.merge(cart, checkout, how='left')
print(cart_checkout.head())
print(len(cart_checkout)) # number of rows
print(len(cart_checkout[cart_checkout.checkout_time.isnull()]))

pct_no_checkout = (len(cart_checkout[cart_checkout.checkout_time.isnull()]) * 100)/len(cart_checkout)

print("\n%d%% percent of users who placed a t-shirt in their cart did not procede to checkout\n" % pct_no_checkout)

##### Merge all using left merges

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print(all_data.head)
print("\nall_data has "+ str(len(all_data)) + " rows\n")

##### Merge checkout and purchase

checkout_purchase = pd.merge(checkout, purchase, how='left')
print(checkout_purchase.head())
print(len(checkout_purchase)) # number of rows
print(len(checkout_purchase[checkout_purchase.purchase_time.isnull()]))

pct_no_purchase = (len(checkout_purchase[checkout_purchase.purchase_time.isnull()]) * 100)/len(checkout_purchase)

print("\n%d%% percent of users who proceded to checkout did not purchase a t-shirt\n" % pct_no_purchase)

#####

print("% of nulls in visit_time: " + str(len(all_data[all_data.visit_time.isnull()]) * 100 / len(all_data)))
print("% of nulls in cart_time: " + str(len(all_data[all_data.cart_time.isnull()]) * 100 / len(all_data)))
print("% of nulls in checkout_time: " + str(len(all_data[all_data.checkout_time.isnull()]) * 100 / len(all_data)))
print("% of nulls in purchase_time: " + str(len(all_data[all_data.purchase_time.isnull()]) * 100 / len(all_data)))

#####

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print("\nAverage time from initial visit to purchase: " + str(all_data.time_to_purchase.mean()) + "\n")
