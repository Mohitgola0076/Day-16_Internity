
                               # Python Pandas - Descriptive Statistics
                               

A large number of methods collectively compute descriptive statistics and other related operations on DataFrame. Most of these are 
aggregations like sum(), mean(), but some of them, like sumsum(), produce an object of the same size. Generally speaking, these 
methods take an axis argument, just like ndarray.{sum, std, ...}, but the axis can be specified by name or integer

DataFrame − “index” (axis=0, default), “columns” (axis=1)

Let us create a DataFrame and use this object throughout this chapter for all the operations.


              # Example : 
                
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print df

                # Output −

    Age  Name   Rating
0   25   Tom     4.23
1   26   James   3.24
2   25   Ricky   3.98
3   23   Vin     2.56
4   30   Steve   3.20
5   29   Smith   4.60
6   23   Jack    3.80
7   34   Lee     3.78
8   40   David   2.98
9   30   Gasper  4.80
10  51   Betina  4.10
11  46   Andres  3.65


                    # Functions & Description : 
                    
Let us now understand the functions under Descriptive Statistics in Python Pandas. The following table list down the important functions −

Sr.No.	Function	Description
1	count()	Number of non-null observations
2	sum()	Sum of values
3	mean()	Mean of Values
4	median()	Median of Values
5	mode()	Mode of values
6	std()	Standard Deviation of the Values
7	min()	Minimum Value
8	max()	Maximum Value
9	abs()	Absolute Value
10	prod()	Product of Values
11	cumsum()	Cumulative Sum
12	cumprod()	Cumulative Product



                                 #  numpy.random.rand() in Python : 
                                 
The numpy.random.rand() function creates an array of specified shape and fills it with random values.
Syntax :   numpy.random.rand(d0, d1, ..., dn)

    # Parameters :
d0, d1, ..., dn : [int, optional]Dimension of the returned array we require, 
     If no argument is given a single Python float is returned.
     
    # Return :
Array of defined shape, filled with random values.

    Code 1 : Randomly constructing 1D array
    
# Python Program illustrating
# numpy.random.rand() method

import numpy as geek

# 1D Array
array = geek.random.rand(5)
print("1D Array filled with random values : \n", array);

        # Output : 
        
1D Array filled with random values : 
 [ 0.84503968  0.61570994  0.7619945   0.34994803  0.40113761]
 
 
                    #  random distributions with numpy and scipy.

In [135]:
from numpy import random
x = random.choice(a, p=[0.1, 0.2, 0.5, 0.2],size=20)  #p is total sum 1
x

array([3, 5, 4, 3, 3, 5, 4, 2, 5, 2, 4, 4, 5, 2, 4, 4, 3, 5, 2, 5])
In [139]:
c=random.choice(a,p=[0.2,0.4,0.2,0.2],size=6)
c
Out[139]:
array([5, 3, 3, 4, 2, 2])
In [233]:
from scipy.stats import alpha

import scipy
#beta ppf etc.
In [234]:
b=3
In [235]:
r = alpha.rvs(b, size=1000) #rvs random
In [236]:
plt.plot(r)
Out[236]:
[<matplotlib.lines.Line2D at 0x7f8968b68ed0>]


                        # Generate Random Number
NumPy offers the random module to work with random numbers.

Example
Generate a random integer from 0 to 100:

from numpy import random

x = random.randint(100)

print(x)


                        # Random Distribution :
                        
A random distribution is a set of random numbers that follow a certain probability density function.
Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

