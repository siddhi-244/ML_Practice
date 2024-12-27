# Data Types in ML

"""
1. Numerical  - numbers 
    a. Discrete - counted data that are limited to integers. Example: The number of cars passing by.
    b. continous -  measured data that can be any number. Example: The price of an item, or the size of an item
2. Categorical - values that cannot be measured up against each other. Example: a color value, or any yes/no values.
3. Ordinal - like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.
"""

# Mean, Median, Mode
"""
    Mean - The average value
    Median - The mid point value
    Mode - The most common value
"""
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
y = numpy.median(speed)
sd = numpy.std(speed)
print(x,y,sd) 

# from scipy import stats
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = stats.mode(speed)

# print(x) 