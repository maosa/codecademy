##### RANDOM FORESTS

"""
A random forest is an ensemble machine learning technique — a random forest contains many decision trees that all work together to classify new points. When a random forest is asked to classify a new point, the random forest gives that point to each of the decision trees. Each of those trees reports their classification and the random forest returns the most popular classification. It’s like every tree gets a vote, and the most popular classification wins.

Some of the trees in the random forest may be overfit, but by making the prediction based on a large number of trees, overfitting will have less of an impact.

>>>>> Bagging

You might be wondering how the trees in the random forest get created. After all, right now, our algorithm for creating a decision tree is deterministic — given a training set, the same tree will be made every time.

Random forests create different trees using a process known as bagging. Every time a decision tree is made, it is created using a different subset of the points in the training set. For example, if our training set had 1000 rows in it, we could make a decision tree by picking 100 of those rows at random to build the tree. This way, every tree is different, but all trees will still be created from a portion of the training data.

One thing to note is that when we’re randomly selecting these 100 rows, we’re doing so with replacement. Picture putting all 100 rows in a bag and reaching in and grabbing one row at random. After writing down what row we picked, we put that row back in our bag.

This means that when we’re picking our 100 random rows, we could pick the same row more than once. In fact, it’s very unlikely, but all 100 randomly picked rows could all be the same row!

Because we’re picking these rows with replacement, there’s no need to shrink our bagged training set from 1000 rows to 100. We can pick 1000 rows at random, and because we can get the same row more than once, we’ll still end up with a unique data set.

Let’s implement bagging! We’ll be using the data set of cars that we used in our decision tree lesson.

>>>>> Bagging Features

We’re now making trees based on different random subsets of our initial dataset. But we can continue to add variety to the ways our trees are created by changing the features that we use.

Recall that for our car data set, the original features were the following:

- The price of the car
- The cost of maintenance
- The number of doors
- The number of people the car can hold
- The size of the trunk
- The safety rating

Right now when we create a decision tree, we look at every one of those features and choose to split the data based on the feature that produces the most information gain. We could change how the tree is created by only allowing a subset of those features to be considered at each split.

For example, when finding which feature to split the data on the first time, we might randomly choose to only consider the price of the car, the number of doors, and the safety rating.

After splitting the data on the best feature from that subset, we’ll likely want to split again. For this next split, we’ll randomly select three features again to consider. This time those features might be the cost of maintenance, the number of doors, and the size of the trunk. We’ll continue this process until the tree is complete.

One question to consider is how to choose the number of features to randomly select. Why did we choose 3 in this example? A good rule of thumb is to randomly select the square root of the total number of features. Our car dataset doesn’t have a lot of features, so in this example, it’s difficult to follow this rule. But if we had a dataset with 25 features, we’d want to randomly select 5 features to consider at every split point.

>>>>> Classify

Now that we can make different decision trees, it’s time to plant a whole forest! Let’s say we make different 8 trees using bagging and feature bagging. We can now take a new unlabeled point, give that point to each tree in the forest, and count the number of times different labels are predicted.

The trees give us their votes and the label that is predicted most often will be our final classification! For example, if we gave our random forest of 8 trees a new data point, we might get the following results:

["vgood", "vgood", "good", "vgood", "acc", "vgood", "good", "vgood"]

Since the most commonly predicted classification was "vgood", this would be the random forest’s final classification.

>>>>> Test Set

We’re now able to create a random forest, but how accurate is it compared to a single decision tree? To answer this question we’ve split our data into a training set and test set. By building our models using the training set and testing on every data point in the test set, we can calculate the accuracy of both a single decision tree and a random forest.

>>>>> Random Forest in Scikit-learn

You now have the ability to make a random forest using your own decision trees. However, scikit-learn has a RandomForestClassifier class that will do all of this work for you! RandomForestClassifier is in the sklearn.ensemble module.

RandomForestClassifier works almost identically to DecisionTreeClassifier — the .fit(), .predict(), and .score() methods work in the exact same way.

When creating a RandomForestClassifier, you can choose how many trees to include in the random forest by using the n_estimators parameter like this:

classifier = RandomForestClassifier(n_estimators = 100)

We now have a very powerful machine learning model that is fairly resistant to overfitting!

>>>>> Review

Nice work! Here are some of the major takeaways about random forests:

- A random forest is an ensemble machine learning model. It makes a classification by aggregating the classifications of many decision trees.
- Random forests are used to avoid overfitting. By aggregating the classification of multiple trees, having overfitted trees in a random forest is less impactful.
- Every decision tree in a random forest is created by using a different subset of data points from the training set. Those data points are chosen at random with replacement, which means a single data point can be chosen more than once. This process is known as bagging.
- When creating a tree in a random forest, a randomly selected subset of features are considered as candidates for the best splitting feature. If your dataset has n features, it is common practice to randomly select the square root of n features.
"""

##### In this project, we will be using a dataset containing census
##### information from UCI’s Machine Learning Repository.
##### By using this census data with a random forest,
##### we will try to predict whether or not a person makes more than $50,000.

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

"""
There’s a small problem with our data that is a little hard to catch — every string has an extra space at the start. For example, the first row’s native-country is " United-States", but we want it to be "United-States". This is happening because in income.csv there are spaces after the commas. To fix this, we can add the parameter delimiter = ", " to our read_csv() function.
"""

income_data = pd.read_csv('~/Desktop/programming/codecademy/python/ml/income.csv', header = 0, delimiter = ', ')

print(income_data.columns)
print(income_data.head(5))
print(income_data.iloc[0])

"""
Now that we have our data imported into a DataFrame, we can begin putting it in a format that our Random Forest can work with. To do this, we need to separate the labels from the rest of the data.

For this project, the labels are in the column called "income". We want to grab only this column.
"""

labels = income_data.income

"""
We’ll also want to pick which columns to use when trying to predict income. For now, let’s select "age", "capital-gain", "capital-loss", "hours-per-week", and "sex".
"""

data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week", "sex"]]

"""
There seems to be a problem with using the column "sex" when training the random forest.

In that column, there are values like "Male" and "Female". Random forests can’t use columns that contain Strings — they have to be continuous values like integers or floats. We’ll solve this problem soon, but for now, let’s remove the "sex" column when creating data.
"""

data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week"]]

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)
forest = RandomForestClassifier(random_state = 1)
forest.fit(train_data, train_labels)

print('\nScore 1: ' + str(forest.score(test_data, test_labels)))

"""
Now that we know the random forest works, let’s go back and try to add the "sex" column.

Recall that the problem was that this column contained strings. If we transformed those strings into integers, we could use this data!
"""

income_data['sex-int'] = income_data["sex"].apply(lambda row: 0 if row == "Male" else 1)

data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week", "sex-int"]]

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)
forest = RandomForestClassifier(random_state = 1)
forest.fit(train_data, train_labels)
print('\nScore 2: ' + str(forest.score(test_data, test_labels)))

"""
There are a couple of other columns that use strings that might be useful to use. Let’s try transforming the values in the "native-country" column.

We should first take a look at the different values that exist in the column. Print income_data["native-country"].value_counts()
"""

print(income_data["native-country"].value_counts())

income_data['country-int'] = income_data['native-country'].apply(lambda row: 0 if row == "United-States" else 1)

data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week", "sex-int", "country-int"]]

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)
forest = RandomForestClassifier(random_state = 1)
forest.fit(train_data, train_labels)
print('\nScore 3: ' + str(forest.score(test_data, test_labels)))

"""
After calling .fit() on the forest, print:

forest.feature_importances_

This will show you a list of numbers where each number corresponds to the relevance of a column from the training data. Which features tend to be more relevant?
"""
