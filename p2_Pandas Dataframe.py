# Introduction to Pandas Dataframe :
'''A Dataframe is comprises of rows and columns'''
import csv
import pandas as pd


df1 = pd.DataFrame({'Name':['Jung','Bob','Ava'],'Marks':[97,83,89]})
print("# Dataframe :")
print(df1)

# Data-frame in-built functions :
# Head()
# iris = pd.read_csv('iris.csv')      #Over we can use any csv file
iris = pd.read_csv('https://github.com/Muhd-Shahid/Write-Raw-File-into-Database-Server/raw/main/iris.csv',index_col=False)
print("\n# Head Function :\n", iris.head())
# iris.head()

# Shape
print("\n# Shape Function :\n", iris.shape)

# Describe()
print("\n# Describe Function :\n", iris.describe())

# Tail()
print("\n# Tail Function :\n", iris.tail())

# iloc[] Function :
'''It help us to extract rows and columns with respect to their index'''
print("\n# ILOC[] Function :\n", iris.iloc[0:5,0:3])

# loc[] Function :
'''It help us to extract rows and columns with respect to their index and names'''
print("\n# LOC[] Function :\n", iris.loc[0:3, ('sepal_length','species')])

# Dropping Columns :
print("\n# Dropping Columns :\n", iris.drop('species',axis=1))

# Dropping Rows :
print("\n# Dropping Columns :\n", iris.drop([3,4,5],axis=0))



