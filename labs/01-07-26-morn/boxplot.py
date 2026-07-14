# box plot
# A simple graph that shos how data is spread out
# Helpful for visualizing the distribution of data and identifying outliers.
# example

import matplotlib.pyplot as plt

data = [[7, 8, 5, 6, 9], [1, 2, 3, 4, 5], [10, 12, 14, 16, 18]]

plt.boxplot(data)
plt.title("Box Plot Example")
plt.xlabel("Data Sets")
plt.ylabel("Values")
plt.show()
