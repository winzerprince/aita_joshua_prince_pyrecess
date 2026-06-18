import pandas as pd

# Create a sample DataFrame
# A dataframe is a 2-dimensional labeled data structure with columns of potentially different types.
# It is similar to a spreadsheet or SQL table, and is a common data structure used in data analysis and manipulation.
#
# Below is an example of creating a DataFrame from a dictionary of lists.
# Each key in the dictionary represents a column name, and the corresponding value is a list of values for that column.

data = {
    "Age": [25, 30, 35, 40],
}
print(data)
df = pd.DataFrame(data)
print(df)


# Dataframes are useful for data analysis and manipulation tasks, such as filtering, grouping, and aggregating data.
# They also provide a convenient way to read and write data to and from various file formats, such as CSV, Excel, and SQL databases.
