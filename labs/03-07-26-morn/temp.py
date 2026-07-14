# Scikit library
# The sciki t-learn library is a powerful tool for machine learning in Python.
# It provides simple and efficient tools for data mining and data analysis, built on top of NumPy, SciPy,
# and matplotlib. In this lab, we will explore some of the basic functionalities of scikit-learn.
#
# 1. Import the necessary libraries

# Key features
# 1. Data preprocessing: Scikit-learn provides various tools for data preprocessing, such as scaling,
#    normalization, and encoding categorical variables.
# - Data splitting: The library offers functions to split
#    datasets into training and testing sets, which is essential for model evaluation.
# - Feature scaling and normalization: Scikit-learn provides methods for scaling and
#    normalizing features, which can improve model performance.
# - Feature engineering: The library includes tools for feature
#    extraction and transformation, allowing users to create new features from existing ones.
# - Absolute maximum scaling: Scikit-learn provides a method for absolute maximum scaling,
#    which scales each feature by its maximum absolute value.
#
# 2. Model Evaluation
# -
# 3.Pipeline Support
# 4.Supports integration
# 5.Easy to use
#
# Machine learning techniques scikit-learnn supports include;
# - Supervised learning: Algorithms such as linear regression, logistic regression, decision trees, random forests, support vector machines (SVM), and k-nearest neighbors (KNN) are available for tasks like classification and regression.
# - Unsupervised learning: Techniques like k-means clustering, hierarchical clustering, and principal component analysis (PCA) are provided for tasks such as clustering and dimensionality reduction.
# - Reinforcement learning: While scikit-learn primarily focuses on supervised and unsupervised learning, it can be used in conjunction with other libraries for reinforcement learning tasks.
#
import pandas as pd
import zipfile

# Option 1: Read the main iris.data file directly from zip
with zipfile.ZipFile("iris.zip") as z:
    with z.open("iris.data") as f:
        df = pd.read_csv(f, header=None)

print(df.head())
print(df.shape)
