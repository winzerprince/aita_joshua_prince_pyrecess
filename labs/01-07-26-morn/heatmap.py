# Heatmap
# Usefull to represent data in a matrix format, where individual values are represented as colors.
# It is often used to visualize the correlation between variables or to display the intensity of
# data points in a two-dimensional space.
# You will need libraries namely matplotlib and seaborn to create a heatmap.
# You can install them using pip if you haven't already:
# seaborn is necessary because it provides a high-level interface for
# drawing attractive and informative statistical graphics, including heatmaps.
#
import matplotlib.pyplot as plt
import seaborn as sns

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sns.heatmap(x, annot=True, cmap="YlGnBu", cbar=True)
plt.title("Heatmap Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
