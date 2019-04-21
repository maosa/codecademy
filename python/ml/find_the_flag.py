##### DESICION TREES - FIND THE FLAG PROJECT


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

##### Row 0 to be used as the header
flags = pd.read_csv('~/Desktop/programming/codecademy/python/ml/flags.csv', header = 0)

print(flags.columns)
print('\n')
print(flags.head())
print('\n')

"""
Many columns contain numbers that don’t make a lot of sense. For example, the third row, which represents Algeria, has a Language of 8. What exactly does that mean?

Take a look at the Attribute Information for this dataset from UCI’s Machine Learning Repository:
http://archive.ics.uci.edu/ml/datasets/Flags

Using that information along with the printout of flags.head(), can you figure out what landmass Andora is on?
"""

labels = flags.Landmass

"""
We have our labels. Now we want to choose which columns will help our decision tree correctly classify those labels.

You could spend a lot of time playing with groups of columns to find the that work best. But for now, let’s see if we can predict where a country is based only on the colors of its flag.

Create a variable named data and set it equal to a DataFrame containing the following columns from flags:

"Red"
"Green"
"Blue"
"Gold"
"White"
"Black"
"Orange"
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

flags = pd.read_csv('flags.csv', header = 0)

print(flags.columns)
print('\n')
print(flags.head())
print('\n')

labels = flags.Landmass

data = flags[['Red', 'Green', 'Blue', 'Gold', 'White', 'Black', 'Orange']]

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)

tree = DecisionTreeClassifier(random_state = 1)

tree.fit(train_data, train_labels)

print(tree.score(test_data, test_labels))

##### Since there are six possible landmasses, if we randomly guessed, wed expect to be right about 16% of the time. Did our decision tree beat randomly guessing?

##### We now have a good baseline of how our model performs with these features. Lets see if we can prune the tree to make it better!

print('\nPruning tree...\n')

scores = []

for i in range(1, 21, 1):
    train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)
    tree = DecisionTreeClassifier(max_depth = i, random_state = 1)
    tree.fit(train_data, train_labels)
    scores.append(tree.score(test_data, test_labels))
    print(str(i) + ': ' + str(tree.score(test_data, test_labels)))

##### Rather than printing the score of each tree, lets graph it! We want the x-axis to show the depth of the tree and the y-axis to show the trees score. To do this, well need to create a list containing all of the scores. Before the for loop, create an empty list named scores. Inside the loop, instead of printing the trees score, use .append() to add it to scores.

plt.plot(range(1, 21, 1), scores)
plt.show()

##### Our graph doesnt really look like we would expect it to. It seems like the depth of the tree isnt really having an impact on its performance. This might be a good indication that were not using enough features. Lets add all the features that have to do with shapes to our data.

data = flags[["Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses", "Saltires", "Quarters", "Sunstars", "Crescent", "Triangle"]]

print('\nRebuilding tree with more features...\n')

scores = []

for i in range(1, 21, 1):
    train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)
    tree = DecisionTreeClassifier(max_depth = i, random_state = 1)
    tree.fit(train_data, train_labels)
    scores.append(tree.score(test_data, test_labels))
    print(str(i) + ': ' + str(tree.score(test_data, test_labels)))

plt.plot(range(1, 21, 1), scores)
plt.show()
