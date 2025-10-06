#!/usr/bin/env python
# coding: utf-8

# ## Numpy Basics

# In[ ]:


import numpy as np


# In[ ]:


np # numpy built-in doc


# In[ ]:


np  # press <TAB> to display all the contents of numpy namespace


# In[ ]:


np.__version__  # Version of numpy 


# ##### Creating Arrays from Python Lists

# In[ ]:


# integer array:
np.array(range(10))


# In[ ]:


"""Remember that unlike Python lists, NumPy is constrained to arrays that all contain
the same type. If types do not match, NumPy will upcast if possible (here, integers are
upcast to floating point)"""
np.array([3.14, 4, 2, 3])


# In[ ]:


np.array([1, 2, 3, 4], dtype='int')


# In[ ]:


get_ipython().run_line_magic('pinfo', 'np.array')


# In[ ]:


# nested lists result in multidimensional arrays
np.array([range(i, i + 3) for i in [2, 4, 6]])


# ##### Creating Arrays from Scratch

# In[ ]:


#Create a length-10 integer array filled with zeros
np.zeros(10,dtype='int')


# In[ ]:


get_ipython().run_line_magic('pinfo', 'np.ones')


# In[ ]:


# Create a 3x5 floating-point array filled with 1s
np.ones((3, 5),dtype='int')


# In[ ]:


# Create a 3x5 array filled with 3.14
np.full((3, 5), 3.14)


# In[ ]:


# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
np.arange(0, 20, 2)


# In[ ]:


# Create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)


# In[ ]:


# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3, 3))


# In[ ]:


#Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
np.random.normal(0, 1, (3, 3))


# In[ ]:


# Create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3, 3))


# In[ ]:


# Create a 3x3 identity matrix
np.eye(3)


# In[ ]:


# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that
# memory location
np.empty(4)


# ### NumPy Standard Data Types
# NumPy arrays contain values of a single type, so it is important to have detailed
# knowledge of those types and their limitations. Because NumPy is built in C, the
# types will be familiar to users of C, Fortran, and other related languages.

# ###### Data type Description
# <pre>bool_        Boolean (True or False) stored as a byte
# int_         Default integer type (same as C long; normally either int64 or int32)
# intc         Identical to C int (normally int32 or int64)
# intp         Integer used for indexing (same as C ssize_t; normally either int32 or int64)
# int8         Byte (–128 to 127)
# int16        Integer (–32768 to 32767)
# int32        Integer (–2147483648 to 2147483647)
# int64        Integer (–9223372036854775808 to 9223372036854775807)
# uint8        Unsigned integer (0 to 255)
# uint16       Unsigned integer (0 to 65535)
# uint32       Unsigned integer (0 to 4294967295)
# uint64       Unsigned integer (0 to 18446744073709551615)
# float_       Shorthand for float64
# float16      Half-precision float: sign bit, 5 bits exponent, 10 bits mantissa
# float32      Single-precision float: sign bit, 8 bits exponent, 23 bits mantissa
# float64      Double-precision float: sign bit, 11 bits exponent, 52 bits mantissa
# complex_     Shorthand for complex128
# complex64    Complex number, represented by two 32-bit floats
# complex128   Complex number, represented by two 64-bit floats</pre>
# 
# Refer for  more advanced datatypes in https://numpy.org

# ##### The Basics of NumPy Arrays

# Attributes of arrays:
# Determining the size, shape, memory consumption, and data types of arrays

# In[ ]:


np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array


# In[ ]:


print(x1)


# In[ ]:


print(x2)


# In[ ]:


print(x3)


# In[ ]:


"""Each array has attributes ndim (the number of dimensions), shape (the size of each
dimension), and size (the total size of the array):"""
print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)


# In[ ]:


print("dtype:", x3.dtype)


# In[ ]:


"""Other attributes include itemsize, which lists the size (in bytes) of each array element,
and nbytes, which lists the total size (in bytes) of the array"""
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")


# In[ ]:


x2


# In[ ]:


#Array Indexing: Accessing Single Elements
x2[0, 0]


# In[ ]:


x2[2, -1]


# In[ ]:


x2[0, 0] = 12
x2


# In[ ]:


#Array Slicing: Accessing Subarrays
#x[start:stop:step]
#One-dimensional subarrays
x = np.arange(10)
x


# In[ ]:


print(x[:5] )# first five elements
print (x[5:]) # elements after index 5
print(x[4:7]) # middle subarray


# In[ ]:


x[::2] # every other element


# In[ ]:


x[1::2] # every other element, starting at index 1


# In[ ]:


"""A potentially confusing case is when the step value is negative. In this case, the
defaults for start and stop are swapped. This becomes a convenient way to reverse
an array"""
x[::-1] # all elements, reversed


# In[ ]:


x[5::-2] # reversed every other from index 5


# ##### Multidimensional subarrays
# Multidimensional slices work in the same way, with multiple slices separated by commas.
# For example:

# In[ ]:


x2


# In[ ]:


x2[:2, :3] # two rows, three columns


# In[ ]:


x2[:3, ::2] # all rows, every other column


# In[ ]:


x2[::-1, ::-1]


# In[ ]:


print(x2[:, 0])
print(x2[0, :]) #x2[0]


# ###### Subarrays as no-copy views

# In[ ]:


"""One important—and extremely useful—thing to know about array slices is that they
return views rather than copies of the array data. This is one area in which NumPy
array slicing differs from Python list slicing: in lists, slices will be copies"""
print("\nx2\n",x2)
x2_sub = x2[:2, :2]
print("\nx2_sub\n",x2_sub)
x2_sub[0, 0] = 99
print("\nx2_sub\n",x2_sub)
print("\nx2\n",x2)


# In[ ]:


x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)


# In[ ]:


x2_sub_copy[0, 0] = 42
print(x2_sub_copy)


# In[ ]:


print(x2)


# ###### Reshaping of Arrays

# In[ ]:


"""Another useful type of operation is reshaping of arrays. The most flexible way of
doing this is with the reshape() method. For example, if you want to put the numbers
1 through 9 in a 3×3 grid, you can do the following:"""
grid = np.arange(1, 10).reshape((3, 3))
print(grid)


# In[ ]:


x = np.array([1, 2, 3])
# row vector via reshape
x.reshape((3, 1))


# In[ ]:


# row vector via newaxis
x[np.newaxis,:]


# In[ ]:


# column vector via reshape
x.reshape((3, 1))


# In[ ]:


# column vector via newaxis
x[:, np.newaxis]


# ###### Array Concatenation and Splitting

# In[ ]:


x= np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])


# In[ ]:


z = [99, 99, 99]
np.concatenate([x, y,z])


# In[ ]:


# concatenate along the first axis
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
np.concatenate([grid,grid])


# In[ ]:


# concatenate along the second axis
np.concatenate([grid,grid],axis=1)


# In[ ]:


"""For working with arrays of mixed dimensions, it can be clearer 
to use the np.vstack(vertical stack) 
and np.hstack (horizontal stack) functions"""
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],[6, 5, 4]])
# vertically stack the arrays
np.vstack([x, grid])


# In[ ]:


# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])


# In[ ]:


"""If `indices_or_sections` is a 1-D array of sorted integers,
the entries indicate where along `axis` the array is split.  
For example, ``[2, 3]`` would, for ``axis=0``, result in

      - ary[:2]
      - ary[2:3]
      - ary[3:]"""
x = np.arange(9)
#np.split(x, 3)

np.split(x, [2,3])


# In[ ]:


grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)


# ###### Universal functions (ufunc)
# ###### Arithmetic operators implemented in NumPy

# +  np.add Addition (e.g., 1 + 1 = 2)<br>
# + np.subtract Subtraction (e.g., 3 - 2 = 1)<br>
# +  np.negative Unary negation (e.g., -2)<br>
# +  np.multiply Multiplication (e.g., 2 * 3 = 6)<br>
# +  np.divide Division (e.g., 3 / 2 = 1.5)
# +  np.floor_divide Floor division (e.g., 3 // 2 = 1)<br>
# +  np.power Exponentiation (e.g., 2 ** 3 = 8)<br>
# +  np.mod Modulus/remainder (e.g., 9 % 4 = 1)<br>

# In[ ]:


x = np.arange(4)
print("x =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2) # floor division
print("-x = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2 = ", x % 2)


# In[ ]:


np.add(x, 2)


# In[ ]:


#Trignometric function 
theta = np.linspace(0, np.pi, 3)
theta


# In[ ]:


print("theta = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))


# In[ ]:


#Exponents and logarithms
x = [1, 2, 3]
print("x =", x)
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("3^x =", np.power(3, x))
x = [1, 2, 4, 10]
print("x =", x)
print("ln(x) =", np.log(x))
print("log2(x) =", np.log2(x))
print("log10(x) =", np.log10(x))


# In[ ]:


x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)


# In[ ]:


print(x)
y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)


# ###### Aggregates

# In[ ]:


"""For binary ufuncs, there are some interesting aggregates that can be computed
directly from the object."""
x = np.arange(1, 7)  #(1+2+3+4+5+6 = (6*7)/2)
np.add.reduce(x)


# In[ ]:


np.multiply.reduce(x)   


# In[ ]:


np.add.accumulate(x)


# In[ ]:


np.multiply.accumulate(x)


# In[ ]:


x = np.arange(1, 6)
np.multiply.outer(x, x)  #[1,2,3,4,5]x [1,2,3,4,5]


# In[ ]:


L = np.arange(10)
np.sum(L)


# In[ ]:


big_array = np.random.rand(1000000)
get_ipython().run_line_magic('timeit', 'sum(big_array)')
get_ipython().run_line_magic('timeit', 'np.sum(big_array)')


# In[ ]:


get_ipython().run_line_magic('timeit', 'min(big_array)')
get_ipython().run_line_magic('timeit', 'np.min(big_array)')


# In[ ]:


#Multidimensional aggregates
M = np.random.random((3, 4))
print(M)


# In[ ]:


M.sum()


# In[ ]:


M.min(axis=0)


# In[ ]:


M.max(axis=1)


# ###### Other aggregation functions
# <pre>Function Name    NaN-safe       Version Description
# np.sum          np.nansum        Compute sum of elements
# np.prod         np.nanprod       Compute product of elements
# np.mean         np.nanmean       Compute median of elements
# np.std          np.nanstd        Compute standard deviation
# np.var          np.nanvar        Compute variance
# np.min          np.nanmin        Find minimum value
# np.max          np.nanmax        Find maximum value
# np.argmin       np.nanargmin     Find index of minimum value
# np.argmax       np.nanargmax     Find index of maximum value
# np.median       np.nanmedian     Compute median of elements
# np.percentile   np.nanpercentile Compute rank-based statistics of elements
# np.any          N/A              Evaluate whether any elements are true
# np.all          N/A              Evaluate whether all elements are true</pre>

# ###### Comparison Operators as ufuncs

# In[ ]:


x = np.array([1, 2, 3, 4, 5])
print(x < 3) # less than
print(x > 3) # greater than
print(x <= 3) # less than or equal
print(x >= 3) # greater than or equal
print(x != 3) # not equal
print(x == 3) # equal


# In[ ]:


x=np.random.randint(10,size=(3,4))
x


# In[ ]:


# how many values less than 6?
np.count_nonzero(x < 6)


# In[ ]:


np.sum(x < 6)


# In[ ]:


# how many values less than 6 in each row?
np.sum(x < 6, axis=1)


# In[ ]:


# are there any values greater than 8?
np.any(x > 8)


# In[ ]:


# are all values less than 10?
np.all(x < 10)


# In[ ]:




