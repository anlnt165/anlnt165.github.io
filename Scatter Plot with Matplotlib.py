import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read files using pandas
df = pd.read_csv('iris.data') # read_csv can read any file types
df.to_csv("iris.csv", index = None) # Convert it to csv for easy access

# Accessing to columns and Rows
# Retrieving the names of the iris
iris_class = df.iloc[:,4].unique() # .iloc is for location of name. Unique is to get unique values

# Filter conditions to retrieve new data frame
def xy_val(dataFrame, class_name_col, iclass, data_type_col):
    # Create data frame for 1 class of iris
    iris_class1 = dataFrame[dataFrame.iloc[:,class_name_col] == iclass]
    # Get values for sepal width (y) and sepal length (x)
    x = iris_class1.iloc[:,data_type_col]
    y = iris_class1.iloc[:,data_type_col+1]
    return x, y

x1, y1 = xy_val(df,4,iris_class[0],0) # Data type col = 0 for sepal
x2, y2 = xy_val(df,4, iris_class[1],0)
x3, y3 = xy_val(df,4, iris_class[2],0)
plt.plot(x1,y1,'x', color='b')
plt.plot(x2,y2,'o', color = "m")
plt.plot(x3,y3, '+', color = 'g')
plt.xlabel('Sepal width (cm)')
plt.ylabel('Sepal length (cm)')
plt.title("Sepal data")
plt.show()

x4, y4 = xy_val(df,4,iris_class[0],2)
x5, y5 = xy_val(df,4,iris_class[1],2)
x6, y6 = xy_val(df,4,iris_class[2],2)
plt.plot(x4,y4,'x', color='b')
plt.plot(x5,y5,'o', color = "m")
plt.plot(x6,y6, '+', color = 'g')
plt.xlabel('Petal width (cm)')
plt.ylabel('Petal length (cm)')
plt.title("Petal data")
plt.show()
