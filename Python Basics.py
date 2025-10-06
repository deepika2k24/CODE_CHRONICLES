#!/usr/bin/env python
# coding: utf-8

# # Unit 1

# ## Basics of Python

# ### Data Types in python

# In[1]:


num1 = 17
num2 = 10.0
pre = 'Py'
print(type(num1),type(num2),type(pre))


# ### Variables in python

# In[2]:


_num1= 3


# ### Basic Operations in python

# #### Number

# In[3]:


print("num1/_num1= {}".format(num1/_num1))
print("num1//_num1= {}".format(num1//_num1))
print("num1%_num1= {}".format(num1%_num1))


# #### String/Text   
# Python Strings are immutable

# In[4]:


print('C:\some\name')
print(r'C:\some\name')  # print as it is
print(3 * 'un' + 'ium')
print('Py' 'thon') # concatenation
print(pre + 'thon')  # variable and string literal use +
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)


# #### Indexing

# In[5]:


word = "Data Science"
print(word[0])
print(word[1])
print(word[-1])
print(word[-2])
print(word[-7])


# #### Slicing

# In[6]:


print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
print(word[:4] )  # character from the beginning to position 2 (excluded)
print(word[5:])   # characters from position 4 (included) to the end
print(word[-7:])  # characters from the second-last (included) to the end
print(word[:2] + word[2:])
print(word[5:42])


# #### Control Flow

# ##### if elif else

# In[8]:


x = int(input("Please enter an integer: "))
if x <0:
    x=0
    print("Negative changed to Zero")
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# ##### for,break,else, contiue

# In[9]:


for i in range(10):
    print(i)


# In[10]:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# In[1]:


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


# ##### pass

# In[ ]:


class MyEmptyClass:
    pass


# ##### match , function

# In[2]:


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# In[3]:


http_error(404)


# In[4]:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


# In[5]:


pt=Point(0,10)


# In[6]:


where_is(pt)


# In[7]:


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to
    n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[8]:


fib(100)


# In[9]:


f=fib


# In[10]:


f(1000)


# ###### More on defining function

# In[14]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[15]:


ask_ok('Is it ok to exit?',10)


# In[16]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[18]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[19]:


parrot(3)


# In[ ]:




