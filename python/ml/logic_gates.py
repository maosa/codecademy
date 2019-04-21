##### LOGIC GATES - PERCEPTRONS PROJECT

"""
In this project, we will use perceptrons to model the fundamental building blocks of computers — logic gates.

For example, the table below shows the results of an AND gate. Given two inputs, an AND gate will output a 1 only if both inputs are a 1:

Input 1	Input 2	Output
0	      0	      0
0	      1	      0
1	      0	      0
1	      1	      1

We’ll discuss how an AND gate can be thought of as linearly separable data and train a perceptron to perform AND.

We’ll also investigate an XOR gate — a gate that outputs a 1 only if one (but not both) of the inputs is a 1

We’ll think about why an XOR gate isn’t linearly separable and show how a perceptron fails to learn XOR.
"""

##### To begin, let’s think of an AND gate as a dataset of four points. The four points should be the four possible inputs to the AND gate. For example, the first point in the dataset should be [0, 0].

import sys ##### needed for sys.exit()
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

data = [[0, 0], [1, 0], [0, 1], [1, 1]]

labels = [0, 0, 0, 1]

plt.scatter([point[0] for point in data], [point[1] for point in data], c = labels)

##### Build a perceptron
##### max_iter sets the number of times the perceptron loops through the training data. The default is 1000, so were cutting the training pretty short! Lets see if our algorithm learns AND even with very little training.
classifier = Perceptron(max_iter = 40, tol = -np.infty)

##### tol = -np.infty is used to avoid some warning messages

classifier.fit(data, labels)

##### Note that it is pretty unusual to train and test on the same dataset. In this case, since there are only four possible inputs to AND, were stuck training on every possible input and testing on those same points.
# print(classifier.score(data, labels))

##### Your perceptron should have 100% accuracy! You just taught it an AND gate!

##### Change labels to those for an XOR logic gate
labels = [0, 1, 1, 0]
classifier.fit(data, labels)
# print(classifier.score(data, labels))

##### Change labels to those for an OR logic gate
labels = [0, 1, 1, 1]
classifier.fit(data, labels)
# print(classifier.score(data, labels))

##### We know the perceptron has been trained correctly, but lets try to visualize what decision boundary it is making. Reset your labels to be representing an AND gate.
labels = [0, 0, 0, 1] # AND
# labels = [0, 1, 1, 1] # OR
# labels = [0, 1, 1, 0] # XOR
labels_choice = input('\nChoose a logic gate (numbers represent the outputs to to following data points: [[0, 0], [1, 0], [0, 1], [1, 1]])\n1) AND: 0, 0, 0, 1]\n2) OR: [0, 1, 1, 1]\n3) XOR: [0, 1, 1, 0]\n\n')

if labels_choice == '1':
    labels = [0, 0, 0, 1]
    gate = 'AND'
elif labels_choice == '2':
    labels = [0, 1, 1, 1]
    gate = 'OR'
elif labels_choice == '3':
    labels = [0, 1, 1, 0]
    gate = 'XOR'
else:
    sys.exit('\nError! Invalid input!\n')


classifier.fit(data, labels)

##### We know the perceptron has been trained correctly, but lets try to visualize what decision boundary it is making. Reset your labels to be representing an AND gate. Lets first investigate the classifiers .decision_function() method. Given a list of points, this method returns the distance those points are from the decision boundary. The closer the number is to 0, the closer that point is to the decision boundary.

# print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]))

##### Is the point [0, 0] or the point [1, 1] closer to the decision boundary? >>>>> [1, 1]

##### Even though an input like [0.5, 0.5] isnt a real input to an AND logic gate, we can still check to see how far it is from the decision boundary. We could also do this to the point [0, 0.1], [0, 0.2] and so on. If we do this for a grid of points, we can make a heat map that reveals the decision boundary. To begin, we need to create a list of the points we want to input to .decision_function().

##### x_values should be a list of 100 evenly spaced decimals between 0 and 1
x_values = np.linspace(0, 1, 100)

y_values = np.linspace(0, 1, 100)

##### We have a list of 100 x values and 100 y values. We now want to find every possible combination of those x and y values. The function product will do this for you.

point_grid = list(product(x_values, y_values))

distances = classifier.decision_function(point_grid)

##### Right now distances stores positive and negative values. We only care about how far away a point is from the boundary  we dont care about the sign.

abs_distances = [abs(p) for p in distances]

##### Were almost ready to draw the heat map. Were going to be using Matplotlibs pcolormesh() function. Right now, abs_distances is a list of 10000 numbers. pcolormesh needs a two dimensional list. We need to turn abs_distances into a 100 by 100 two dimensional array.

"""
Numpys reshape function does this for us. The code below turns list lst into a 2 by 2 list.

lst = [1, 2 ,3, 4]
new_lst = np.reshape(lst, (2, 2))
new_lst now looks like this:

[[1, 2],[3, 4]]
"""

distances_matrix = np.reshape(abs_distances, (100, 100))

heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)

##### This will put a legend on the heat map
plt.colorbar(heatmap)

plt.title(gate + " logic gate decision boundary")

##### Make sure plt.show() is always the last line of code
plt.show()

##### Change your labels back to representing an OR gate. Where does the decision boundary go? Change your labels to represent an XOR gate. Remember, this data is not linearly separable. Where does the decision boundary go?

##### Perceptrons cant solve problems that arent linearly separable. However, if you combine multiple perceptrons together, you now have a neural net that can solve these problems!
