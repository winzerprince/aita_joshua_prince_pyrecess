# Numpy library
# what is numpy?
# Numpy is a powerful library in Python that is used for numerical computing. It provides support
# for large multi-dimensional arrays and matrices, along with a collection of mathematical functions
# to operate on these arrays efficiently. Numpy is widely used in data science, machine learning,
# and scientific computing due to its performance and ease of use.

import numpy as np

print(np.__version__)

# the numpy array
# - it is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers.
# - the number of dimensions is the rank of the array; the shape of an array is
# - a tuple of integers giving the size of the array along each dimension.

array1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", array1)

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array2)
print("Shape of 2D Array:", array2.shape)
print("Rank of 2D Array:", array2.ndim)
print("Size of 2D Array:", array2.size)
print("Data type of 2D Array:", array2.dtype)

for element in array1:
    print("Element:", element)

# mathematical array manipulation
# - mathematical operations on arrays are performed element-wise, meaning that the operation is
# - applied to each corresponding element of the arrays.
# Examples of array manipulation include addition, subtraction, multiplication,
# division, and more complex operations like dot products and matrix multiplication.

array3 = np.array([10, 20, 30, 40, 50])
# Element-wise addition
print("Element-wise Addition:", array1 + array3)

# Element-wise multiplication
print("Element-wise Multiplication:", array1 * array3)

# Dot product
print("Dot Product:", np.dot(array1, array3))

# Reshaping arrays
print("Original Shape of array2:", array2.shape)
print("Reshaped array2 to (3, 2):\n", array2.reshape(3, 2))

# Slicing arrays
print("Sliced array2 (first row):", array2[0, :])

# Broadcasting
# - Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes
# - during arithmetic operations. It automatically expands the smaller array to match the shape of the larger
# - array, enabling element-wise operations without the need for explicit replication of data.
# Example

print("Broadcasting Example:")
array4 = np.array([[1], [2], [3]])
array5 = np.array([10, 20, 30])
print("Array4:\n", array4)
print("Array5:\n", array5)
# Broadcasting addition
print("Broadcasted Addition:\n", array4 + array5)

# Random number generation
# - Numpy provides a suite of functions for generating random numbers, which are essential for simulations
# - and probabilistic modeling. These functions can generate random numbers from various distributions,
# - including uniform, normal, and binomial distributions. Random number generation is crucial in many
# - applications, such as Monte Carlo simulations, randomized algorithms, and data augmentation in machine learning
# Example

array6 = np.random.rand(3, 3)  # Uniform distribution
print("Random Array (Uniform Distribution):\n", array6)
array7 = np.random.randn(3, 3)  # Normal distribution
print("Random Array (Normal Distribution):\n", array7)
array8 = np.random.randint(0, 10, (3, 3))  # Random integers
print("Random Array (Random Integers):\n", array8)
array9 = np.random.choice([1, 2, 3, 4, 5], size=(3, 3))  # Random choice from a list
print("Random Array (Random Choice):\n", array9)
array10 = np.random.binomial(n=10, p=0.5, size=(3, 3))  # Binomial distribution
print("Random Array (Binomial Distribution):\n", array10)

# Other useful numpy functions
# - Numpy provides a wide range of functions for various mathematical and statistical operations, including:
# - np.sum(): Computes the sum of array elements.
# - np.mean(): Computes the mean of array elements.
# - np.median(): Computes the median of array elements.
# - np.std(): Computes the standard deviation of array elements.
# - np.min() and np.max(): Find the minimum and maximum values in an array.
# - np.argmin() and np.argmax(): Find the indices of the minimum and maximum values in an array.
# - np.unique(): Finds the unique elements in an array.
# - np.sort(): Sorts the elements of an array.
# - np.concatenate(): Concatenates two or more arrays.
# - np.vstack() and np.hstack(): Stack arrays vertically or horizontally.
# - np.linalg.inv(): Computes the inverse of a matrix.
# - np.linalg.det(): Computes the determinant of a matrix.
# - np.linalg.eig(): Computes the eigenvalues and eigenvectors of a matrix.
# - np.fft.fft(): Computes the one-dimensional discrete Fourier Transform.
# - np.fft.ifft(): Computes the one-dimensional inverse discrete Fourier Transform.
# - np.fft.fft2(): Computes the two-dimensional discrete Fourier Transform.
# - np.fft.ifft2(): Computes the two-dimensional inverse discrete Fourier Transform.
# - np.fft.fftn(): Computes the N-dimensional discrete Fourier Transform.
# - np.linspace(): Generates linearly spaced values between two endpoints.
# - np.logspace(): Generates logarithmically spaced values between two endpoints.
# - np.meshgrid(): Generates coordinate matrices from coordinate vectors.
# - np.zeros(): Creates an array filled with zeros.
# - np.ones(): Creates an array filled with ones.
# - np.eye(): Creates an identity matrix.
# - np.diag(): Creates a diagonal matrix or extracts the diagonal of a matrix.
# - np.triu() and np.tril(): Extract the upper or lower triangular part of a matrix.
# - np.random.seed(): Sets the seed for random number generation to ensure reproducibility.
# - np.save() and np.load(): Save and load arrays to/from binary files.
# - np.savetxt() and np.loadtxt(): Save and load arrays to/from text files.
# - np.genfromtxt(): Load data from a text file, with missing values handled gracefully.
# - np.recarray(): Create a record array, which allows for heterogeneous data types.
# - np.char: Provides a set of vectorized string operations for arrays of strings.
# - np.datetime64(): Represents dates and times in a compact format.
# - np.timedelta64(): Represents time durations in a compact format.
# - np.isfinite(), np.isinf(), np.isnan(): Check for finite, infinite, or NaN values in an array.
#

# Sample usecase of numpy to solve a more complex problem using all concepts learned above
# Problem: Given a dataset of students' scores in different subjects, we want to calculate the
# average score for each student, identify the top-performing student, and visualize the score distribution.
#

# Step 1: Create a dataset of students' scores

scores = np.array([[85, 90, 78], [92, 88, 95], [76, 85, 80], [89, 94, 91]])
students = np.array(["Alice", "Bob", "Charlie", "David"])

# Step 2: Calculate the average score for each student
# the axxis represents the dimension along which the mean is computed.
# axis=1 means we are calculating the mean across columns (i.e., for each student).
average_scores = np.mean(scores, axis=1)

# Step 3: Identify the top-performing student
top_student_index = np.argmax(average_scores)
top_student = students[top_student_index]

# Step 4: Visualize the score distribution using a histogram
import matplotlib.pyplot as plt

plt.hist(average_scores, bins=5, color="blue", alpha=0.7)
plt.title("Distribution of Average Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.legend()
plt.show()
plt.savefig("average_scores_distribution.png")
# Note: if you get this "/home/winzer/code/python/class/aita_joshua_prince_pyrecess/labs/29-06-26-morn/temp.py:157: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
#  plt.show()" then you can save the figure instead of showing it by using plt.savefig("average_scores_distribution.png")
#
#
#  Another example is to use numpy to perform linear regression on a dataset of house prices based on their sizes.
#  We will generate synthetic data, fit a linear model, and visualize the results.

# step 1: Generate synthetic data for house sizes and prices
house_sizes = np.random.rand(100) * 2000 + 500  # Sizes between 500 and 2500 sq ft
house_prices = house_sizes * 150 + np.random.randn(100) * 20000

# step 2: Fit a linear regression model using numpy's polyfit function
# The degree represents the degree of the polynomial to fit. In this case, we are fitting a linear model (degree 1).
m, b = np.polyfit(house_sizes, house_prices, 1)  # Linear fit (degree 1)

# step 3: Visualize the data and the fitted line
plt.scatter(house_sizes, house_prices, color="blue", alpha=0.5, label="Data Points")
plt.plot(
    house_sizes,
    m * house_sizes + b,
    color="black",
    label=f"Fitted Line: y = {m:.2f}x + {b:.2f}",
)
plt.title("House Prices vs. Sizes")
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price ($)")
plt.legend()
plt.show()
plt.savefig("house_prices_vs_sizes.png")
