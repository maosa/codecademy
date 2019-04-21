###################
##### PANDAS PART 2

import pandas as pd
import numpy as np

orders = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
pricey_shoes.rename(columns={'price':'max_price'}, inplace=True)
print(pricey_shoes)
print(type(pricey_shoes))

#####  Calculate 25th percentile for each shoe_color
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes)

##### Group by 2 columns
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
print(shoe_counts)

##### Pivot tables
##### df.pivot(columns='ColumnToPivot', index='ColumnToBeRows', values='ColumnToBeValues')
shoe_counts_pivot = shoe_counts.pivot(columns='shoe_color', index='shoe_type', values='id').reset_index(drop=True)
print(shoe_counts_pivot)

##################################
##### PAGE VISITS - PANDAS PROJECT

user_visits = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/page_visits.csv')

# print(user_visits.head())

click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)
print(type(click_source))

click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()
print(click_source_by_month)
print(type(click_source_by_month))

click_source_by_month_pivot = click_source_by_month.pivot(columns='month', index='utm_source', values='id').reset_index()
click_source_by_month_pivot.columns = map(str.upper, click_source_by_month_pivot.columns)
print(click_source_by_month_pivot)

################################
##### AD CLICKS - PANDAS PROJECT

ad_clicks = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/ad_clicks.csv')

# print(ad_clicks.head(5))

print(ad_clicks.groupby('utm_source').user_id.count().reset_index())

##### Can use this istead of the lambda function below: ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

timestamp_lambda = lambda x: True if not pd.isnull(x) else False

ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.apply(timestamp_lambda)

print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

# print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id')

# print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

##### The column experimental_group tells us whether the user was shown Ad A or Ad B

print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())

print(ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index())

exp_grp = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

exp_grp_pivot = exp_grp.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()

exp_grp_pivot['pct_clicked'] = exp_grp_pivot[True]/(exp_grp_pivot[True] + exp_grp_pivot[False])

print(exp_grp_pivot)

##### The Product Manager for the A/B test thinks that the clicks might have changed by day of the week

a_clicks = pd.DataFrame(ad_clicks[ad_clicks.experimental_group == "A"])

# print(a_clicks)

b_clicks = pd.DataFrame(ad_clicks[ad_clicks.experimental_group == "B"])

# print(b_clicks)

pct_a_clicks = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

pct_a_clicks = pct_a_clicks.pivot(columns='is_click', index='day', values='user_id')

pct_a_clicks['pct_clicked'] = pct_a_clicks[True]/(pct_a_clicks[True] + pct_a_clicks[False])

print(pct_a_clicks)

pct_b_clicks = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

pct_b_clicks = pct_b_clicks.pivot(columns='is_click', index='day', values='user_id')

pct_b_clicks['pct_clicked'] = pct_b_clicks[True]/(pct_b_clicks[True] + pct_b_clicks[False])

print(pct_b_clicks)
