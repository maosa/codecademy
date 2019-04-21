##### HONEY PRODUCTION PREDICTION

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())

prod_per_year = df.groupby('year').totalprod.mean().reset_index()

print(prod_per_year.head())

X = prod_per_year.year
##### After creating X, we will need to reshape it to get it into the right format
X = X.values.reshape(-1, 1)

y = prod_per_year.totalprod

regr = linear_model.LinearRegression()

regr.fit(X, y)

print('Coefficients: ' + str(regr.coef_))
print('Intercept: ' + str(regr.intercept_))

y_predict = regr.predict(X)

plt.scatter(X, y, alpha = 0.5)
plt.plot(X, y_predict)
plt.show()

##### So, it looks like the production of honey has been in decline, according to this linear model. Lets predict what the year 2050 may look like in terms of honey production. Our known dataset stops at the year 2013, so lets create a NumPy array called X_future that is the range from 2013 to 2050.

X_future = np.array(range(2013, 2051))
##### Reshape it for scikit-learn. You can think of reshape() as rotating this array. Rather than one big row of numbers, X_future is now a big column of numbers  theres one number in each row.
X_future = X_future.reshape(-1, 1)

future_predict = regr.predict(X_future)

plt.scatter(X, y, alpha = 0.5)
plt.plot(X_future, future_predict)
plt.show()
