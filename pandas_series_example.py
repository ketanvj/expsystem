import pandas as pd


a = [1, 7, 2]
# A Pandas Series is like a column in a table.
myvar = pd.Series(a)

print(myvar)
print(type(myvar))
# Labeled series
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Accessing a particular entry
print(myvar["y"])


#Key/Value Objects as Series
# Create a simple Pandas Series from a dictionary:
# Keys of the dict becomes labels
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


# To select only some of the items in the dictionary,
# use the index argument and specify only the items you want to include in the Series.

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

