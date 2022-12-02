#---------------------------------------------------------------NUMPY---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Numpy arrays are the main way we will use Numpy throughout the course
#Numpy arrays essentially come in two flavors: vectors and matrices
#Vector are strictly 1-D arrays and matrices are 2-D arrays or more

#Some of the important attributes of a ndarray are
#ndim : Returns number of dimensions.
#shape: Returns Shape in tuple.
#size : Total number of elements.
#dtype : Type of each element.
#itemsize : Size of each element in Bytes.
#nbytes : Total bytes consumed by all elements.

#pip install Numpy
from gettext import install
from unittest.mock import NonCallableMagicMock
import numpy as numpy

mylist = [1,2,3]
type(mylist)
mylist

arr = np.array(mylist)
type(arr)
arr # -> This is a 1D array

my_mat = ([1,2,3],[4,5,6],[7,8,9])
np.array(my_mat) #This is a 2D array. This is denoted by the number of open and closing square brackets. It contains 3 rows and 3 columns

#arange -> (start,stop,step)
np.arange(1,11) # -> This is a quick way to create an array. Similar to built in function 'range'
np.arange(1,21,2)

#zeros -> To generate arrays filled with zeros
np.zeros(3) #Single digit to get a 1D vector. array([0., 0., 0.])
np.zeros((5,5)) #You can also pass a tuple to state the dimensions you want. -> (rows,columns)

#ones -> To generate arrays filled with ones
np.ones(4) #Single digit to get a 1D vector.
np.ones((3,2)) #You can also pass a tuple to state the dimensions you want. -> (rows,columns)

#linspace -> (start,stop,number of spaced points between start-end you want)
np.linspace(0,10,5)

#identity matrix
np.eye(4)


#RANDOMS
#np.random.rand -> Brings back random samples from the UNIFORM DISTRIBUTION over 0 to 1.
np.random.rand(5) #Digit refers to the # of samples you want
np.random.rand(3,3) #Here, for 2D, you dont need to pass a tuple

#np.random.randn -> Returns samples from the STANDARD NORMAL DISTRIBUTION / GAUSSIAN
np.random.randn(2)
np.random.randn(4,4)

#np.random.randint -> Returns random integers from a low to a high number. (low-inclusive, high-exclusive, # of random integers you want)
np.random.randint(1,100,10)


#reshape method -> (rows,columns)
arr = np.arange(1,11)
#To make reshape work, you need to make sure that the number of rows and columns can be equaly distributed according to the lenght of your array
len(arr) #Array has 10 elements
arr.reshape(5,2) #We can split it this way
arr.reshape(5,3) #ValueError: cannot reshape array of size 10 into shape (5,3)


#More useful methods
randarr = np.random.randint(1,100,10)
randarr

randarr.max() #Will return the max value
randarr.argmax() #This will return the index of the max value

randarr.min()
randarr.argmin()

randarr.shape #shape method (without parenthesis) returns the shape of the array.
randarr.dtype #Return the type of your array


#arrays indexing, slicing and copy
arr = np.arange(0,11)
arr

arr_slice = arr[:6] #Here we sliced through arr and assigned the result to arr_slice
arr_slice
arr_slice[:] = 7 #Here we changed the values of arr_slice to 7
arr_slice

arr #When we print arr, the first six values are converted to 7, even if we did the change of arr_slice. This is because we didn't explicitly say we wanted a copy

#Let's do it again, but now, setting a copy
arr = np.arange(0,11)
arr_copy = arr.copy()
arr_copy[:6] = 7

arr #When printing, arr stays the same
arr_copy #When printing, the copy has the updated values we previously changed


#indexing, slicing in 2D arrays [starts on 0 : starts on 1]
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]]) #Uses double [] since it contains a lists inside a list
arr_2d
#Now, lets get the item '5'
arr_2d[0][0] #[row][column]
#Now, lets get the item '40'
arr_2d[2][1] #[2,1]
#Lets get the entire first row
arr_2d[0,:]
#Lets get the entire first column
arr_2d[:,0]
#Lets get 40 & 45
arr_2d[2,1:]
#Lets get 5 & 20
arr_2d[:2,0]
#Lets get [10,15]
#         [25,30]
arr_2d[:2,1:]


#Conditional selection
arr = np.arange(1,11)
arr
arr > 5 #This syntax (without []) will return boolean values -> array([False, False, False, False, False,  True,  True,  True,  True, True])
bool_array = arr > 5
arr[bool_array] #This syntax (with []) will return the actual values that fulfill the condition -> array([ 6,  7,  8,  9, 10])
arr[arr < 6] 

#Numpy operations
#array with array
#array with scalars
#universal array functions

import numpy as np
arr = np.arange(1,11)
arr
arr + arr
arr - arr
arr * arr
arr + 100
arr * 2
np.square(arr)
np.exp(arr)
np.max(arr) #same as arr.max()
np.min(arr) #same as arr.min()
np.sin(arr)
np.log(arr)
np.std(arr)


mat = np.arange(1,26).reshape(5,5)
mat
#Get the sum of the columns of mat
mat.sum(axis = 0)


#---------------------------------------------------------------PANDAS--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#PANDAS is built on top of Numpy
#Allows for fast analysis and data cleaning and preparation
#Excels in performance and productivity
#It also has built in visualization features
#It can work with data from a wide variaty of sources

#Series
#A series is similar to a nunpy array but what differentiates them if that a series can be indexed by labels
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
d = {'a':10, 'b':20, 'c':30}
arr = np.array(my_data)

#pd.Series(data,index)
pd.Series(my_data, labels) #This is how we create a series through variables
pd.Series(arr,labels) #We can also create a series passing in an array
pd.Series(d) #We can also create a series passing in a dictionary

ser1 = pd.Series([1,2,3,4],['USA','MX','ENG','AUS'])
ser1
ser2 = pd.Series([1,2,5,4],['USA','MX','GER','AUS'])
ser2

ser1['MX']


#DATAFRAMES (data, index: rows , columns)
from numpy.random import randn

np.random.seed(101) #Seed to get the same results
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df

#Selecting Columns
df['W'] #This is the way to bring a column
df[['W','Z']] #This is the way to bring more than one column [[]]

#Creating new columns
df['NEW'] = df['X'] + df['Z'] #df[name of the new column] = df[existing column] +-*/ df[existing column]
df
df.shape

#Removing columns
#If you want to keep the DF after removing some columns, you have to overwrite it, this is because df.drop() doesnt occur inplace
df.drop('NEW', axis = 1) #if you leave it by default, it will look for axis = 0 which is the index of the rows
df #Here we still have column 'NEW'

df = df.drop('NEW', axis = 1) #Here we overwrote the DF
df


#Selecting rows
df
df.loc['C'] #loc -> Label index
df.iloc[2] #iloc -> Numerical index 
df.loc[['A','B']]

#What if I want some specific rows and columns?
df.loc[['A','B'], ['Z','NEW']] # [ [rows],[columns] ]


#Removing rows
#since axis is set to 0 by default, we don't need to specify it
df.drop(['D','E'])


#------
np.random.seed(101) #Seed to get the same results
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

#Conditional selection
df
booldf = df > 0 #Returns booleans
df[df > 0] #NaN for False values

df['W'] > 0
df[df['W'] > 0] #This way will return the values of the rows that fulfill the condition in a DF format. Will also print the rest of the columns even if we chose 'W'
df[df['Z'] < 0]

#To get only the column we want:
df
resultdfW = df[df['W'] > 0]
resultdfW['W']

df[df['W'] > 0]['W'] #This is the same but writing it in one line
df[df['Z'] > 0][['Y','X']] #This is another example

#2 or more conditions
df[(df['W'] > 0) & (df['Y'] > 1)] #You have to use parenthesis and '&' or '|'
df[(df['W'] > 0) | (df['Y'] > 1)]

#Reset index
df
df = df.reset_index() #now 'index' is another columns and the actual indexes are numbers. Since this doesnt occur inplace, you have to overwrite.
df

#Set a index
#Lets first create the column we want to be our new index
new_ind = 'CA NY WY OR CO'.split()
new_ind
df['States'] = new_ind
df
#Now lets set it as the index
df.set_index('States') #This is not inplace


#DATAFRAMES
import numpy as np
import pandas as pd
from numpy.random import randn

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index

df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])
df 
df.loc['G1'] #Returns only the G1 index
df.loc['G1'].iloc[0] #Returns the first row of the G1 index

#We can also change the index names
df.index.names # -> FrozenList([None, None])
df.index.names = ['Groups', 'Numbers'] #Now, we set the indexes names
df

#                        A         B
# Groups Numbers                    
# G1     1       -0.099262 -0.488303
#        2        0.948244  0.074742
#        3       -0.190053 -2.091059
# G2     1       -0.306067 -0.872216
#        2        0.045822  0.828032
#        3       -1.344006 -0.000161

#Lets say we wanna grab the second value of the B columns inside the G2 group
df.loc['G2'].iloc[1]['B']

#When selecting in more complex ways, for example, selecting number 1 from group 1 and 2, we can use cross selection -> 'xs'
df.xs('G1') #Works just like the loc notation
df.xs(1, level = 'Numbers') #This will return our desired value


#MISSING DATA
d = {'A': [1,2,np.nan], 'B': [5,np.nan,np.nan], 'C': [1,2,3]}
d
df = pd.DataFrame(d)
df
#dropna() This method will delete EVERY ROW that at least contain one missing value
df.dropna()

#dropna(axis = 1) This will delete EVERY COLUMN that at least contain one missing value
df.dropna(axis = 1)

#df.dropna(thresh=2) -> this way will set a threshold for the rows to delete
df.dropna(thresh=2)

#df.fillna(value = )
df.fillna(value = 'Fill the value')

#Sometimes, you will want to fill the missing values of a column with its mean. So this is how we do it
df
df['A'].fillna(value = df['A'].mean())


#GROUP BY
#Group by allows you to group rows together based on a column to perform further aggregate functions on them
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
df

#Let's group by company and perform aggregate functions
#First you have to group by the column you want. After, you have to perform an aggregate function
df.groupby('Company').sum()
df.groupby('Company').count()
df.groupby('Company').max()
df.groupby('Company').min()

#If wanted, we can also filter by items inside the columns
df.groupby('Company').sum().loc['MSFT']

#We can also get the description of the columns in conjunction with group by
df.groupby('Company').describe()
df.groupby('Company').describe().loc['FB']
df.groupby('Company').describe().transpose()


#MERGE, JOIN AND CONCATENATE DATAFRAMES

#CONCATENATION
#Concatenation basically glues together DataFrames. Keep in mind that dimensions should match along the axis you are concatenating on. 
# You can use pd.concat and pass in a list of DataFrames to concatenate together:

df1 = pd.DataFrame(
    {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
    }, index=[0, 1, 2, 3])

df2 = pd.DataFrame(
    {
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
    }, index=[4, 5, 6, 7]) 

df3 = pd.DataFrame(
    {
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']
    },index=[8, 9, 10, 11])

df1
df2
df3

pd.concat([df1,df2,df3])


#MERGING
#The merge function allows you to merge DataFrames together using a similar logic as merging SQL Tables together. For example:

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']}) 

left
right

pd.merge(left,right, how='inner', on='key')

#JOINING
#Joining is a convenient method for combining the columns of two potentially differently-indexed DataFrames into a single result DataFrame.

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

left.join(right)
right.join(left)


#OPERATIONS

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df
df.head()
df.columns #Prints the columns DF had
df.index #Return the index features -> start, stop, step
df['col2'].unique() #Returns an array filled with the unique values
len(df['col2'].unique()) #Returns the actual number of unique values
df['col2'].nunique() #Returns the actual number of unique values but using pandas built in function .nunique()
df['col2'].value_counts() #Returns the number of times each unique value occured in the selected column.

#OPERATIONS -> SELECTING DATA

df['col1']>2 ##Returns in a BOOLEAN format the result of the columns for the described condition
df[df['col1']>2] #Returns the columns that fulfill the logical condition but in a DF format
df[(df['col1'] > 2) & (df['col3'] == 'ghi')] #Multiple conditions

#OPERATIONS -> APPLY METHOD
#When selecting columns on pandas, using apply you can broadcast a function to the column you previously selected.
#You can also implement it using built-in functions
#Apply is especial when using it with lambda functions

df

def times2(x):
    return x * 2

df['col1'].apply(times2) #This will multiply each element of col1 2 times
df['col3'].apply(len) #This will return the lenght of each element 
df['col2'].apply(lambda x: x * 2) #The benefit here is that we didn't have to write a previous function in order to get the desired calculation

#OPERATIONS -> REMOVE COLUMNS
#Remember to specify axis 1 since we are talking about columns, otherwise its gonna throw an error
#If we want the result to remain, don't forget to set the inplace parameter to True (inplace = True)

df
df.drop('col1')
df.drop('col1', axis = 1)

#OPERATIONS -> SORT VALUES
df
df.sort_values('col2')

#OPERATIONS -> FIND NULL VALUES

df
df.isnull() #This will return a DF with booleans indicating wether or not the value is null or not
df.isna() #This will return a DF with booleans indicating wether or not the value is NA or not

#OPERATIONS -> PIVOT TABLE

data = {
    'A':['foo','foo','foo','bar','bar','bar'],
    'B':['one','one','two','two','one','one'],
    'C':['x','y','x','y','x','y'],
    'D':[1,3,2,5,4,1]
}

df = pd.DataFrame(data)
df.pivot_table(values = 'D', index = ['A','B'], columns = 'C')


#DATA INPUT AND OUTPUT
#We can read CSV, Excel, HTML, SQL
#Keep in mind that as we reference the files, we need to make sure that files are at the same location when using Jupyter Notebook. 
# We can see the locations by calling pwd


#Go to DATA INPUT AND OUTPUT file on anaconda to review this section


#MATPLOTLIB
#When using this library in jupyter notebook you need to type '%matplotlib inline' so you can see the plots in the actual file
#When using text editor, you have to type 'plt.show()' at the end 

import numpy as np
import matplotlib.pyplot as plt

#FUNCTIONAL METHOD
x = np.linspace(0,5,11)
y = x ** 2

#One plot
plt.plot(x,y,'r')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Plot Title')

#Two plots
#Subplot(#rows, #columns, plot # you're referring to)
plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()


#OBJECT ORIENTED METHOD

#METHOD 1 (SINGLE PLOTS):
#1.CREATE THE FIGURE
#2.CREATE THE AXE/S AND ITS LOCATION (EACH AXE WILL DISPLAY ONE PLOT)
#3.SET THE INFORMATION THAT WILL BE PLOTTED IN THE AXE/S
#4.SET THE TITLE AND LABEL NAMES
x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure() #This basically create an empty canvas
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #add_axes takes in 4 arguments as a list (left, bottom, width and height) than range from 0 to 1
axes.plot(x,y)

axes.set_xlabel('x label')
axes.set_ylabel('y label')
axes.set_title('plot title')

plt.show()


#---------------------
x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y)
ax.set(title = 'plot title', xlabel = 'x label', ylabel = 'y label')
plt.show()


#A PLOT INSIDE ANOTHER PLOT
fig = plt.figure() 

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #This numbers makes reference to the line (left, bottom, width and height) and its position
axes2 = fig.add_axes([0.55, 0.15, 0.3, 0.2])

axes1.plot(x,y)
axes1.set_title('main plot')

axes2.plot(y,x)
axes2.set_title('subplot')

plt.show() 


#SUBPLOTS USING OO METHOD
#METHOD 2 (SUBPLOTS):
#1.CREATE THE FIGURE AND AXES (HERE YOU CAN DO TUPLE UNPACKING)
#2.ESPICIFY HOW MANY PLOTS YOU WANT
#3.SET THE INFORMATION THAT WILL BE PLOTTED IN THE AXE/S
#4.SET THE TITLE AND LABEL NAMES

#SUBPLOTS USING OO METHOD - ITERATING
x = np.linspace(0,5,11)
y = x ** 2

fig, axes = plt.subplots(nrows = 1, ncols = 2)

#When printing 'axes' we can se that its an array of 2 objects, it means we can iterate & index over them
axes # --> array([<AxesSubplot:>, <AxesSubplot:>], dtype=object)

for current_ax in axes:
    current_ax.plot(x,y)


plt.tight_layout() #To give space between plots
plt.show()


#SUBPLOTS USING OO METHOD - INDEXING
fig, axes = plt.subplots(nrows = 1, ncols = 2)

axes[0].plot(x,y)
axes[0].set_title('plot 1')
axes[0].set_xlabel('x label')
axes[0].set_ylabel('y label')

axes[1].plot(y,x)
axes[1].set_title('plot 2')
axes[1].set_xlabel('x label')
axes[1].set_ylabel('y label')

plt.tight_layout()
plt.show()


#FIGURE SIZE AND DPI (DOTS PER INCH)
x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure(figsize = (8,6))
ax = fig.add_axes([0.1,0.1,0.8,0.8]) 
ax.plot(x,y)
plt.show()


fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (6,4))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.show()

fig.savefig('my_plot.png') #This is how you can save a plot


#lEGENDS OF A PLOT
#This requires 2 steps: first add the label parameter into the ax.plot and then add ax.legend()
#To locate the legend box in the 'best' position, type the parameter 'loc = 0'
#If non of the locations codes suite your needs, you can also create one through a tuple
x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure(figsize = (8,6))
ax = fig.add_axes([0.1,0.1,0.8,0.8])

ax.plot(x,x**2, label = 'x squared')
ax.plot(x,x**3, label = 'x cubed')

ax.legend(loc = 0)

plt.show()


#PLOT APPEARANCE
#color: you can write the basic colors or RGB hex codes in case you want to be more specific
#linewidth (lw) & alpha: basically type the number of the width (1 is the default value). alpha refers to the transparency
#linestyle (ls): Lines can have different formats such as: --, -., :, steps, 
#marker, markersize, markerfacecolor, markeredgewidth, markeredgecolor: 
# Are going to be used when you have few data points and want to show them. ex: o, +, *, 1, 
x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

ax.plot(x,y, color = '#FF8C00', lw = 2.5, alpha = 0.5, label = 'Thick marked transparent line', marker = 'o', markersize = 10,
        markerfacecolor = 'purple', markeredgewidth = 3, markeredgecolor = 'black')
ax.plot(y,x, color = 'blue', lw = 1, label = 'Formatted line', ls = '-.')

ax.set_title('Plot Demonstration')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend(loc = 0)

plt.show()


#PLOT RANGE
#Using '.set_xlim' or '.set_xylim', you'll pass a LIST with the low and high boundaries
x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y, color = 'blue', lw = 2, ls = '--')

ax.set_xlim([0,1])
ax.set_ylim([0,2])

plt.show()


#PLOTTING MULTIPLE LINES
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

ax.set(title='Avg. Daily Temperature of Jan 2018',
      xlabel='Day', ylabel='Temperature (in deg)',
      xlim=(0, 30), ylim=(25, 35))

days = [1, 5, 8, 12, 15, 19, 22, 26, 29]
location1_temp = [29.3, 30.1, 30.4, 31.5, 32.3, 32.6, 31.8, 32.4, 32.7]
location2_temp = [26.4, 26.8, 26.1, 26.4, 27.5, 27.3, 26.9, 26.8, 27.0]

plt.plot(days, location1_temp, 'g^')
plt.plot(days, location2_temp, 'g-')

plt.show()


#SPECIAL PLOT TYPES
#Even if seaborn is better for statistical plotting, matplotlib allow you to create scatter plots, histograms, bar plots or box plots
x = np.linspace(0,5,11)
y = x ** 2

plt.scatter(x,y)
plt.show()

#SCATTER
#c: Sets color of markers.
#s: Sets size of markers.
#marker: Selects a marker. e.g: circle, triangle, etc
#edgecolor: Sets the color of lines on edges of markers.

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set(title='Avg. Daily Temperature of Jan 2018',
      xlabel='Day', ylabel='Temperature (in deg)',
      xlim=(0, 30), ylim=(25, 35))
days = [1, 5, 8, 12, 15, 19, 22, 26, 29]
temp = [29.3, 30.1, 30.4, 31.5, 32.3, 32.6, 31.8, 32.4, 32.7]
ax.scatter(days, temp, marker='o', c=['green'], s=[60], edgecolor='black')
plt.show()


from random import sample
data = sample(range(1,1000), 100)
plt.hist(data)
plt.show()

data = [np.random.normal(0, std, 100) for std in range(1,4)]
plt.boxplot(data, vert = True, patch_artist = True)
plt.show()


#SEABORN
#Is a statistical plotting library
#It has beatiful default styles
#Its designed to work vert well with pandas dataframe objects
#When using jupyter notebook, you also need to use %matplotlib inline
import seaborn as sns

#DISTRIBUTION PLOTS
#Let's load the 'tips' dataset
tips = sns.load_dataset('tips')
tips.head()

#dist_plot: allows you to show the distribution of a univariate set of observations (just one variable)
#kde: kernel density estimation is the sum of all the normal distributions
#bins: refers to the number of points/lines that will be displayed on the plot
sns.displot(tips['total_bill'], kde = True, bins = 40) #You just need to pass a single column
plt.show()

#joint_plot
#Allows you to basically match up 2 dist plots for bivariate data; meaning you can combine two different distribution plots
#kind parameter: allow us to choose the format of the central plot. ex: hex, reg, kde. The default value is scatter
sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex') # x and y are column names and data will be our dataset/dataframe
plt.show()


#pair_plot: allows you to plot pairwise relationships across an entire dataframe (for numerical columns)
#It also supports a color 'hue' argument for categorical columns.
#in the 'hue' parameter, you'll pass a CATEGORICAL column name (categorical = not numerical/continue)
#You can also format the plot with the 'palette' parameter
#Its a very nice way to quickly see/analize your data
sns.pairplot(tips, hue = 'sex', palette = 'pastel')
plt.show()


#rugplot: we'll use them to explain the KDE concept. You pass only one column
#It also shows the distribution of the column you want to display
sns.rugplot(tips['total_bill'])
plt.show()

sns.kdeplot(tips['total_bill'])
plt.show()


#CATEGORICAL PLOTS
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')
tips.head()

#barplot: by default will display the mean
#you can change the estimator (that contains an aggregate function) by typing the parameter
#'x' parameter has to be categorical and 'y' parameter has to be numerical
sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator = np.std) 
plt.show()

#countplot: here the estimator is explicitly using 'count' agg function
#you only pass 'x' and 'data' parameter 
sns.countplot(x = 'sex', data = tips)
plt.show()

#box/whisker plots and violin plots
#These plots are used to show the distribution of categorical data 

#A box and whisker plot—also called a box plot—displays the five-number summary of a set of data.
#The five-number summary is the minimum, first quartile, median, third quartile, and maximum.
#In a box plot, we draw a box from the first quartile to the third quartile. A vertical line goes through the box at the median. 
# The whiskers go from each quartile to the minimum or maximum.
#The points outside the whiskers are outliers
#The line inside the box represent the 'median'
#You can also add the 'hue' parameter to add a new layer of information
sns.boxplot(x = 'day', y = 'total_bill', data = tips, hue = 'smoker')
plt.show()

#MORE ADVANCED PLOTS:

#The violin plot, allow us to actually plot all the components that correspond to actual data points and it's essentially
# showing the KDE of the underlying distribution
sns.violinplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex', split = True)
plt.show()


#stripplot: is going to draw a scatter plot where one variable is categorical 
#Since with this kind of plot you cant really tell how many dots are stacked on each other, you can use 'jitter' parameter
#jitter: is going to add a little bit of noise to separate some of these stacked points so it will be clearer
sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True, hue = 'sex', split = True)
plt.show()


#swarmplot: Its very similar to a stripplot except that the points are adjusted so they don't overlap. This brings a better
# representation of the distribution of values
#This type of plot is not recommended for very large data sets since it tries to display all points of data
sns.swarmplot(x = 'day', y = 'total_bill', data = tips)
plt.show()


#factorplot: the 'kind' argument is what the plot is going to look like. It's another way to call the plots 
sns.factorplot(x = 'day', y = 'total_bill', data = tips, kind = 'bar')
plt.show()


#MATRIX PLOTS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
flights.head()

#HEAT MAPS
#In order for you heat map to work correctly, the information should already be in a matrix form
#Matrix form -> index name and column name match up so that the cell value indicates something relevant to both of those names
#We can get this matrix form through a correlation table or pivot table
#annot argument will display the numerical value that belong to each of the cells
#'cmap' argument will let you modify the color of the plot
#'linecolor' and 'linewidths' arguments are to give format

tc = tips.corr()
sns.heatmap(tc, annot = True, cmap = 'coolwarm')
plt.show()

#Now let's get the matrix form through a pivot table
#It need 3 arguments: index, columns and values
fp = flights.pivot_table(index = 'month', columns = 'year', values = 'passengers')
sns.heatmap(fp, cmap = 'magma', linecolor = 'white', linewidths = 1)
plt.show()


#CLUSTER MAP
#Cluster map is going to use hierarchal clustering to produce a clustered version of a heat map
#The result will be a clustered heat map showing the values that are similar to each other in the same clusters
#To get even more insights from this plot, we can also change the color and standardize the values (normalize)
fp = flights.pivot_table(index = 'month', columns = 'year', values = 'passengers')
sns.clustermap(fp, cmap = 'coolwarm', standard_scale = 1)
plt.show()


#GRIDS
iris = sns.load_dataset('iris')
iris.head()
iris['species'].unique()

#'PairGrid' takes all the numerical columns and grids them up 
# The main way to use it is by setting the PairGrid into a variable and then map the type of plot you want to use
#We can specify the type of plot we wanna use on the grids by using 'map_diag()', 'map_upper()', or 'map_lower()'
#This way, we can customize our plots
g = sns.PairGrid(iris)
g.map_diag(sns.displot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
plt.show()


#'FacetGrid'
#Just like PairGrid, but here we can separate through columns and rows and when mapping, we choose the type of plot
#FacetGrid arguments: data, col and row
#When mapping, you pass the plot arguments after you choose the plot type
tips = sns.load_dataset('tips')
tips.head()

g = sns.FacetGrid(data = tips, col = 'time', row = 'smoker')
g.map(sns.displot, 'total_bill')
plt.show()

g = sns.FacetGrid(data = tips, col = 'time', row = 'smoker')
g.map(sns.scatterplot, 'total_bill','tip')
plt.show()


#REGRESSION PLOTS
#LM plots allow you to display linear models with seaborn
#Since this will print a scatter plot, you'll need your x vs y variable
#Here you can pass in matplotlib style parameters
#If you want to change the size of the markers, in this case, since its a scatter plot, we'll use the argument
# 'scatter_kws' and pass in a dictionary
#We can change the aspect ratio and size
tips = sns.load_dataset('tips')
tips.head()

sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', markers = ['o','v'], scatter_kws = {'s': 50}) # s -> size
plt.show()

#Also, instead of using hue to separate from sex, we can use grids by calling 'col'
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, col = 'day', hue = 'sex', aspect = 0.6, size = 6)
sns.set_style('darkgrid')
plt.show()


#STYLE AND COLOR
#plt.figure(figsize = ( , )) -> to change the size
#sns.set_style() -> to change the elements inside the plot
#sns.despine() -> to show/not show the axis lines
#sns.set_context() -> to change the format


tips = sns.load_dataset('tips')
tips.head()

plt.figure(figsize = (12,4))
sns.countplot(x = 'sex', data = tips)
sns.set_style('ticks')
sns.despine(left = True, bottom = True)
sns.set_context('notebook', font_scale = 1)
plt.show()

#https://matplotlib.org/stable/gallery/color/colormap_reference.html ---> palettes and colors
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', palette = 'Wistia')
plt.show()


#-------------------------------------------------------------------------------------------------------
#PANDAS BUILT IN DATA VISUALIZATION
#This type of visualization works for quick views (lineplots or histograms)
#IF you want more personalized plots, better use seaborn or matplotlib methods

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#df1 is a time series
df1 = pd.read_csv('/Users/alexisvargas/Documentos/Data Science/Bootcamps files/df1.csv', index_col = 0) #Time series
df1.head()
df1.tail()

#df2 is just a collection of information
df2 = pd.read_csv('/Users/alexisvargas/Documentos/Data Science/Bootcamps files/df2.csv') #Non time series with sequential index
df2.head()

#There's different ways to create a histogram using the pandas built in visualization tools
df1['A'].hist(bins = 30)
plt.show()

df1['A'].plot(kind = 'hist', bins = 30)
plt.show()

df1['A'].plot.hist(bins = 30) #Method to use in this lesson
plt.show()

df1['A'].plot.hist() #Method to use in this lesson
plt.show()

df2.head()
#AREA
df2.plot.area(alpha = 0.4)
plt.show()

#BAR
df2.plot.bar()
plt.show()

df2.plot.bar(stacked = True)
plt.show()

#LINE
df1.plot.line(x = df1.index, y = 'B', figsize = (12,3), lw = 1)
plt.show()

#SCATTER
df1.plot.scatter(x = 'A', y = 'B')
plt.show()

#We can read the third argument as A vs B and the size/color indicates how large their 'C' value was
df1.plot.scatter(x = 'A', y = 'B', c = 'C', s = df1['C']*50) #You can add another level with 'c' -> color
plt.show()

df1.plot.scatter(x = 'A', y = 'B', s = df1['C']*50) #You can add another level with 's' -> size
plt.show()

#BOXPLOT
df2.plot.box()
plt.show()

#For BIVARIATE data (2 variables)
df = pd.DataFrame(np.random.randn(1000,2), columns = ['a','b'])
df.head()

df.plot.hexbin(x = 'a', y = 'b', gridsize = 25) #gridsize -> number of hex's that will be displayed
plt.show()

#KDE
#You can call all or just one column of your data frame
df2['a'].plot.kde()
plt.show()

df2.plot.kde()
plt.show()


#Geographical plotting and plotly lessons will be available in the jupyter notebook 'pyplot_session' file
#PLOTLY AND CUFFLINKS - FOR INTERACTIVE VISUALIZATIONS
