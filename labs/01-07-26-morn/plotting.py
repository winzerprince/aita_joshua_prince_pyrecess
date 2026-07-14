import matplotlib.pyplot as plt

x = [0, 2, 4, 8, 10]
y = [i**2 for i in x]

plt.plot(x, y)
plt.title("Plot of y = x^2")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()
