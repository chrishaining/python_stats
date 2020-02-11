# 1. imports: the stats module from the scipy library; numpy; matplotlib
from scipy import stats
import numpy as np 
import matplotlib.pyplot as plt

# 2. create lists to work with
even_list = [1, 2, 3, 5, 6, 7, 2, 4, 5, 9]
odd_list = [1, 2, 3, 4, 5, 6, 2, 5, 9]

# 3. Calculate the IQR using stats
even_iqr = stats.iqr(even_list, interpolation = 'midpoint') 
print(even_iqr)

odd_iqr = stats.iqr(odd_list, interpolation = 'midpoint') 
print(odd_iqr)

# The IQRs differ from the results I got in interquartile_range.py, so I want to check the other parts of the five-figure summaries. 

# 4. calculate medians
even_median = np.median(even_list)
odd_median = np.median(odd_list)

# print(even_median)
# print(odd_median)

# 5. calculate the lower quartiles
even_lower_quartile = np.percentile(even_list, 25)
odd_lower_quartile = np.percentile(odd_list, 25)

print(even_lower_quartile)
print(odd_lower_quartile)

# 6. calculate the upper quartiles
even_upper_quartile = np.percentile(even_list, 75)
odd_upper_quartile = np.percentile(odd_list, 75)

print(even_upper_quartile)
print(odd_upper_quartile)

# 7. calculate the maximum values
even_max = np.max(even_list)
odd_max = np.max(odd_list)

print(even_max)
print(odd_max)

# 8. calculate the minimum values
even_min = np.min(even_list)
odd_min = np.min(odd_list)

print(even_min)
print(odd_min)

# 9. function to create the five-figure summary. 
def create_five_figure_summary(sample):
    percentiles = np.percentile(sample, [25, 50, 75]) # creates LQ, median and UQ. These could be done as separate variables - I just wanted to try it this way
    min, max = np.min(sample), np.max(sample)
    iqr = stats.iqr(sample, interpolation = 'midpoint')
    standardised_iqr = round(iqr / percentiles[1], 2)
    return "Min value: {min}\nLQ: {lq}\nMedian: {median}\nUQ: {uq}\nMax value: {max}\nInterQuartile Range: {iqr}\nStandardised InterQuartile Range: {standardised_iqr}".format(min=min, lq=percentiles[0], median=percentiles[1], uq=percentiles[2], max=max, iqr=iqr, standardised_iqr=standardised_iqr)
    
even_summary = create_five_figure_summary(even_list)
odd_summary = create_five_figure_summary(odd_list)
print(even_summary)
print("\n")
print(odd_summary)