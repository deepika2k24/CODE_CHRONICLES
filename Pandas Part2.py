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

# In[1]:


import pandas as pd  # pandas : panel data , python data analysis


# ###### Pandas concatenate

# In[2]:


#pd.concat() can be used for a simple concatenation of 
# Series or DataFrame objects,
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
print(ser1)
print(ser2)
pd.concat([ser1, ser2],axis=1)


# In[3]:


def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c:[str(c) + str(i) for i in ind] for c in cols}
    print(data)
    return pd.DataFrame(data, ind)


# In[4]:


df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
print(df1); print(df2); print(pd.concat([df1, df2],axis=1))


# In[5]:


"""By default, the concatenation takes place row-wise within the DataFrame 
(i.e.,axis=0). Like np.concatenate, pd.concat allows specification 
of an axis along which concatenation will take place."""
df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
print(df3); print(df4); print(pd.concat([df3, df4],axis=1))


# ###### Duplicate indices

# In[6]:


"""One important difference between np.concatenate and pd.concat is that Pandas
concatenation preserves indices, even if the result will have duplicate indices!
Consider this simple example:"""
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index # make duplicate indices!
print(x); print(y); print(pd.concat([x, y]))


# ###### Caching the error

# In[7]:


"""Catching the repeats as an error. If you’d like to simply verify that the indices in the
result of pd.concat() do not overlap, you can specify the verify_integrity flag.
With this set to True, the concatenation will raise an exception if there are duplicate
indices. Here is an example, where for clarity we’ll catch and print the error message:"""
try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print("ValueError:", e)


# ###### Ignoring the Index

# In[8]:


"""Sometimes the index itself does not matter, and you would prefer
it to simply be ignored. You can specify this option using the ignore_index flag. With
this set to True, the concatenation will create a new integer index for the resulting
Series:"""
print(x); print(y); print(pd.concat([x, y], ignore_index=True))


# ###### Adding MultiIndex keys

# In[9]:


print(x); print(y); print(pd.concat([x, y], keys=['x', 'y']))


# In[10]:


"""Concatenation with joins
In the simple examples we just looked at, we were mainly concatenating DataFrames
with shared column names. In practice, data from different sources might have different
sets of column names, and pd.concat offers several options in this case. Consider
the concatenation of the following two DataFrames, which have some (but not all!)
columns in common:"""
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
print(df5); print(df6); print(pd.concat([df5, df6]))


# In[11]:


print(df5); print(df6);
print(pd.concat([df5, df6], join='inner'))


# ###### Combining Datasets: Merge and Join
# One essential feature offered by Pandas is its high-performance, <b> in-memory join and
# merge operations</b>. If you have ever worked with databases, you should be familiar
# with this type of data interaction. The main interface for this is the pd.merge function,

# In[12]:


#Categories of Join
"""The pd.merge() function implements a number of types of joins: the one-to-one,
many-to-one, and many-to-many joins. All three types of joins are accessed via an
identical call to the pd.merge() interface; the type of join performed depends on the
form of the input data."""
#One-to-one joins
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
print(df1); print(df2)


# In[13]:


#To combine df1 and df2
df3 = pd.merge(df1, df2)
df3


# In[14]:


#Many-to-one joins
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
print(df3); print(df4); print(pd.merge(df3, df4))


# In[15]:


#Many-to-many joins
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                              'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding', 'linux',
                               'spreadsheets', 'organization']})
print(df1); print(df5); print(pd.merge(df1, df5))                  


# In[16]:


#Specification of the Merge Key
#The on keyword
#This option works only if both the left and right DataFrames have the specified column name.
print(df1); print(df2); print(pd.merge(df1, df2, on='employee'))


# In[17]:


df3 = pd.DataFrame({'name':['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})
print(df2); print(df3); print(pd.merge(df2, df3, left_on='employee',right_on='name'))


# In[18]:


"""The result has a redundant column that we can drop if desired—for example, by
using the drop() method of DataFrames:"""
print(pd.merge(df2, df3, left_on='employee',right_on='name').drop('name',axis=1))


# In[19]:


#The left_index and right_index keywords
df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
print(df1a); print(df2a)


# In[20]:


print(pd.merge(df1a, df2a, left_index=True, right_index=True))


# In[21]:


"""For convenience, DataFrames implement the join() method, which performs a
merge that defaults to joining on indices:"""
print(df1a); print(df2a); print(df1a.join(df2a))


# In[22]:


"""If you’d like to mix indices and columns, you can combine left_index with right_on
or left_on with right_index to get the desired behavior:"""
print(df1a); print(df3);
print(pd.merge(df1a, df3, left_index=True, right_on='name'))


# ###### Specifying Set Arithmetic for Joins

# In[23]:


#by default inner join
df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
'food': ['fish', 'beans', 'bread']},
columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
'drink': ['wine', 'beer']},
columns=['name', 'drink'])
print(df6); print(df7); print(pd.merge(df6, df7))


# In[24]:


"""We can specify this explicitly using the how keyword,
which defaults to 'inner':"""
pd.merge(df6, df7, how='inner')


# In[25]:


"""Other options for the how keyword are 'outer', 'left', and 'right'. An outer join
returns a join over the union of the input columns, and fills in all missing values with
NAs:"""
print(df6); print(df7); print(pd.merge(df6, df7, how='outer'))


# In[26]:


print(df6); print(df7); print(pd.merge(df6, df7, how='left'))


# In[27]:


print(df6); print(df7); print(pd.merge(df6, df7, how='right'))


# ###### Overlapping Column Names: The suffixes Keyword

# In[28]:


df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
'rank': [3, 1, 4, 2]})
print(df8); print(df9); print(pd.merge(df8, df9,on="rank"))


# In[29]:


print(df8); print(df9);
print(pd.merge(df8, df9, on="name", suffixes=["_L", "_R"]))


# In[ ]:


df.dropna()


# In[30]:


#US States Data
pop = pd.read_csv('state-population.csv')
areas = pd.read_csv('state-areas.csv')
abbrevs = pd.read_csv('state-abbrevs.csv')


# In[31]:


pop.head()


# In[32]:


#pop_df = pd.get_dummies(pop, columns=['ages'], dtype='int',drop_first=True)
#pop_df


# In[33]:


areas.head()


# In[34]:


areas.shape[0]


# In[35]:


abbrevs.head()


# In[36]:


"""Query: Given this information, say we want to compute a relatively straightforward result:
rank US states and territories by their 2010 population density."""
merged = pd.merge(pop, abbrevs, how='outer',
left_on='state/region', right_on='abbreviation').drop('abbreviation',axis=1)
merged


# In[37]:


merged.isnull().sum()


# In[38]:


"""It appears that all the null population values are from Puerto Rico prior to the year
2000; this is likely due to this data not being available from the original source."""

"""The statement filters the merged DataFrame for rows where the ‘population’ 
column contains missing values (NaN) and returns the first 5 rows of this filtered DataFrame.."""

merged[merged['population'].isnull()].head()


# In[39]:


"""we see also that some of the new state entries are also null, which
means that there was no corresponding entry in the abbrevs key! Let’s figure out
which regions lack this match"""

"""The statement filters the merged DataFrame for rows where the ‘state’ column 
has missing values, and then retrieves the unique values from the ‘state/region’column in those filtered rows. 
This will give a list of unique state/region codes or identifiers that correspond to missing state information."""

merged.loc[merged['state'].isnull(), 'state/region'].unique()


# In[40]:


merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'


# In[41]:


merged.isnull().any()


# In[42]:


areas.head()


# In[43]:


merged.head()


# In[44]:


pd.set_option('display.max_rows', 3000)


# In[45]:


"""Now we can merge the result with the area data using a similar procedure. Examining
our results, we will want to join on the state column in both:"""
final = pd.merge(merged, areas, on='state', how='left')
final


# In[46]:


final.isnull().any()


# In[47]:


"""This statement filters the final DataFrame for rows where the ‘area (sq. mi)’ column has missing values and returns the unique values from the ‘state’ column in those rows. 
This will give a list of unique states that have missing data in the ‘area (sq. mi)’ field."""
final['state'][final['area (sq. mi)'].isnull()].unique()


# In[48]:


"""We see that our areas DataFrame does not contain the area of the United States as a
whole. We could insert the appropriate value (using the sum of all state areas, for
instance), but in this case we’ll just drop the null values because the population density
of the entire United States is not relevant to our current discussion:"""
final.dropna(inplace=True)
final.head()


# In[79]:


# Calculate correlation matrix
correlation_matrix = final[['population', 'area (sq. mi)']].corr()

# Generate a heatmap for the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of Population, Area Correlation')
plt.show()


# In[49]:


get_ipython().system('pip install numexpr')


# In[50]:


#data2010 = final[(final.year == 2010) & (final.ages == 'total')]
data2010 = final.query("year == 2010 & ages == 'total'")
data2010.head()


# In[51]:


data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)
density.head()


# In[52]:


#end list
density.tail()


# ###### Aggregation and Grouping

# In[53]:


#Planets Data
"""It gives information on planets that astronomers
have discovered around other stars (known as extrasolar planets or exoplanets for
short). It can be downloaded with a simple Seaborn command:"""
import seaborn as sns
planets = sns.load_dataset('planets')
planets.shape


# In[54]:


planets.head()


# In[74]:


planets[['method','year']]


# In[55]:


planets.columns


# In[75]:


planets.info()


# In[76]:


"""there is a convenience method describe() that computes several common aggregates for
each column and returns the result."""
planets.describe(include='all')


# In[57]:


planets.isnull().any()


# In[58]:


planets.dropna().describe()


# <pre><b>Listing of Pandas aggregation methods</b>
# Aggregation           Description
# count()               Total number of items
# first(), last()       First and last item
# mean(), median()      Mean and median
# min(), max()          Minimum and maximum
# std(), var()          Standard deviation and variance
# mad()                 Mean absolute deviation
# prod()                Product of all items
# sum()                 Sum of all items</pre>

# ###### Group by: Split, Apply and Combine
# <img src="Group by.png">

# In[77]:


df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
'data': range(1,7)}, columns=['key', 'data'])


# In[78]:


df


# In[61]:


df.groupby('key')


# In[62]:


df.groupby('key').sum()


# In[63]:


planets.groupby('method')


# In[64]:


#column indexing
planets.groupby('method')['orbital_period']


# In[65]:


planets.groupby('method')['orbital_period'].median()


# In[66]:


df = pd.read_json('2024.json')
df.shape


# In[67]:


df.info()


# In[68]:


df.head(10)


# In[69]:


import pandas as pd
import sqlite3

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('diabetes_data_all_patient.csv')

# Create a connection to SQLite database
conn = sqlite3.connect('my_database.db')

# Write the data to a table named 'diabetes'
df.to_sql('diabetes', conn, if_exists='replace', index=False)

# Close the connection
conn.close()


# In[70]:


# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to get the table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch and print the list of tables
tables = cursor.fetchall()
print(tables)

# Close the connection
conn.close()


# In[71]:


# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Write a SQL query to fetch the data
query = "SELECT * FROM diabetes"

# Read the data into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Display the DataFrame
print(df)


# In[72]:


get_ipython().run_line_magic('pip', 'install jupytext')
get_ipython().system('jupytext --to notebook seaborn_visualization_examples.py')


# In[73]:


get_ipython().run_line_magic('pip', 'install jupytext')
get_ipython().system('jupytext --to notebook plotly_visualization_examples.py')


# In[ ]:




