# 1. Createing a machine learning model that can predict profit based on sales
# and other features , basically a regression task
#
# 2. Predict customer type base on transaction data,basically a classification task
#
"""
1. Import nececssry libraries
2. Load the dataset
3. Preprocess the data (handle missing values, encode categorical variables, etc.) and feature engineering (if necessary)
4. Split the dataset into training and testing sets
5. Choose a machine learning algorithm (e.g., linear regression, decision tree, random forest, etc.)
6. Train the model on the training set
7. Evaluate the model on the testing set using appropriate metrics (e.g., accuracy, precision, recall, F1-score for classification tasks; mean squared error, R-squared for
regression tasks)
8. Fine-tune the model (if necessary) by adjusting hyperparameters or trying different algorithms
9. Make predictions on new data using the trained model
"""

# step 1: Import necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
import warnings

# warnings.filterwarnings("ignore")

# step 2: Load the dataset

df = pd.read_csv("ecommerce_bigdata.csv")

# step 3: Preprocess the data (handle missing values, encode categorical variables, etc.)

# Check for empty values

# Check for duplicate rows

#

# Check for missing values
missing_values = df.isnull().sum()

df = df.dropna()

summary_stats = df.describe()
print(missing_values)
print(summary_stats)

# Data visualization

# Settup plotting style

plt.style.use("seaborn-v0_8-darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# plot distribution of sales
sns.histplot(df["Sales"], bins=30, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Distribution of Sales")
axes[0, 0].set_xlabel("Sales")
axes[0, 0].set_ylabel("Frequency")

# plot distribution of profit
sns.histplot(df["Profit"], bins=30, kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Distribution of Profit")
axes[0, 1].set_xlabel("Profit")
axes[0, 1].set_ylabel("Frequency")

plt.show()

# simple mid-code excercise
# Plot sales by product category using a boxplot
# Plot relationship between sales and profit using a scatter plot

# sales by product category using a boxplot
sns.boxplot(x="ProductCategory", y="Sales", data=df, ax=axes[1, 0])
axes[1, 0].set_title("Sales by Product Category")
axes[1, 0].set_xlabel("Product Category")
axes[1, 0].set_ylabel("Sales")

# Sales vs Profit using a scatter plot
sns.scatterplot(x="Sales", y="Profit", data=df, ax=axes[1, 1])
axes[1, 1].set_title("Sales vs Profit")
axes[1, 1].set_xlabel("Sales")
axes[1, 1].set_ylabel("Profit")

plt.show()


# Feature engineering: Create new features based on existing ones (if necessary)

df_copy = df.copy()

# Convert data to datetime format
df_copy["Date"] = pd.to_datetime(df_copy["Date"])
df_copy["Year"] = df_copy["Date"].dt.year
df_copy["Month"] = df_copy["Date"].dt.month
df_copy["Day"] = df_copy["Date"].dt.day
df_copy["Weekday"] = df_copy["Date"].dt.weekday

print(df_copy.head())
# step 4: Split the dataset into training and testing sets
#
