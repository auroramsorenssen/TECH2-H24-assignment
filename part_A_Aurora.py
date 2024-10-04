"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

from math import sqrt

num_lst = [1, 2, 3, 4, 5]


def std_loops(x):
    "Computing the standard deviation of x using loops"
    "Step 1: computing the mean"
    for i in range num_lst:
        max = 5
        min = 1
        total_num = 1+2+3+4+5

        mean = (max - min)/total_num
    

    "Step 2: computing the mean of squares"
    for i in range num_lst:
        Smax = 5^2
        Smin = 1^2
        total_S = 1^2 + 2^2 + 3^2 + 4^2 + 5^2

        Smean = (Smax - Smin)/total_S


    "Step 3: computing the variance"
    for i in range num_lst:
        var = Smean - mean^2

    #var for variance

    "Step 4: computing the standard deviation"
    for std in range N:
        o = sqrt(var)


    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    num_lst = [1, 2, 3, 4, 5]




def std_builtin(x):

    for mean in range len(num_lst):
        mean = (max(num_lst) - min(num_lst))/sum(num_lst)

        for Smean in range len(num_lst):
            S = (num_lst)^2
            Smean = (max(S) - min(S))/sum(S)

            for var in range len(num_lst):
                var = Smean - mean^2

                for std in range len(num_lst):
                    std = sqrt(var^2)

    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    