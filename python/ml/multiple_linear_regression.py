##### MULTIPLE LINEAR REGRESSION

import pandas as pd

# brooklyn = pd.read_csv('https://raw.githubusercontent.com/Codecademy/datasets/master/streeteasy/brooklyn.csv')
# queens = pd.read_csv('https://raw.githubusercontent.com/Codecademy/datasets/master/streeteasy/queens.csv')

df = pd.read_csv('https://raw.githubusercontent.com/Codecademy/datasets/master/streeteasy/manhattan.csv')

"""
As with most machine learning algorithms, we have to split our dataset into:

- Training set: the data used to fit the model
- Test set: the data partitioned away at the very start of the experiment (to provide an unbiased evaluation of the model)

Training Set vs. Testing Set
In general, putting 80% of your data in the training set and 20% of your data in the test set is a good place to start.

Suppose you have some values in x and some values in y:

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

Here are the parameters:

- train_size: the proportion of the dataset to include in the train split (between 0.0 and 1.0)
- test_size: the proportion of the dataset to include in the test split (between 0.0 and 1.0)
- random_state: the seed used by the random number generator [optional]
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

##### We have 14 features that we’re looking for for each apartment, and 1 label we’re looking for for each apartment. The .shape attribute for NumPy arrays returns the dimensions of the array. If array has n rows  m columns, then array.shape returns (n, m).
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

"""
The steps for multiple linear regression in scikit-learn are identical to the steps for simple linear regression. Just like simple linear regression, we need to import LinearRegression from the linear_model module:

from sklearn.linear_model import LinearRegression
Then, create a LinearRegression model, and then fit it to your x_train and y_train data:

mlr = LinearRegression()

mlr.fit(x_train, y_train)

# finds the coefficients and the intercept value
We can also use the .predict() function to pass in x-values. It returns the y-values that this plane would predict:

y_predicted = mlr.predict(x_text)

# takes values calculated by `.fit()` and the `x` values, plugs them into the multiple linear regression equation, and calculates the predicted y values.
"""

mlr = LinearRegression()
mlr.fit(x_train, y_train)
y_predict = mlr.predict(x_test)

sonny_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 0, 1, 0]]

predict = mlr.predict(sonny_apartment)

print("Predicted rent: $%.2f" % predict)

print(mlr.coef_)
print(mlr.intercept_)

import matplotlib.pyplot as plt

"""
Graphs can be created using Matplotlib’s pyplot module. Here is the code with inline comments explaining how to plot using Matplotlib’s .scatter():

# Create a scatter plot
plt.scatter(x, y, alpha=0.4)

# Create x-axis label and y-axis label
plt.xlabel("the x-axis label")
plt.ylabel("the y-axis label")

# Create a title
plt.title("title!")

# Show the plot
plt.show()
"""

plt.scatter(y_test, y_predict, alpha=0.4)
plt.title("Multiple linear regression for predicting house prices")
plt.xlabel("Actual rent prices ($)")
plt.ylabel("Predicted rent prices ($)")
plt.show()

#####

"""
In our Manhattan model, we used 14 variables, so there are 14 coefficients (print these using print(mlr.coef_)).

To see if there are any features that don’t affect price linearly, let’s graph the different features against rent.

In regression, the independent variables will either have a positive linear relationship to the dependent variable, a negative linear relationship, or no relationship. A negative linear relationship means that as X values increase, Y values will decrease. Similarly, a positive linear relationship means that as X values increase, Y values will also increase.

Graphically, when you see a downward trend, it means a negative linear relationship exists. When you find an upward trend, it indicates a positive linear relationship.
"""

plt.scatter(df[['size_sqft']], df[['rent']], alpha=0.4)
plt.show()

plt.scatter(df[['min_to_subway']], df[['rent']], alpha=0.4)
plt.show()

plt.scatter(df[['bedrooms']], df[['rent']], alpha=0.4)
plt.show()

#####

"""
When trying to evaluate the accuracy of our multiple linear regression model, one technique we can use is Residual Analysis.

The difference between the actual value y, and the predicted value ŷ is the residual e.

In the StreetEasy dataset, y is the actual rent and the ŷ is the predicted rent. The real y values should be pretty close to these predicted y values.

sklearn‘s linear_model.LinearRegression comes with a .score() method that returns the coefficient of determination R² of the prediction.

The coefficient R² is defined as:

1 - (u/v)

where u is the residual sum of squares:

((y - y_predict) ** 2).sum()

and v is the total sum of squares (TSS):

((y - y.mean()) ** 2).sum()​

The TSS tells you how much variation there is in the y variable.

>>>>> R² is the percentage variation in y explained by all the x variables together <<<<<

For example, say we are trying to predict rent based on the size_sqft and the bedrooms in the apartment and the R² for our model is 0.72 — that means that all the x variables (square feet and number of bedrooms) together explain 72% variation in y (rent).

Now let’s say we add another x variable, building’s age, to our model. By adding this third relevant x variable, the R² is expected to go up. Let say the new R² is 0.95. This means that square feet, number of bedrooms and age of the building together explain 95% of the variation in the rent.

The best possible R² is 1.00 (and it can be negative because the model can be arbitrarily worse). Usually, a R² of 0.70 is considered good.

Now let’s rebuild the model using the new features as well as evaluate the new model to see if we improved!

For Manhattan, the scores returned:

Train score: 0.772546055982
Test score:  0.805037197536

>>>>> REVIEW

Multiple Linear Regression uses two or more variables to make predictions about another variable:
y = b + m_{1}x_{1} + m_{2}x_{2} + ... + m_{n}x_{n}
​
- Multiple linear regression uses a set of independent variables and a dependent variable. It uses these variables to learn how to find optimal parameters. It takes a labeled dataset and learns from it. Once we confirm that it’s learned correctly, we can then use it to make predictions by plugging in new x values.
- We can use scikit-learn’s LinearRegression() to perform multiple linear regression.
- Residual Analysis is used to evaluate the regression model’s accuracy. In other words, it’s used to see if the model has learned the coefficients correctly.
- Scikit-learn’s linear_model.LinearRegression comes with a .score() method that returns the coefficient of determination R² of the prediction. The best score is 1.0.
"""
