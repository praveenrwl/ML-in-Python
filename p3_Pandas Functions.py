# Pandas Functions

import pandas as pd

iris = pd.read_csv('https://github.com/Muhd-Shahid/Write-Raw-File-into-Database-Server/raw/main/iris.csv',index_col=False)

# Mean Function :
print("\n# Mean Function :\n", iris.mean())

# Median Function :
print("\n# Median Function :\n", iris.median())

# Minimum Function :
print("\n# Minimum Function :\n", iris.min())

# Maximum Function :
print("\n# Maximum Function :\n", iris.max())


# Apply Function :
print("------------------------------------------------")
def double(s):
    return s*2
print("\n",iris.head())
print("\n# Apply Function :\n", iris[['sepal_width','petal_width']].apply(double))

# Value Counts Function :
print("\n# Value Counts Function :\n", iris['species'].value_counts())

# Sort Values Function :
print("\n# Sort Values Function :\n", iris.sort_values(by='petal_length'))