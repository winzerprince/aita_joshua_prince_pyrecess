# Histogram
# Similar to bar char but used to represent the distribution of numerical data rather than categorical data.
#
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(data, bins=5, color="lightcoral", edgecolor="black")
plt.title("Histogram Example")
plt.xlabel("Value Ranges")
plt.ylabel("Frequency")
plt.legend(["Frequency"])
plt.show()
