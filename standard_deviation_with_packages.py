# 1. import numpy and scipy
import numpy as np 
from scipy import stats

# 2. create lists
even_list = [1, 2, 3, 5, 6, 7, 2, 4, 5, 9]
odd_list = [1, 2, 3, 4, 5, 6, 2, 5, 9]
list1 = [1, 2, 3, 4, 5, 6, 2, 4, 5, 9]

# 3. find standard deviation using numpy
numpy_even_standard_deviation = np.std(even_list)
numpy_odd_standard_deviation = np.std(odd_list)
numpy_list1_standard_deviation = np.std(list1)

print(numpy_even_standard_deviation)
print(numpy_odd_standard_deviation)
print(numpy_list1_standard_deviation)

# the result for list1 is the same as my calculation in standard_deviation.py.  

# 4. find standard deviation using stats
stats_list1_standard_deviation = stats.tstd(list1)

print(stats_list1_standard_deviation)
# The result is very different from the result produced by np.std(). This could be because scipy uses a TRIMMED STANDARD DEVIATION (tstd). The tstd is designed to compensate for results that are skewed by extreme values in a sample. That is, it chops off a certain percentage of values from the sample's tails. So, in theory the tstd should be more representative. However, I don't know enough about it to comment further. 

# 5. find variance using numpy - expecting ca. 4.89
numpty_variance = np.var(list1)
print(numpty_variance)

# 6. find variance using stats - there is a .variation method, but I don't understand whether it is doing the same as np.var()
scipy_variation = stats.variation(list1)
print(scipy_variation)