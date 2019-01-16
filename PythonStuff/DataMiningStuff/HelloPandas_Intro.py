#This programs shows how to create and manipulate arrays of data using Pandas data frames
#Also includes many helpful commands in comments 




import pandas as pd
import numpy as np

my_dict = {'name' : ['a','b','c','d','e','f','g'],
            'age' : [20,21,23,45,34,56,32],
            'designation' : ['IN','BM','RM','CTO','CFO','VP','CEO']}


df = pd.DataFrame(my_dict)

df = pd.DataFrame(my_dict, index=[1,2,3,4,5,6,7]) #changes index of dataframe. Can use [first, second, third...]

np_arr = np.array([10,20,30,40,50,60,70])

df = pd.DataFrame(my_dict, index=np_arr) # changes index values to numpy array values

#the funtion df.[object].dtype checks the data type of the element
#df.head, df.tail gives top 5 and bottom 5 rows of dataframe respectively
#also df.head(2) gives first 2 rows...works same for example df.tail(2)
#df.index - gives index & df.columns - gives columns
#df.designation.unique() - gives unique designations (objects)
#df.age.mean() - gives mean age (numbers)
#df.set_index("age") - sets default index to age
#df.set_index("age", "name") - sets default combination of index objects
#df = pd.DataFrame(my_dict, columns=["name","age"]) - gives columns selected only
#df('name') - deletes name column from Dataframe
#df.drop('age', 1) - deletes row 1 of age column from Dataframe
#df.drop(3,0) - deletes row 3
#df.drop(['name','age'], 1) - drops name and age column
#df.drop([2,3,4],0) - drops rows 2,3,and 4
#df.drop(df.columns[[0,1]],1) - drops first 2 columns

my_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
#df = pd.DataFrame(my_list)

np_arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
#df = pd.DataFrame(np_arr)
#df * df - self multiplication of array
#newdf = df*13 - creates new df array as multiple df by 13
#df+100 - adds 100 to elements
#df&0 - sets elements to 0



