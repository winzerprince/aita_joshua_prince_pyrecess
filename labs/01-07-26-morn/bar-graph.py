# Bar graph
# Displays categorical data using rectrangular bars.
# The length of each bar is proportional to the value it represents.
import matplotlib.pyplot as plt

w = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
z = [5, 7, 3, 8, 6]

fig, ax = plt.subplots()

ax.bar(w, z, color="skyblue")
ax.set_title("Bar Graph Example")
ax.set_xlabel("Days of the Week")
ax.set_ylabel("Values")


plt.show()
