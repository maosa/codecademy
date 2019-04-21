# Import codecademylib
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

# Load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Histogram 1
plt.figure(1)
plt.subplot(2, 1, 1)
plt.hist(flights, range = (0, 365), bins = 365)
plt.xlabel('Day')
plt.ylabel('Frequency')
plt.title('Flight frequency per day')
# Histogram 2
plt.subplot(2, 1, 2)
plt.hist(in_bloom, range = (0, 365), bins = 365)
plt.title("Flower Blooms and Flights by Day")
plt.ylabel("Bloom Count")
plt.xlabel("Day of the Year")
# Plot histogram
plt.tight_layout() # this will prevent the labels from overlapping with the graphs
plt.show()
