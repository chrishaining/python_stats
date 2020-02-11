# This program calculates the standard deviation and variance of values in a list. 

# import the math module. This allows us to easily calculate square roots.
import math

# 1. create a list
list1 = [1, 2, 3, 4, 5, 6, 2, 4, 5, 9]
print("The sample is: {}.".format(list1))

# 2. calculate the mean of the values in the list
list_sum = 0
for item in list1:
    list_sum += item 
list_mean = list_sum / len(list1)
print("The mean of the sample is {}.".format(list_mean))

# 3. for each value in the list, calculate the distance from the mean. First, create a new list of deviaions.
deviations = []
for value in list1: 
    deviation = value - list_mean 
    deviations.append(deviation)
print("The list of deviations is: {}.".format(deviations))
# 4. square the deviations for each value, and add them to a sum of deviations. 
deviation_sum = 0
for deviation in deviations:
    squared_deviation = deviation * deviation 
    deviation_sum += squared_deviation
print("The sum of deviations is {}.".format(deviation_sum))

# 5. divide the result of step 5 by the number of items in the list. This will give you the VARIANCE.
variance = deviation_sum / len(list1)
print("The variance is {}.".format(variance))

# 6. find the square root of the variance. The result is the STANDARD DEVIATION.
standard_deviation = math.sqrt(variance)
print("The standard deviation is {}.".format(standard_deviation))

# I haven't converted any of the numbers to float or adjusted the number of decimal points.