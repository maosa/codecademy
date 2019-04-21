"""
A huge part of data science involves acquiring raw data and getting it into a form ready for analysis. Some have estimated that data scientists spend 80% of their time cleaning and manipulating data, and only 20% of their time actually analyzing it or building models from it.

We have provided an example of data representing exam scores from 1000 students in an online math class.

These DataFrames are hard to work with. They’re separated into multiple tables, and the values don’t lend themselves well to analysis. Try to think about how you would plot the exam score average against the age of the students in the class. This would not be easy!

In the next exercises, we’ll transform this data so that performing a task like that visualization would be simple.

Data diagnosing functions:

.head() — display the first 5 rows of the table
.info() — display a summary of the table
.describe() — display the summary statistics of the table
.columns — display the column names of the table
.value_counts() — display the distinct values for a column

We can combine the use of glob, a Python library for working with files, with pandas to organize this data better. glob can open multiple files by using regex matching to get the filenames.d
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import glob

"""
Could use the lines below to open all the required csv files

students0 = pd.read_csv('~/Desktop/programming/codecademy/python/basics/file0.csv')
students1 = pd.read_csv('~/Desktop/programming/codecademy/python/basics/file1.csv')
students2 = pd.read_csv('~/Desktop/programming/codecademy/python/basics/file2.csv')
students3 = pd.read_csv('~/Desktop/programming/codecademy/python/basics/file3.csv')......

OR USE GLOB

student_files = glob.glob('exams[0-9].csv')

df_list = []

for file in student_files:
  df = pd.read_csv(file)
  df_list.append(df)

students = pd.concat(df_list)
"""

#####

"""
Using pd.melt() arguments:

frame: the DataFrame you want to melt
id_vars: the column(s) of the old DataFrame to preserve
value_vars: the column(s) of the old DataFrame that you want to turn into variables
value_name: what to call the column of the new DataFrame that stores the values
var_name: what to call the column of the new DataFrame that stores the variables
"""

#####

##########################
#####DATA CLEANING PROJECT

# states0 = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/basics/data_cleaning_project/states0.csv')
# print(states0.head())
# print(states0.dtypes)

##### It would be easier to read all dataframes using glob
states = glob.glob('/Users/maosa/Desktop/programming/codecademy/python/basics/data_cleaning_project/states[0-9].csv')

all_states = []
for state in states:
  data = pd.read_csv(state)
  all_states.append(data)

us_census = pd.concat(all_states)

print("\nNUMBER OF STATES: " + str(us_census.State.nunique()) + "\n")

# print(us_census.head())
# print(us_census.dtypes)

us_census.Income = us_census.Income.replace('[\$,]', '', regex=True)
us_census.Income = pd.to_numeric(us_census.Income)
us_census.Income = us_census.Income.round(2)

# print(us_census.head())
# print(us_census.dtypes)

GenderPop_split = us_census.GenderPop.str.split('_')
# print(GenderPop_split.head())

us_census['Men'] = GenderPop_split.str.get(0)
us_census.Men = us_census.Men.replace('[M]', '', regex=True)
us_census.Men = pd.to_numeric(us_census.Men)

us_census['Women'] = GenderPop_split.str.get(1)
us_census.Women = us_census.Women.replace('[F]', '', regex=True)
us_census.Women = pd.to_numeric(us_census.Women)

##### Remove GenderPop column
us_census.drop(['GenderPop', 'Unnamed: 0'], axis=1, inplace=True)

##### Check for NaN values
# print(us_census.Women)

##### Could drop NaN values but it is best to replace them with something else
# print(len(us_census))
# us_census = us_census.dropna(subset=['Women'])
# print(len(us_census))

us_census = us_census.fillna(value={'Women' : us_census.TotalPop - us_census.Men})

##### NaN values have been removed
# print(us_census.Women)

##### Find duplicated rowsand remove them
# print(us_census.duplicated())
us_census = us_census.drop_duplicates()

##### Plot some data
# pyplot.scatter(us_census.Women, us_census.Men)
# pyplot.show()

# print(us_census.head())
print('\nCOLUMN NAMES: ' + str(us_census.columns) + '\n')

##### Modify the columns containing race information
##### Remove percentage sign
##### Convert values to numeric

for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    us_census[race] = us_census[race].replace('[\%,]', '', regex=True) ### remove % sign
    us_census[race] = pd.to_numeric(us_census[race]) ### convert string values to numeric
    us_census[race] = us_census[race]/100 ### get race proportion in the total population
    # us_census[race] = us_census[race]*us_census.TotalPop ### get race population
    us_census[race] = us_census[race].round(3)

print(us_census.dtypes)
print('\n')
print(us_census.head())
# print(us_census[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']].head())
