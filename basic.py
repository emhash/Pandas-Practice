print("-------======>> Pandas Tutorials <<=======---------\n")
import numpy as np
import pandas as pd

data = {
    "total_bill":[16.99,10.34,21.01],
    "tip":[1.01,1.66,3.5,],
    "sex":['Female','Male','Male',],
    "smoker":['No','No','No',],
    "day":['Sun','Sun','Sun',],
    "time":['Dinner','Dinner','Dinner',],
    "size":[2,3,3],

}
the_dataframe = pd.DataFrame(data)

# 1 --> convert into csv
# the_dataframe.to_csv("data-csv.csv")

# 2 --> csv without index
# the_dataframe.to_csv('data_no_index.csv', index=False)

# 3 --> show few data i.e: first or last 3, 4 or 5 data
first_data = the_dataframe.head(2)
last_data = the_dataframe.tail(2)

# 4 --> description - used for summurize the numaric data or integer data
analysis = the_dataframe.describe()
# print(analysis)

# 5 --> reaad the csv file
new_data = pd.read_csv('demo.csv')
# new_df = pd.DataFrame(new_data)
# print(new_data.head(5))

# 6 --> specific data get like numpy
# new_data['crim'][1] = 0.504  #--> this will update the value but not a good way
print(new_data['crim'][1]) # --> 2nd index's colum crim's value
# 7 --> 
# 8 --> 



