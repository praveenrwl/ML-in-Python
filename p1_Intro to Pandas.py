# Introduction of Python Pandas

'''Pandas stands for Panel Data and is the core library of
data manipulation and data analysis. '''
'''It consists of single and multi-dimensional data structures for 
data manipulation. '''

# Single Dimensional Data-Structures :
'''Series Object'''
# Multi Dimensional Data-Structures :
'''Data-frame'''

# Pandas Series Object :
import pandas as pd
p1 = pd.Series([1,2,3,4,5])

print("Pandas Series Object :\n", p1)
print("Type:",type(p1))


p2 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print("\nPandas Series Object Changing Index :\n", p2)

p3 = pd.Series({'apple':1,'ball':2,'cat':3})
print("\nPandas Series Object from Dictionary :\n", p3)

p4 = pd.Series({'a':10,'b':20,'c':30}, index=['c','a','b','d'])
print("\nPandas Series Object Changing Index Position :\n", p4)

# Extracting a single element :
p5 = pd.Series([1,2,3,4,5,6,7,8,9])
print("\n# Extracting a single element :\n", p5[6])

# Extracting elements from back :
p6 = pd.Series([1,2,3,4,5,6,7])
print("\n# Extracting elements from back :\n", p6[-3:])

# Extracting a sequence of elements :
p7 = pd.Series([1,2,3,4,5,6])
print("\n# Extracting a sequence of elements :\n", p7[:4])

# Basic Math Operations on Series :
# Adding a scalar value to Series Elements :
p8 = pd.Series([10,20,30,40,50])
print("\n# Adding a scalar value to Series Elements :\n", p8+5)

# Adding two Series Object :
p9 = pd.Series([10,20,30,40,50])
p10 = pd.Series([11,12,13,14,15])
print("\n# Adding two Series Object :\n", p9 + p10)