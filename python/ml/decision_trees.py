##### DECISION TREES

"""
>>>>> Decision Trees

Decision trees are machine learning models that try to find patterns in the features of data points. Take a look at the tree on this page. This tree tries to predict whether a student will get an A on their next test.

By asking questions like “What is the student’s average grade in the class” the decision tree tries to get a better understanding of their chances on the next test.

In order to make a classification, this classifier needs a data point with four features:

The student’s average grade in the class.
The number of hours the student plans on studying for the test.
The number of hours the student plans on sleeping the night before the test.
Whether or not the student plans on cheating.

For example, let’s say that somebody has a “B” average in the class, studied for more than 3 hours, slept less than 5 hours before the test, and doesn’t plan to cheat. If we start at the top of the tree and take the correct path based on that data, we’ll arrive at a leaf node that predicts the person will not get an A on the next test.

>>>>> Making Decision Trees

If we’re given this magic tree, it seems relatively easy to make classifications. But how do these trees get created in the first place? Decision trees are supervised machine learning models, which means that they’re created from a training set of labeled data. Creating the tree is where the learning in machine learning happens.

We begin with every point in the training set at the top of the tree. These training points have labels — the red points represent students that didn’t get an A on a test and the green points represent students that did get an A on a test .

We then decide to split the data into smaller groups based on a feature. For example, that feature could be something like their average grade in the class. Students with an A average would go into one set, students with a B average would go into another subset, and so on.

Once we have these subsets, we repeat the process — we split the data in each subset again on a different feature.

Eventually, we reach a point where we decide to stop splitting the data into smaller groups. We’ve reached a leaf of the tree. We can now count up the labels of the data in that leaf. If an unlabeled point reaches that leaf, it will be classified as the majority label.

We can now make a tree, but how did we know which features to split the data set with? After all, if we started by splitting the data based on the number of hours they slept the night before the test, we’d end up with a very different tree that would produce very different results. How do we know which tree is best?

>>>>> Gini impurity

This idea can be quantified by calculating the Gini impurity of a set of data points. To find the Gini impurity, start at 1 and subtract the squared percentage of each label in the set. For example, if a data set had three items of class A and one item of class B, the Gini impurity of the set would be:

1 - (3/4)^2 - (1/4)^2 = 0.375

If a data set has only one class, you’d end up with a Gini impurity of 0. The lower the impurity, the better the decision tree!

>>>>> Information Gain

We know that we want to end up with leaves with a low Gini Impurity, but we still need to figure out which features to split on in order to achieve this. For example, is it better if we split our dataset of students based on how much sleep they got or how much time they spent studying?

To answer this question, we can calculate the information gain of splitting the data on a certain feature. Information gain measures difference in the impurity of the data before and after the split. For example, let’s say you had a dataset with an impurity of 0.5. After splitting the data based on a feature, you end up with three groups with impurities 0, 0.375, and 0. The information gain of splitting the data in that way is 0.5 - 0 - 0.375 - 0 = 0.125.

Not bad! By splitting the data in that way, we’ve gained some information about how the data is structured — the datasets after the split are purer than they were before the split. The higher the information gain the better — if information gain is 0, then splitting the data on that feature was useless! Unfortunately, right now it’s possible for information gain to be negative. In the next exercise, we’ll calculate weighted information gain to fix that problem.

>>>>> Weighted Information Gain

We’re not quite done calculating the information gain of a set of objects. The sizes of the subset that get created after the split are important too! For example, the image below shows two sets with the same impurity. Which set would you rather have in your decision tree?

Both of these sets are perfectly pure, but the purity of the second set is much more meaningful. Because there are so many items in the second set, we can be confident that whatever we did to produce this set wasn’t an accident.

It might be helpful to think about the inverse as well. Consider these two sets with the same impurity:

Both of these sets are completely impure. However, that impurity is much more meaningful in the set with more instances. We know that we are going to have to do a lot more work in order to completely separate the two classes. Meanwhile, the impurity of the set with two items isn’t as important. We know that we’ll only need to split the set one more time in order to make two pure sets.

Let’s modify the formula for information gain to reflect the fact that the size of the set is relevant. Instead of simply subtracting the impurity of each set, we’ll subtract the weighted impurity of each of the split sets. If the data before the split contained 20 items and one of the resulting splits contained 2 items, then the weighted impurity of that subset would be 2/20 * impurity. We’re lowering the importance of the impurity of sets with few elements.

>>>>> Recursive Tree Building

Now that we can find the best feature to split the dataset, we can repeat this process again and again to create the full tree. This is a recursive algorithm! We start with every data point from the training set, find the best feature to split the data, split the data based on that feature, and then recursively repeat the process again on each subset that was created from the split.

We’ll stop the recursion when we can no longer find a feature that results in any information gain. In other words, we want to create a leaf of the tree when we can’t find a way to split the data that makes purer subsets.

The leaf should keep track of the classes of the data points from the training set that ended up in the leaf. In our implementation, we’ll use a Counter object to keep track of the counts of labels.

We’ll use these counts to make predictions about new data that we give the tree.

#####

We’ve given you the function find_best_split() that takes a set of data points and a set of labels.

The function returns the index of the feature that causes the best split and the information gain caused by that split.

Let’s create a function called build_tree() that takes data and labels as parameters.

Move your call of find_best_split() inside this function, but change the parameters from car_data and car_labels to data and labels.

If best_gain is 0, return a Counter object of labels. We’ve reached the base case — there’s no way to gain any more information so we want to create a leaf.

After the if statement, we want to start working on the recursive case.

In the recursive case, we want to split the data into subsets using the best feature, and then recursively call the build_tree() function on those subsets to create subtrees. Finally, we want to return a list of all those subtrees.

Let’s begin by splitting the data. You can do this by using the split() function which takes three parameters — the data and labels that you want to split and the index of the feature you want to split on.

Store the result of the split() function in two variables named data_subsets and label_subsets.

For now, return data_subsets at the bottom of your function.

Before that final return statement, create an empty list named branches. This list will store all of the subtrees we’re about to make from our recursive calls.

We now want to loop through all of the subsets of data and labels. Inside the for loop, call build_tree using data_subsets[i] and label_subsets[i] as parameters and append the result to branches.

Finally outside the for loop, return branches instead of data_subsets.
"""

from collections import Counter

##### Essential functions

def split(dataset, labels, column):
    data_subsets = []
    label_subsets = []
    counts = list(set([data[column] for data in dataset]))
    counts.sort()
    for k in counts:
        new_data_subset = []
        new_label_subset = []
        for i in range(len(dataset)):
            if dataset[i][column] == k:
                new_data_subset.append(dataset[i])
                new_label_subset.append(labels[i])
        data_subsets.append(new_data_subset)
        label_subsets.append(new_label_subset)
    return data_subsets, label_subsets

def gini(dataset):
  impurity = 1
  label_counts = Counter(dataset)
  for label in label_counts:
    prob_of_label = label_counts[label] / len(dataset)
    impurity -= prob_of_label ** 2
  return impurity

def information_gain(starting_labels, split_labels):
  info_gain = gini(starting_labels)
  for subset in split_labels:
    info_gain -= gini(subset) * len(subset)/len(starting_labels)
  return info_gain

class Leaf:
    def __init__(self, labels):
        self.predictions = Counter(labels)

class Internal_Node:
    def __init__(self,
                 feature,
                 branches):
        self.feature = feature
        self.branches = branches

def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""
    question_dict = {0: "Buying Price", 1:"Price of maintenance", 2:"Number of doors", 3:"Person Capacity", 4:"Size of luggage boot", 5:"Estimated Saftey"}
    # Base case: we've reached a leaf
    if isinstance(node, Counter):
        print (spacing + str(node))
        return

    # Print the question at this node
    print (spacing + "Splitting")

    # Call this function recursively on the true branch
    for i in range(len(node)):
        print (spacing + '--> Branch ' + str(i)+':')
        print_tree(node[i], spacing + "  ")


#####

from sklearn import tree

car_data = [['med', 'low', '3', '4', 'med', 'med'], ['med', 'vhigh', '4', 'more', 'small', 'high'], ['high', 'med', '3', '2', 'med', 'low'], ['med', 'low', '4', '4', 'med', 'low'], ['med', 'low', '5more', '2', 'big', 'med'], ['med', 'med', '2', 'more', 'big', 'high'], ['med', 'med', '2', 'more', 'med', 'med'], ['vhigh', 'vhigh', '2', '2', 'med', 'low'], ['high', 'med', '4', '2', 'big', 'low'], ['low', 'low', '2', '4', 'big', 'med']]

car_labels = ['acc', 'acc', 'unacc', 'unacc', 'unacc', 'vgood', 'acc', 'unacc', 'unacc', 'good']

def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0
    for feature in range(len(dataset[0])):
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_feature, best_gain


def build_tree(data, labels):
    best_feature, best_gain = find_best_split(data, labels)
    if best_gain == 0:
        return Counter(labels)
    data_subsets, label_subsets = split(data, labels, best_feature)
    branches = []
    for i in range(len(data_subsets)):
        branches.append(build_tree(data_subsets[i], label_subsets[i]))
    return branches

tree = build_tree(car_data, car_labels)
print_tree(tree)

"""
We’ve slightly changed the way our build_tree() function works. Instead of returning a list of branches or a Counter object, the build_tree() function now returns a Leaf object or an Internal_Node object. We’ll explain how to use these objects in the instructions!

We’ve created a tree named tree using a lot of car data. Use the print_tree() function with tree as a parameter to see it.

Notice that the tree now knows which feature was used to split the data. This new information is contained in the Leaf and Internal_Node classes. This will come in handy when we write our classify function!

Let’s start writing the classify() function. classify() should take a datapoint and a tree as a parameter.

The first thing classify should do is check to see if we’re at a leaf.

Check to see if tree is a Leaf by using the isinstance() function.

For example, isinstance(a, list) will be True if a is a list. You should check if tree is a Leaf.

If we’ve found a Leaf, that means we want to return the label with the highest count. The label counts are stored in tree.labels.

If we’re not at a leaf, we want to find the branch that corresponds to our data point. For example, if we’re splitting on index 0 and our data point is ['med', 'low', '4', '2', 'big', 'low'], we want to find the branch that contains all of the points with med at index 0.

To start, let’s find datapoint‘s value of the feature we’re looking for. If datapoint were the example above, and the feature we’re interested is 0, this would be med.

Outside the if statement, create a variable named value and set it equal to datapoint[tree.feature]. tree.feature contains the index of the feature that we’re splitting on, so datapoint[tree.feature] is the value at that index.

Let’s now loop through all of the branches in the tree to find the one that has all the data points with value at the correct index.

Next, inside the loop, check to see if branch.value is equal to value. If it is, we’ve found the branch that we’re looking for! We want to now recursively call classify() on that branch:

We know that one of these branches will be the one we’re looking for, so we know that this return statement will happen once.
"""

import operator

test_point = ['vhigh', 'low', '3', '4', 'med', 'med']

# print_tree(tree)

def classify(datapoint, tree):
  if isinstance(tree, Leaf):
    return max(tree.labels.items(), key=operator.itemgetter(1))[0]
  value = datapoint[tree.feature]
  for branch in tree.branches:
    if branch.value == value:
      return classify(datapoint, branch)

print(classify(test_point, tree))

"""
Nice work! You’ve written a decision tree from scratch that is able to classify new points. Let’s take a look at how the Python library scikit-learn implements decision trees.

The sklearn.tree module contains the DecisionTreeClassifier class. To create a DecisionTreeClassifier object, call the constructor:

classifier = DecisionTreeClassifier()

Next, we want to create the tree based on our training data. To do this, we’ll use the .fit() method.

.fit() takes a list of data points followed by a list of the labels associated with that data. Note that when we built our tree from scratch, our data points contained strings like "vhigh" or "5more". When creating the tree using scikit-learn, it’s a good idea to map those strings to numbers. For example, for the first feature representing the price of the car, "low" would map to 1, "med" would map to 2, and so on.

classifier.fit(training_data, training_labels)

Finally, once we’ve made our tree, we can use it to classify new data points. The .predict() method takes an array of data points and will return an array of classifications for those data points.

predictions = classifier.predict(test_data)

If you’ve split your data into a test set, you can find the accuracy of the model by calling the .score() method using the test data and the test labels as parameters.

print(classifier.score(test_data, test_labels))

.score() returns the percentage of data points from the test set that it classified correctly.

>>>>> Decision Tree Limitations

Now that we have an understanding of how decision trees are created and used, let’s talk about some of their limitations.

One problem with the way we’re currently making our decision trees is that our trees aren’t always globablly optimal. This means that there might be a better tree out there somewhere that produces better results. But wait, why did we go through all that work of finding information gain if it’s not producing the best possible tree?

Our current strategy of creating trees is greedy. We assume that the best way to create a tree is to find the feature that will result in the largest information gain right now and split on that feature. We never consider the ramifications of that split further down the tree. It’s possible that if we split on a suboptimal feature right now, we would find even better splits later on. Unfortunately, finding a globally optimal tree is an extremely difficult task, and finding a tree using our greedy approach is a reasonable substitute.

Another problem with our trees is that they potentially overfit the data. This means that the structure of the tree is too dependent on the training data and doesn’t accurately represent the way the data in the real world looks like. In general, larger trees tend to overfit the data more. As the tree gets bigger, it becomes more tuned to the training data and it loses a more generalized understanding of the real world data.

One way to solve this problem is to prune the tree. The goal of pruning is to shrink the size of the tree. There are a few different pruning strategies, and we won’t go into the details of them here. scikit-learn currently doesn’t prune the tree by default, however we can dig into the code a bit to prune it ourselves.

#####

If your classifier is named classifier, you can find the depth of the tree by printing classifier.tree_.max_depth.

>>>>> Review
Great work! In this lesson, you learned how to create decision trees and use them to make classifications. Here are some of the major takeaways:

- Good decision trees have pure leaves. A leaf is pure if all of the data points in that class have the same label.
- Decision trees are created using a greedy algorithm that prioritizes finding the feature that results in the largest information gain when splitting the data using that feature.
- Creating an optimal decision tree is difficult. The greedy algorithm doesn’t always find the globally optimal tree.
- Decision trees often suffer from overfitting. Making the tree small by pruning helps to generalize the tree so it is more accurate on data in the real world.
"""
