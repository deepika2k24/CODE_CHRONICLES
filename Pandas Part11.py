#!/usr/bin/env python
# coding: utf-8

# ## Data Manipulation with Pandas

# Pandas is a newer package built on top of NumPy, and provides an
# efficient implementation of a DataFrame. DataFrames are essentially multidimensional
# arrays with attached row and column labels, and often with heterogeneous types
# and/or missing data. As well as offering a convenient storage interface for
# labeled data, Pandas implements a number of powerful data 
# operations familiar to users of both database frameworks and spreadsheet programs.
# Pandas, and in particular its <b> Series and DataFrame objects </b>, 
# builds on the NumPy array structure and provides efficient access to messy data 
# and helps in “data munging” tasks that occupy much of a data scientist’s time.

# In[51]:


import numpy as np
import pandas as pd  # pandas : panel data , python data analysis


# In[52]:


pd.__version__


# ###### The Pandas Series Object
# A Pandas Series is a one-dimensional array of indexed data. It can be created from a
# list or array as follows:

# %%
import pandas as pd
# %%
data = pd.Series([0.25, 0.5, 0.75, 1.0])


# In[54]:


data.values


# In[55]:


data.index


# In[56]:


data[1]


# In[57]:


data[1:4]


# In[58]:


"""Pandas Series is much more general and flexible than the one-dimensional NumPy array that it emulates
The essential difference is the presence of the index: while the NumPy array has an implicitly defined integer 
index used to access the values, the Pandas Series has an explicitly defined index associated with the values."""
# pd.Series(data, index=index) where index is an optional argument, and data can be one of many entities.
data = pd.Series([0.25, 0.5, 0.75, 1.0],index=['a', 'b', 'c', 'd'])
data


# In[59]:


data['c']


# In[60]:


'a' in data


# In[61]:


data.keys()


# In[62]:


list(data.items())


# In[63]:


data['a':'c']


# In[64]:


# slicing by implicit integer index
data[0:2]


# In[65]:


# masking
data[(data > 0.3) & (data < 0.8)]


# In[66]:


# fancy indexing
data[['a', 'd']] # passing an array of indices to access multiple array elements at once


# In[67]:


#noncontiguous indices
data = pd.Series([0.25, 0.5, 0.75, 1.0],index=[2, 5, 3, 7])
data


# In[68]:


#Series as specialized dictionary
population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}
population = pd.Series(population_dict)
population


# In[69]:


#Unlike a dictionary the Series also supports array-style operations such as slicing
population['California':'New York']


# In[70]:


#Data can be a scalar, which is repeated to fill the specified index:
data = pd.Series(5,index=[100,200,300])
data


# In[71]:


#Data can be a dictionary
data = pd.Series({2:'a', 1:'b', 3:'c'})
data


# In[72]:


data[1:3]


# In[73]:


#The index can be explicitly set if a different result is preferred:
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2]) #Series is populated only with the explicitly identified keys


# ###### The Pandas DataFrame Object
# If a Series is an analog of a one-dimensional array with flexible indices, a DataFrame is an analog of a two-dimensional array with both flexible row indices and flexible column names.

# In[74]:


area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
'Florida': 170312, 'Illinois': 149995}


# In[75]:


area = pd.Series(area_dict)
area


# In[76]:


states = pd.DataFrame({'population': population,'area': area})
states


# In[77]:


states.index


# In[78]:


states.values


# In[79]:


states.columns


# ###### DataFrame as specialized dictionary

# In[80]:


#dictionary-style access
states['population']


# In[81]:


#Equivalently, we can use attribute-style access with column names that are strings:
states.population


# In[82]:


#This attribute-style column access actually accesses the exact same object as the dictionary-style access:
states['population'] is states.population


# In[83]:


states.rename(columns={'population': 'pop'}, inplace=True)
states


# In[84]:


#the DataFrame has a pop() method, so data.pop will point to this rather than the "pop" column:
states.pop is states['pop']


# In[85]:


#introduce new column better to use dictionary style
states['density'] = states['pop'] /states['area']
states


# In[86]:


pd.DataFrame(states)


# In[87]:


df=pd.DataFrame(states,columns=['pop'])
df


# In[88]:


df.dtypes


# ###### From list of dict

# In[89]:


data = [{'a': i, 'b': 2 * i}for i in range(3)]
pd.DataFrame(data)


# In[90]:


pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])


# In[91]:


#Constructing DataFrame from a dictionary.
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df


# In[92]:


df.dtypes


# In[93]:


df = pd.DataFrame(data=d,dtype='int8')
df


# In[94]:


df.dtypes


# In[95]:


#From a two-dimensional NumPy array.
"""Given a two-dimensional array of data, we can create a DataFrame with any specified column and index names. 
If omitted, an integer index will be used for each:"""
pd.DataFrame(np.random.rand(3, 2),columns=['foo', 'bar'],index=['a', 'b', 'c'])


# In[96]:


#From a NumPy structured array.
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
A


# In[ ]:





# In[97]:


pd.DataFrame(A)


# In[98]:


A.dtype


# ###### Indexers loc and iloc 

# In[99]:


data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data


# In[100]:


# explicit index when indexing
data[1]


# In[101]:


# implicit index when slicing
data[1:3]


# In[102]:


data.iloc[1]


# Because of this potential confusion in the case of integer indexes, Pandas provides some special indexer 
# attributes that explicitly expose certain indexing schemes. These are not functional methods, 
# but attributes that expose a particular slicing interface to the data in the Series.

# In[103]:


# First, the loc attribute allows indexing and slicing that always references the explicit index:
data.loc[1]


# In[104]:


data.loc[1:3]


# In[105]:


#The iloc attribute allows indexing and slicing that always references the implicit Python-style index
data.iloc[1]


# In[106]:


data.iloc[1:3]


# ###### DataFrame as two-dimensional array

# In[107]:


states


# In[108]:


states.values


# In[109]:


states.area


# In[110]:


states.iloc[:3,:2]


# In[111]:


states.loc[:'Illinois', :'pop']


# In[112]:


states['density']= states['pop']/states['area']
states


# In[113]:


#In the loc indexer we can combine masking and fancy indexing
states.loc[states.density > 100, ['pop', 'density']]


# In[114]:


#indexing  may also be used to set or modify values
states.iloc[0, 2] = 90
states


# In[115]:


#First, while indexing refers to columns, slicing refers to rows:
states['Florida':'Illinois']


# In[116]:


#Such slices can also refer to rows by number rather than by index:
states[3:5]


# In[117]:


#direct masking operations are also interpreted row-wise rather than column-wise:
states[states.density > 100]


# ###### Handling Missing Data
# Pandas chose to use sentinels for missing data, and further chose to use two already-existing <b>Python null values: the special floatingpoint NaN (Not a Number) value, and the Python None object</b>. 
# 
# <b>None: Pythonic missing data</b>
# The first sentinel value used by Pandas is None, a Python singleton object that is often used for missing data in Python code. Because None is a Python object, it cannot be used in any arbitrary NumPy/Pandas array, but only in arrays with data type 'object' (i.e., arrays of Python objects

# In[118]:


vals1 = np.array([1, None, 3, 4])
vals1


# In[119]:


# amount of overhead to handle object type
for dtype in ['object', 'int']:
    print("dtype =", dtype)
    get_ipython().run_line_magic('timeit', 'np.arange(1E6, dtype=dtype).sum()')
    print()


# In[120]:


#The use of Python objects in an array also means that if you perform aggregations
#like sum() or min() across an array with a None value, you will generally get an error:
vals1.sum()


# ###### NaN: Missing numerical data

# In[ ]:


#it is a special floating-point value recognized by all systems that use the standard IEEE floating-point representation:
vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype


# In[ ]:


1 + np.nan


# In[ ]:


vals2.sum(), vals2.min(), vals2.max()


# In[ ]:


np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)


# In[ ]:


#NaN and None in Pandas
pd.Series([1, np.nan, 2, None])


# In[ ]:


x = pd.Series(range(2), dtype=int)
x


# In[ ]:


x[0]=np.nan
x


# ###### Pandas handling of NAs by type
# <pre><b>Typeclass           Conversion when storing NAs          NA sentinel value  </b>
#    floating             No change                           np.nan
#    object               No change                           None or np.nan
#    integer              Cast to float64                     np.nan
#    boolean              Cast to object                      None or np.nan  </pre>

# ###### Operating on Null Values

# ###### Detecting null values
# Pandas data structures have two useful methods for detecting null data: <b> isnull() and notnull()</b>. Either one will return a Boolean mask over the data. For example:

# In[ ]:


data = pd.Series([1, np.nan, 'hello', None])


# In[ ]:


data.notnull().any()


# In[ ]:


#Boolean masks can be used directly as a Series or DataFrame index:
data[data.notnull()]


# ###### Dropping null values
# In addition to the masking used before, there are the convenience methods, <b>dropna()(which removes NA values) and fillna()</b> (which fills in NA values).

# In[ ]:


data.dropna(ignore_index=True)


# In[122]:


df = pd.DataFrame([[1, np.nan, 2],
                   [2, 3, 5],
                   [np.nan, 4, 6]],
                  columns=['A','B','C'])
df


# In[ ]:


df.dropna()


# In[ ]:


df.dropna(axis=1) #or axis='columns'


# In[ ]:


#set a column with all null values
df['D'] = np.nan
df


# In[ ]:


#to drop all null values column
df.dropna(axis=1,how='all')


# In[ ]:


df


# In[ ]:


"""thresh parameter lets you specify a minimum number of 
non-null values for the row/column to be kept:
Here the first and last row have been dropped, because 
they contain only two nonnull values."""
df.dropna(axis='columns', thresh=2)


# ###### Filling null values

# In[ ]:


data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data


# In[ ]:


#We can fill NA entries with a single value, such as zero:
data.fillna(0)


# In[ ]:


#We can specify a forward-fill to propagate the previous value forward
data.fillna(method='ffill')


# In[ ]:


#Or we can specify a back-fill to propagate the next values backward:
data.fillna(method='bfill')


# In[123]:


#For DataFrame
df


# In[127]:


df.fillna(method='ffill', axis=1)


# In[128]:


df


# In[129]:


df.fillna(method='bfill', axis=1)


# ###### Hierarchical(multi) Indexing

# In[130]:


#Bad way
index = [('California', 2000), ('California', 2010),('New York', 2000), ('New York', 2010),
('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,18976457, 19378102,20851820, 25145561]
pop = pd.Series(populations, index=index)
pop


# In[131]:


pop[('California', 2010):('Texas', 2000)]


# In[132]:


"""But the convenience ends there. For example, if you need to select all values from 2010, you’ll need to do some messy (and potentially slow) munging to make it
happen:"""
pop[[i for i in pop.index if i[1] == 2010]]


# In[133]:


#The better way: Pandas MultiIndex
index = pd.MultiIndex.from_tuples(index)
index


# In[134]:


"""Here the first two columns of the Series representation show the multiple index values,
while the third column shows the data. Notice that some entries are missing in
the first column: in this multi-index representation, any blank entry indicates the
same value as the line above it"""
pop = pop.reindex(index)
pop


# In[135]:


#to access all data for which the second index is 2010, we can simply use the Pandas slicing notation:
pop[:, 2010]


# ###### MultiIndex as extra dimension

# In[136]:


pop_df = pop.unstack()
pop_df


# In[137]:


pop_df.stack()


# In[138]:


"""we might want to add another column of demographic data for each state at each year
(say, population under 18); with a MultiIndex this is as easy as adding another column to the DataFrame:"""
pop_df = pd.DataFrame({'total': pop,'under18': [9267089, 9284094,4687374, 4318033,5906301, 6879014]})
pop_df


# In[140]:


#we compute the fraction of people under 18 by year, given the above data
f_u18 = pop_df['under18'] / pop_df['total']
f_u18.unstack()


# ###### MultiIndex level names

# In[141]:


pop_df.index.names = ['state', 'year']
pop_df


# ###### MultiIndex for columns

# In[142]:


# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
names=['subject', 'type'])
# mock some data
data = np.round(np.random.randn(4, 6), 1)
print(data)
data[:, ::2] *= 10
print(data)
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data


# In[143]:


health_data['Guido']


# ###### Index setting and resetting

# In[144]:


pop


# In[146]:


pop_flat = pop.reset_index(name='population')
pop_flat


# In[147]:


pop_multi=pop_flat.set_index(['state', 'year'])
pop_multi


# ###### Data Aggregations on Multi-Indices

# In[148]:


health_data


# In[149]:


health_data.mean(axis='columns')


# In[150]:


health_data.mean(axis='rows')


# ###### Recall: Concatenation of NumPy Arrays

# In[153]:


"""x = [[1], [2], [3]]
y = [[4], [5], [6]]
z = [[7], [8], [9]]"""
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])


# In[155]:


x = [[1, 2],[3, 4]]
np.concatenate([x, x])


# In[ ]:




