import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.csv",names=col)
print("shape:",iris.shape)
print("*********")
print("First five rows")
print(iris.head())
print("*********")
print("Last five rows")
print(iris.tail())
print("*********")
print("Size:",iris.size)
print("*********")
print("no of samples available for each variety") 
print(iris["type"].value_counts())
print("*********")
