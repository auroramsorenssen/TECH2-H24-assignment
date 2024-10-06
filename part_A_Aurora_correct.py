"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

from math import sqrt
import numpy as np

num_lst = [1, 2, 3, 4, 5]




def std_loops(num_lst):
    "Computing the standard deviation of num_lst using loops"

    "Step 1: computing the mean"
    total_num = 0

   
    for i in range(5):
        total_num = total_num + num_lst[i]

    mean = total_num/5


    "Step 2: computing the mean of squares"
    total_Snum = 0

    for i in range(5):
        total_Snum = total_Snum + num_lst[i]**2

    Smean = total_Snum/5


    "Step 3: computing the variance"
    var = Smean - mean**2


    "Step 4: computing standard deviation"
    std = sqrt(var)

    "Printing out all the numbers to visualize them"
    print(f'The mean of num_lst is given by: {mean}')
    print(f'The mean of squares of num_lst is given by: {Smean}')
    print(f'The varience is given by: {var}')
    print(f'The standard deviation is given by: {std}')

    "Returning the function "
    return 

"Calling the function"
std_loops(num_lst)






"Computing the standard deviation of num_lst using built-in funtions sum() and len()"
def std_builtin(num_lst):

    "Step 1: computing the mean"
    mean = (sum(num_lst))/len(num_lst)
    
    "Step 2: computing the mean of squares"
    total_Snum = 0

    for i in range(len(num_lst)):
        total_Snum = total_Snum + num_lst[i]**2
    
    Smean = total_Snum/len(num_lst)

    "Step 3: computing the variance"
    var = Smean - mean**2

    "Step 4: computing standard deviation"
    std = sqrt(var)

    "Printing out all the numbers to visualize them"
    print(f'The mean of num_lst is given by: {mean}')
    print(f'The mean of squares of num_lst is given by: {Smean}')
    print(f'The varience is given by: {var}')
    print(f'The standard deviation is given by: {std}')

    "Returning the function"
    return 

"Calling the function"
std_builtin(num_lst)





"Computing the standard deviation of num_lst using the pre-existing function for standard deviation"
# We need to import numpy to run this code, because std is a pre-existing code from NumPy. 
# Therefore, we write np. infront of the funtion

std_preexisting = np.std(num_lst)
print(f'The standard deviation is given by: {std_preexisting}')

