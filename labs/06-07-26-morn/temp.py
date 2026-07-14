# Objectives of our project
# 1. To find the number of active and inactive customers
# 2. To find the most impactful features in determining customer retention
# 3. To find the relationship between customer demographics and churn
# 4. To prepare the data for predictive modeling
# 5. To handle null values and outliers in the dataset
# 6. To evaluate the preditive performance of the model
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Customer-Churn.csv")

print(df.head())
print(df.describe())

df["Churn"].value_counts().plot(kind="bar")
plt.show()
