import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)

t = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(t['b'])

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["London", "Paris", "Berlin"]
}

df = pd.DataFrame(data)
print(df)

df1 = pd.read_csv("data.csv")
print(df1)

df1.to_csv("output.csv", index=False)

# df.head()        # first 5 rows
# df.tail(3)       # last 3 rows
# df.info()        # data types and non-null values
# df.describe()    # quick stats for numeric columns

df["Name"]               # select one column
df[["Name", "City"]]     # select multiple columns
df.iloc[0]               # select first row (by position)
df.loc[1, "City"]        # select specific value (by label)
