##### K-MEANS CLUSTERING
"""
>>>>> Introduction to Clustering

Often, the data you encounter in the real world won’t have flags attached and won’t provide labeled answers to your question. Finding patterns in this type of data, unlabeled data, is a common theme in many machine learning applications. Unsupervised Learning is how we find patterns and structure in these data.

Clustering is the most well-known unsupervised learning technique. It finds structure in unlabeled data by identifying similar groups, or clusters. Examples of clustering applications are:

1) Recommendation engines: group products to personalize the user experience
2) Search engines: group news topics and search results
3) Market segmentation: group customers based on geography, demography, and behaviors
4) Image segmentation: medical imaging or road scene segmentation on self-driving cars

The goal of clustering is to separate data so that data similar to one another are in the same group, while data different from one another are in different groups. So two questions arise:

- How many groups do we choose?
- How do we define similarity?

K-Means is the most popular and well-known clustering algorithm, and it tries to address these two questions.

The “K” refers to the number of clusters (groups) we expect to find in a dataset.
The “Means” refers to the average distance of data to each cluster center, also known as the centroid, which we are trying to minimize.
It is an iterative approach:

1) Place k random centroids for the initial clusters.
2) Assign data samples to the nearest centroid.
3) Update centroids based on the above-assigned data samples.

Repeat Steps 2 and 3 until convergence (when points don’t move between clusters and centroids stabilize).

Once we are happy with our clusters, we can take a new unlabeled datapoint and quickly assign it to the appropriate cluster.

Before we implement the K-means algorithm, let’s find a dataset. The sklearn package embeds some datasets and sample images. One of them is the Iris dataset.

The Iris dataset consists of measurements of sepals and petals of 3 different plant species:

- Iris setosa
- Iris versicolor
- Iris virginica

The sepal is the part that encases and protects the flower when it is in the bud stage. A petal is a leaflike part that is often colorful.

From sklearn library, import the datasets module:

from sklearn import datasets

To load the Iris dataset:

iris = datasets.load_iris()

We call each piece of data a sample. For example, each flower is one sample.

Each characteristic we are interested in is a feature. For example, petal length is a feature of this dataset.

The features of the dataset are:

Column 0: Sepal length
Column 1: Sepal width
Column 2: Petal length
Column 3: Petal width

The 3 species of Iris plants are what we are going to cluster later in this lesson.

Every dataset from sklearn comes with a bunch of different information (not just the data) and is stored in a similar fashion.

First, let’s take a look at the most important thing, the sample data:

print(iris.data)

Each row is a plant!

Since the datasets in sklearn datasets are used for practice, they come with the answers (target values) in the target key:

Take a look at the target values:

print(iris.target)

The iris.target values give the ground truth for the Iris dataset. Ground truth, in this case, is the number corresponding to the flower that we are trying to learn.

It is always a good idea to read the descriptions of the data:

print(iris.DESCR)

Expand the terminal (right panel):

When was the Iris dataset published?
What is the unit of measurement?

>>>>> Visualize Before K-Means

To get a better sense of the data in the iris.data matrix, let’s visualize it!

With Matplotlib, we can create a 2D scatter plot of the Iris dataset using two of its features (sepal length vs. petal length). The sepal length measurements are stored in column 0 of the matrix, and the petal length measurements are stored in column 2 of the matrix.

But how do we get these values?

Suppose we only want to retrieve the values that are in column 0 of a matrix, we can use the NumPy/Pandas notation [:,0] like so:

matrix[:,0]

[:,0] can be translated to [all_rows , column_0]

Once you have the measurements we need, we can make a scatter plot by:

plt.scatter(x, y)
plt.show()
"""

import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

##### Store iris.data
samples = iris.data
##### Create x and y
x = samples[:, 0]
y = samples[:, 1]
##### Plot x and y
plt.scatter(x, y, alpha = 0.5)
##### Show the plot
plt.show()

"""
>>>>> Implementing K-Means: Step 1

The K-Means algorithm:

1) Place k random centroids for the initial clusters.
2) Assign data samples to the nearest centroid.
3) Update centroids based on the above-assigned data samples.

Repeat Steps 2 and 3 until convergence.

After looking at the scatter plot and having a better understanding of the Iris data, let’s start implementing the K-Means algorithm.

In this exercise, we will implement Step 1.

Because we expect there to be three clusters (for the three species of flowers), let’s implement K-Means where the k is 3.

Using the NumPy library, we will create 3 random initial centroids and plot them along with our samples.

Use NumPy’s random.uniform() function to generate random values in two lists:

a centroids_x list that will have k random values between min(x) and max(x)
a centroids_y list that will have k random values between min(y) and max(y)
The random.uniform() function looks like:

np.random.uniform(low, high, size)

The centroids_x will have the x-values for our initial random centroids and the centroids_y will have the y-values for our initial random centroids.

Create an array named centroids and use the zip() function to add centroids_x and centroids_y to it.

The zip() function looks like:

np.array(list(zip(array1, array2)))

Then, print centroids.

The centroids list should now have all the initial centroids.
"""

import numpy as np

##### Number of clusters
k = 3
##### Create x coordinates of k random centroids
centroids_x = np.random.uniform(min(x), max(x), k)
##### Create y coordinates of k random centroids
centroids_y = np.random.uniform(min(y), max(y), k)
##### Create centroids array
centroids = np.array(list(zip(centroids_x, centroids_y)))
print(centroids)
##### Make a scatter plot of x, y
plt.scatter(y, x)
##### Make a scatter plot of the centroids
plt.scatter(centroids_x, centroids_y)
##### Display plot
plt.show()

"""
>>>>> Implementing K-Means: Step 2

Assign data samples to the nearest centroid.

In this exercise, we will implement Step 2.

Now we have the 3 random centroids. Let’s assign data points to their nearest centroids.

To do this we’re going to use the Distance Formula to write a distance() function. Then, we are going to iterate through our data samples and compute the distance from each data point to each of the 3 centroids.

Suppose we have a point and a list of three distances in distances and it looks like [15, 20, 5], then we would want to assign the data point to the 3rd centroid. The argmin(distances) would return the index of the lowest corresponding distance, 2, because the index 2 contains the minimum value.

Create an array called labels that will hold the cluster labels for each data point. Its size should be the length of the data sample.

It should look something like:

[ 0.  0.  0.  0.  0.  0.  ...  0.]

Create an array called distances that will hold the distances for each centroid. It should have the size of k.

It should look something like:

[ 0.  0.  0.]
"""

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

sepal_length_width = np.array(list(zip(x, y)))

##### Step 2: Assign samples to nearest centroid

##### Distance formula
def distance(a, b):
    one = (a[0] - b[0])**2
    two = (a[1] - b[1])**2
    distance = (one + two)**0.5
    return distance


labels = np.zeros(len(samples))

distances = np.zeros(k)

##### Cluster labels for each point (either 0, 1, or 2)

for i in range(len(samples)):
    ##### Distances to each centroid
    distances[0] = distance(sepal_length_width[i], centroids[0])
    distances[1] = distance(sepal_length_width[i], centroids[1])
    distances[2] = distance(sepal_length_width[i], centroids[2])
    ##### Assign to the closest centroid
    cluster = np.argmin(distances)
    labels[i] = cluster

##### Print labels
print(labels)

"""
>>>>> Implementing K-Means: Step 3

In this exercise, we will implement Step 3.

Find new cluster centers by taking the average of the assigned points. To find the average of the assigned points, we can use the .mean() function.

Save the old centroids value before updating.

Use:

from copy import deepcopy

Store centroids into centroids_old using deepcopy():

centroids_old = deepcopy(centroids)

Then, create a for loop that iterates k times.

Since k = 3, as we are iterating through the forloop each time, we can calculate mean of the points that have the same cluster label.

Inside the for loop, create an array named points where we get all the data points that have the cluster label i.

Then, calculate the mean of those points using .mean() to get the new centroid.
"""

from copy import deepcopy

##### Step 3: Update centroids
centroids_old = deepcopy(centroids)

for i in range(k):
    points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
    ##### OR use a nested for loop
    # for n in range(k):
    #   points = []
    #   for j in range(len(sepal_length_width)):
    #     if labels[j] == i:
    #       points.append(sepal_length_width[j])
    ##### We need the axis=0 here to specify that we want to compute the means along the rows
    centroids[i] = np.mean(points, axis = 0)

print(centroids_old)

print(centroids)

"""
>>>>> Implementing K-Means: Step 4 (Repeat Steps 2 and 3 until convergence)

This is the part of the algorithm where we repeatedly execute Step 2 and 3 until the centroids stabilize (convergence).

We can do this using a while loop. And everything from Step 2 and 3 goes inside the loop.

For the condition of the while loop, we need to create an array named errors. In each error index, we calculate the difference between the updated centroid (centroids) and the old centroid (centroids_old).

The loop ends when all three values in errors are 0.
"""

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

sepal_length_width = np.array(list(zip(x, y)))

##### Step 1: Place K random centroids

k = 3

centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)

centroids = np.array(list(zip(centroids_x, centroids_y)))

def distance(a, b):
    one = (a[0] - b[0]) ** 2
    two = (a[1] - b[1]) ** 2
    distance = (one + two) ** 0.5
    return distance

##### To store the value of centroids when it updates
centroids_old = np.zeros(centroids.shape)

##### Cluster labeles (either 0, 1, or 2)
labels = np.zeros(len(samples))

distances = np.zeros(3)

##### Initialize error:
#### Use the distance() function to calculate the distance between the updated centroid and the old centroid and put them in error
error = np.zeros(3)
error[0] = distance(centroids[0], centroids_old[0])
error[1] = distance(centroids[1], centroids_old[1])
error[2] = distance(centroids[2], centroids_old[2])

##### Repeat Steps 2 and 3 until convergence:
while error.all() != 0:
    ##### Step 2: Assign samples to nearest centroid
    for i in range(len(samples)):
        distances[0] = distance(sepal_length_width[i], centroids[0])
        distances[1] = distance(sepal_length_width[i], centroids[1])
        distances[2] = distance(sepal_length_width[i], centroids[2])
        cluster = np.argmin(distances)
        labels[i] = cluster
        error = np.zeros(3)

    ##### Step 3: Update centroids
    centroids_old = deepcopy(centroids)

    for i in range(3):
        points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
        centroids[i] = np.mean(points, axis=0)

    error[0] = distance(centroids[0], centroids_old[0])
    error[1] = distance(centroids[1], centroids_old[1])
    error[2] = distance(centroids[2], centroids_old[2])


colors = ['r', 'g', 'b']

for i in range(k):
    points = np.array([sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i])
    plt.scatter(points[:, 0], points[:, 1], c = colors[i], alpha = 0.5)


##### Here, we are visualizing all the points in each of the labels a different color
plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'D', s = 150)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

"""
>>>>> Implementing K-Means: Scikit-Learn

Instead of implementing K-Means from scratch, the sklearn.cluster module has many methods that can do this for you.

To import KMeans from sklearn.cluster:

from sklearn.cluster import KMeans

For Step 1, use the KMeans() method to build a model that finds k clusters. To specify the number of clusters (k), use the n_clusters keyword argument:

model = KMeans(n_clusters = k)

For Steps 2 and 3, use the .fit() method to compute K-Means clustering:

model.fit(X)

After K-Means, we can now predict the closest cluster each sample in X belongs to. Use the .predict() method to compute cluster centers and predict cluster index for each sample:

model.predict(X)
"""

from sklearn import datasets

##### From sklearn.cluster, import KMeans class
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

##### Use KMeans() to create a model that finds 3 clusters
model = KMeans(n_clusters = 3)
##### Use .fit() to fit the model to samples
model.fit(samples)
##### Use .predict() to determine the labels of samples
model.predict(samples)
##### Print the labels
print(model.predict(samples))

new_samples = np.array([[5.7, 4.4, 1.5, 0.4], [6.5, 3. , 5.5, 0.4], [5.8, 2.7, 5.1, 1.9]])

print(new_samples)

"""
>>>>> Visualize After K-Means

We have done the following using sklearn library:

- Load the embedded dataset
- Compute K-Means on the dataset (where k is 3)
- Predict the labels of the data samples

And the labels resulted in either 0, 1, or 2.

Let’s finish it by making a scatter plot of the data again!

This time, however, use the labels numbers as the colors.

To edit colors of the scatter plot, we can set c = labels
"""

x = samples[:, 0]
y = samples[:, 1]

plt.scatter(x, y, c = labels, alpha = 0.5)
plt.show()

"""
>>>>> Evaluation

At this point, we have clustered the Iris data into 3 different groups (implemented using Python and using scikit-learn). But do the clusters correspond to the actual species? Let’s find out!

First, remember that the Iris dataset comes with target values:

target = iris.target
It looks like:

[ 0 0 0 0 0 ... 2 2 2]
According to the metadata:

All the 0‘s are Iris-setosa
All the 1‘s are Iris-versicolor
All the 2‘s are Iris-virginica
Let’s change these values into the corresponding species using the following code:

species = np.chararray(target.shape, itemsize=150)

for i in range(len(samples)):
    if target[i] == 0:
        species[i] = 'setosa'
    elif target[i] == 1:
        species[i] = 'versicolor'
    elif target[i] == 2:
        species[i] = 'virginica'

Then we are going to use the Pandas library to perform a cross-tabulation.

Cross-tabulations enable you to examine relationships within the data that might not be readily apparent when analyzing total survey responses.
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd

iris = datasets.load_iris()

samples = iris.data

target = iris.target

model = KMeans(n_clusters=3)

model.fit(samples)

labels = model.predict(samples)

species = np.chararray(target.shape, itemsize = 150)

for i in range(len(samples)):
    if target[i] == 0:
        species[i] = 'setosa'
    elif target[i] == 1:
        species[i] == 'versicolor'
    elif target[i] == 2:
        species[i] == 'virginica'


df = pd.DataFrame({'labels': labels, 'species': species})
print(df)

##### Use the the crosstab() method to perform cross-tabulation
ct = pd.crosstab(df['labels'], df['species'])
print(ct)

"""
>>>>> The Number of Clusters

At this point, we have grouped the Iris plants into 3 clusters. But suppose we didn’t know there are three species of Iris in the dataset, what is the best number of clusters? And how do we determine that?

Before we answer that, we need to define what is a good cluster?

Good clustering results in tight clusters, meaning that the samples in each cluster are bunched together. How spread out the clusters are is measured by inertia. Inertia is the distance from each sample to the centroid of its cluster. The lower the inertia is, the better our model has done.

You can check the inertia of a model by:

print(model.inertia_)

For the Iris dataset, if we graph all the ks (number of clusters) with their inertias.

Notice how the graph keeps decreasing.

Ultimately, this will always be a trade-off. The goal is to have low inertia and the least number of clusters.

One of the ways to interpret this graph is to use the elbow method: choose an “elbow” in the inertia plot - when inertia begins to decrease more slowly.

In the graph above, 3 is the optimal number of clusters.
"""

num_clusters = list(range(1, 9))
inertias = []

for k in num_clusters:
    model = KMeans(n_clusters = k)
    model.fit(samples)
    inertias.append(model.inertia_)

plt.plot(num_clusters, inertias, '-o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()
