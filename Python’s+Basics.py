
# coding: utf-8

# # Welcome to Python

# Based on: http://www.scipy-lectures.org/

# In[ ]:

from IPython.display import Image
from IPython.core.display import HTML 
# Image(url= "https://qph.ec.quoracdn.net/main-qimg-57d110580af8b0196601be5fb58c96fa-c?convert_to_webp=true")
Image(url="http://malwaredoc.com/wp-content/uploads/2014/05/shutterstock_python_0.jpg")


# # Markup

# In[ ]:

# Insert a Markup text here


# # Setups

# ## Try Jupyter (IPYTHON)

# **IPython**, an advanced **Python shell** http://ipython.org/
#  
# To try it on the web, use:  https://try.jupyter.org/
# 
# To learn more about Jupyter: http://jupyter.org/

# # Installing Python & Jupyter using Anaconda and conda

# 1. **Download Anaconda.** Downloading Anaconda’s latest Python 3 version (currently Python 3.5).
# 2. Install the version of Anaconda, which you downloaded.
# 3. Congratulations, you have installed Python and Jupyter Notebook. To run the notebook (from command line):
#     - jupyter notebook

# For more advanced programing you may need another interface. Try pyCharm.

# # Data Science with Python

# We will use the Python language, with some additional building blocks:
# - **Numpy:** provides powerful numerical arrays objects, and routines to manipulate them. http://www.numpy.org/ 
# - **Scipy:** high-level data processing routines. Optimization, regression, interpolation, etc http://www.scipy.org/
# - **Matplotlib:** 2-D visualization,“publication-ready” plots http://matplotlib.org/
# - **pandas:** providing high-performance, easy-to-use data structures and data analysis tools http://pandas.pydata.org/
# - **scikit-learn:** simple and efficient tools for data mining and data analysis http://scikit-learn.org/stable/
# - **Statsmodels:** provides a complement to scipy for statistical computations including descriptive statistics and data exploration, statistical models, and statistical tests. http://statsmodels.sourceforge.net/

# # Set your working directory

# #### Where am I?

# In[ ]:

import os
os.getcwd()


# #### Change a directory:

# In[ ]:

cd ~/


# In[ ]:

cd C:/Users/ofrit/Dropbox/Teaching/Technion/sandbox 


# #### A better idea:

# 1. Create Jupyter's shortcut in your working directory
# 2. Right click it to get into Properties
# 3. Set Target to *jupyter notebook* and Start in to the full path of your new working directory. Aprove the new settings.
# 4. Launch jupyter using your new shortcut.
# 
# Or follow: http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html#change-jupyter-notebook-startup-folder-windows

# # Let's start working

# In[ ]:

print('Hello Python') #shift+enter to run this chunk and move to the next one


# Getting help by using the ? operator after an object:

# In[ ]:

get_ipython().magic('pinfo print')


# ### Run a script 

# Create a ﬁle script1.py in a text editor. In the ﬁle, add the following lines: 
s = 'Hello world' 
print(s)
# Now run your script:

# In[ ]:

get_ipython().magic('run script1.py')


# Explore the resulting variables: 

# In[ ]:

get_ipython().magic('whos')


# **From a script to functions:** plan the script as a set of reusable functions, instead of a ﬁle full of instructions following each other.

# ## Basics

# In[ ]:

a = 3
b = 2*a
type(b)


# In[ ]:

print(b)


# In[ ]:

a*b


# In[ ]:

b = 'hello' 
type(b)


# In[ ]:

b + b


# In[ ]:

b*2


# # Exercise 1: first steps 

# 1. Load the materials of this class into a folder. Create a shortcut to Jupyter and put it in your folder. Set Target and start in properties to change the starting working directory.
# 2. Create a new Python notebook (we will go with conda root).
# 3. Add a new metadata chunk, and describe your next step there. (if you prefer key commands: b for adding a chunk below, m for converting it to metadata)
# 4. Add a new code chunk and print your name.(shift+ enter to run to the next chunk)

# ## Basic Types and Arithmetic Operations 

# In[ ]:

#integer:
1 + 1


# In[ ]:

a = 4
type(a)


# In[ ]:

#Float:
c = 2.1
type(c)


# In[ ]:

#complex
a = 1.5 + 0.5j
a.real


# In[ ]:

a.imag


# In[ ]:

type(1. + 0j) 


# In[ ]:

#Boolean
3 > 4


# In[ ]:

test = (3 > 4) 
test


# In[ ]:

type(test)


# In[ ]:

#Tobesafe: useﬂoats (Python2 returns 2)
7 / 3.


# In[ ]:

2**10 


# In[ ]:

#modulo:
8 % 3 


# In[ ]:

float(1)


# ## Containers

# ### List

# A list is an ordered collection of objects, that may have different types. For example: 

# In[ ]:

l = ['red', 'blue', 'green', 'black', 'white'] 
type(l)


# Python's indices starts at 0, not at 1 (like at R). 
# 
# Access elements by index:

# In[ ]:

l[2]


# In[ ]:

l[-1] 


# In[ ]:

l[-2] 


# The range **start:stop** means: start<= index **<** stop 

# In[ ]:

l[2:4]


# **Slicing syntax:** l[start:stop:stride]
# 
# All slicing parameters are optional:

# In[ ]:

l[3:]


# In[ ]:

l[:3]


# In[ ]:

l[::2]


# Lists are mutable objects and can be modiﬁed: 

# In[ ]:

l[0] = 'yellow' 
l


# In[ ]:

l[2:4] = ['gray', 'purple'] 
l


# The elements of a list may have different types

# In[ ]:

l = [3, -200, 'hello'] 
l


# In[ ]:

l[1],l[2]


# For collections of numerical data that all have the same type, it is often more efﬁcient to use the array type provided by the numpy module. A NumPy array is a chunk of memory containing ﬁxed-sized items. With NumPy arrays, operations on elements can be faster because elements are regularly spaced in memory and more operations are performed through specialized C functions instead of Python loops.

# Add and remove list elements: 

# In[ ]:

l = ['red', 'blue', 'green', 'black', 'white'] 
l.append('pink') 
l


# In[ ]:

l.pop()


# In[ ]:

l


# In[ ]:

l.extend(['pink', 'purple']) # extend l, in-place
l


# In[ ]:

l = l[:-2] 
l


# In[ ]:

#reverse:
r = l[::-1]
r


# Concatenate and repeat lists:

# In[ ]:

r + l


# In[ ]:

r*2


# In[ ]:

#Sort: 
sorted(r) # new object


# In[ ]:

r


# In[ ]:

r.sort() # in-place 
r


# The notation r.method() (e.g. r.append(3) and L.pop()) is our ﬁrst example of object-oriented programming(OOP).Being a list, the object r owns the method function that is called using the notation .

# Discovering methods:
# in Ipython: tab-completion (press tab) 

# In[ ]:

r.<TAB>


# In[ ]:

t = [1,2,3,4]
t


# In[ ]:

#apply a method to each element in the list using "map"
list(map(str,t))


# ## Strings

# In[ ]:

s = 'Hello, how are you?' 
s


# In[ ]:

s = "Hi, what's up" 
s


# In[ ]:

# tripling the quotes allows the string to span more than one line 
s = """Hi, what's 
        up?"""
s


# In[ ]:

s = '''Hello, 
        how are you''' 
s


# Strings are collections like lists. Hence they can be indexed and sliced, using the same syntax and rules.

# In[ ]:

a = "hello, world!"
a[0] 


# In[ ]:

a[3:6] # 3rd to 6th (excluded) elements: elements 3, 4, 5 


# In[ ]:

a[2:10:2] # Syntax: a[start:stop:step] 


# In[ ]:

a[::3] # every three characters, from beginning to end 


# A string is an immutable object and it is not possible to modify its contents. One may however create new strings from the original one. 

# In[ ]:

a[2] = 'z' 


# In[ ]:

a.replace('l', 'z', 1) 


# In[ ]:

a.replace('l', 'z') 


# In[ ]:

#String formatting:
'An integer: %i; a float: %f; another string: %s' % (1, 0.1, 'string') 


# # Exercise 2: Lists

# 1. Create a list with seven numbers.
# 2. Create another list in reverse order, ignoring the first two elements.
# 3. Now use the last list, and check for the number that appears third in the list. (if it's a seven, print 'boom' ;-)  )

# In[16]:

list=[1,2,3,4,5,6,7]
ignore2=list[2:7]
lastlist=ignore2[::-1]
third=lastlist[2]
if third==7:
    print("boom")
else:
    print("no boom")


# ## Dictionaries:

# A dictionary is basically an efﬁcient table that maps keys to values. It is an unordered container 

# In[ ]:

tel = {'emmanuelle': 5752, 'sebastian': 5578} 
tel['francis'] = 5915 
tel


# In[ ]:

tel['sebastian'] 


# In[ ]:

tel.keys() 


# In[ ]:

tel.values() 


# In[ ]:

'francis' in tel 


# It can be used to conveniently store and retrieve values associated with a name. 
# A dictionary can have keys with different types: 

# In[ ]:

d = {'a':1, 'b':2, 3:'hello'} 
d


# ## Tuples

# Tuples are basically immutable lists. The elements of a tuple are written between parentheses,or just separated by commas: 

# In[ ]:

t = 12345, 54321, 'hello!' 
t


# In[ ]:

t[0]


# In[ ]:

t = (12345, 'hello!' )
t


# ## Sets

# Unordered, unique items: 

# In[ ]:

s = set(('a', 'b', 'c', 'a')) 
s


# In[ ]:

s.difference(('a', 'b')) 


# ## Things to note:

# A single object can have several names bound to it: 

# In[ ]:

a = [1, 2, 3] 
b = a
b


# In[ ]:

a is b


# In[ ]:

b[1] = 'hi!' 
a


# In[ ]:

id(a)


# In[ ]:

id(b)


# In[ ]:

# Creates another object
a=['a','b','c']
id(a)


# Mutable objects can be changed in place (while immutable objects cannot be modiﬁed once created)

# In[ ]:

# Modifies object in place:
a[:]= [1,2,3]
id(a)


# #  Control Flow

# **Be careful to respect the indentation depth.** Blocks are delimited by indentation.

# In[ ]:

if 2**2 == 4: 
    print('Obvious!')


# In[ ]:

a = 10
if a == 1:
    print(1)
elif a == 2:
    print(2)
else:
    print('A lot') 


# In[ ]:

for i in range(4):
    print(i) 


# In[ ]:

for word in ('cool', 'powerful', 'readable'):
    print('Python is %s' % word) 


# In[ ]:

z = 2
while abs(z) < 100:
    z = z**2 + 1
z 


# In[ ]:

#iterate over a sequence while keeping track of the item number:
words = ('cool', 'powerful', 'readable') 
for index, item in enumerate(words):
    print((index, item)) 


# In[ ]:

#Looping over a dictionary:
d = {'a': 1, 'b': 1.2, 'c': True}
for key, val in sorted(d.items()):
    print('Key: %s has value: %s' % (key, val)) 


# In[ ]:

# List Comprehensions
[i**2 for i in range(4)] 


# ## Defining functions

# In[ ]:

def test():
    print('in test function') 


# In[ ]:

test() 


# In[ ]:

def disk_area(radius):
    return 3.14 * radius * radius 

disk_area(1.5) 


# By default, functions return None.
# 
# Mandatory parameters:

# In[ ]:

disk_area() #a missing parameter


# In[ ]:

#Optional parameters (Keyword arguments allow you to specify default values.)
def disk_area(radius=2):
    return 3.14 * radius * radius 

disk_area() 


# Default values are evaluated when the function is deﬁned, not when it is called. This can be problematic when using mutable types (e.g. dictionary or list) and modifying them in the function body, since the modiﬁcations will be persistent across invocations of the function. 

# In[ ]:

bigx = 10
def double_it(x=bigx):
    return x * 2

bigx = 1e9 # Now really big
double_it() 


# Using a mutable type in a keyword argument (and modifying it inside the function body): 

# In[ ]:

def add_to_dict(args={'a': 1, 'b': 2}): 
    for i in args.keys(): 
        args[i] += 1 
    print(args)
        
add_to_dict()


# In[ ]:

add_to_dict() 


# In[ ]:

add_to_dict() 


# Parameters to functions are references to objects, which are passed by value. When you pass a variable to a function, python passes the reference to the object to which the variable refers (the value). Not the variable itself. If the value passed in a function is immutable, the function does not modify the caller’s variable. If the value is mutable,the function may modify the caller’s variable in-place: 

# In[ ]:

def try_to_modify(x, y, z):
    x = 23
    y.append(42)
    z = [99] # new reference 
    print(x) 
    print(y) 
    print(z) 
    
a = 77 # immutable variable
b = [99] # mutable variable 
c = [28] 
try_to_modify(a, b, c) 


# In[ ]:

print(a) 


# In[ ]:

print(b) 


# In[ ]:

print(c)


# Functions have a local variable table called a local namespace. 
# The variable x only exists within the function try_to_modify.

# #### Global variables

# Variables declared outside the function can be referenced within the function: 

# In[ ]:

x = 5
def addx(y):
    return x + y
addx(10)


# But these “global” variables cannot be modiﬁed within the function, unless declared global in the function.
# This doesn’t work: 

# In[ ]:

x = 5
def setx(y):
    x = y
    print('x is %d' % x)
    
setx(10) 


# In[ ]:

x


# This works:

# In[ ]:

x=5
def setx(y):
    global x 
    x = y 
    print('x is %d' % x)
    
setx(10) 


# In[ ]:

x


# #### Variable number of parameters

# **Special forms of parameters:**
#     - *args: any number of positional arguments packed into a tuple 
#     - **kwargs: any number of keyword arguments packed in to a dictionary

# In[ ]:

def variable_args(*args, **kwargs):
    """Concise one-line sentence describing the function.
    Extended summary which can contain multiple paragraphs.
    """
    print('args is', args)
    print('kwargs is', kwargs)
    
variable_args('one', 'two', x=1, y=2, z=3) 


# In[ ]:

#see the docstring when searching for help with this function
get_ipython().magic('pinfo variable_args')


# Functions are ﬁrst-class objects, which means they can be assigned to a variable.
# Methods are functions attached to objects. 

# In[ ]:

va = variable_args
va('three', x=1, y=2) 


# # Exercise 3: Fibonacci sequence

# Write a function that displays the n ﬁrst terms of the Fibonacci sequence, deﬁned by: 
#     - u_0 = 1; u_1 = 1 
#     - u_(n+2) = u_(n+1) + u_n

# ### Importing objects from modules 

# In[ ]:

import numpy as np # data arrays 
np.linspace(0, 10, 6) 


# In[ ]:

import scipy # scientific computing


# ###  Creating modules

# If we want to write larger and better organized programs (compared to simple scripts), where some objects are deﬁned, (variables, functions, classes) and that we want to reuse several times, we have to create our own modules. 
# Let us create a module demo contained in the ﬁle demo.py: 
"A demo module."

def print_b():
    "Prints b."
    print('b')
    
def print_a(): 
    "Prints a."
    print('a')

c = 2 
d = 2 
# In this ﬁle, we deﬁned two functions print_a and print_b. Suppose we want to call the print_a function from the interpreter. We could execute the ﬁle as a script, but since we just want to have access to the function print_a, we are rather going to import it as a module. The syntax is as follows. 

# In[ ]:

import demo
demo.print_a() 


# In[ ]:

demo.print_b()


# Modules are cached: if you modify demo.py and re-import it in the old session, you will get the old one. Solution: 

# In[ ]:

import importlib
importlib.reload(demo)

