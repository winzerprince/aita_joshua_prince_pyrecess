# Piechart
# Useful for visualizing proportions of a whole
import matplotlib.pyplot as plt

data = [30, 20, 15, 10, 25]

labels = ["Category A", "Category B", "Category C", "Category D", "Category E"]

fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%", startangle=90)
ax.set_title("Pie Chart Example")
ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
