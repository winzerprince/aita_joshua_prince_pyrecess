# scatter plot
# Usefull for visualizing the relationship between two variables and identifying patterns or trends in the data.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 5]

fig, ax = plt.subplots()
ax.scatter(x, y, color="green", marker="o", label="Data Points")
ax.set_title("Scatter Plot Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

plt.legend()
plt.show()
