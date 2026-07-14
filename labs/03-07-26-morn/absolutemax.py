import pandas as pd
import numpy as np

df = pd.read_csv("Housing.csv")
df = df.select_dtypes(include=[np.number])  # Select only numeric columns
print(df.head())

max_abs = np.max(np.abs(df), axis=0)
print(f"Maximum absolute values for each column: {max_abs}")

scaled_df = df / max_abs
print(scaled_df.head())
