"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using Numpy library as much as possible (note: you can combine with OOP from the previous task).
"""

import numpy as np

n = int(input())
numbers = np.array([int(input()) for _ in range(n)])
# Read the target value (X) to search for
x = int(input())   # for example, input 3 10 20 30 20

indices = np.where(numbers == x)[0]  
if indices.size > 0:
    print(indices[0] + 1)  
else:
  # Print -1 if no matches found
    print(-1)   # output 2
