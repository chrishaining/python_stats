# This program calculates the INTERQUARTILE RANGE (IQR) for a list of values. The IQR gives an indication of the spread of the values. 

# ONE PROBLEM MIGHT BE HOW TO DEAL WITH A LIST THAT HAS AN EVEN NUMBER OF VALUES IN IT. I WILL START BY IGNORING THE PROBLEM AND SEEING WHAT PYTHON DOES.

#  1. create a list of values.
even_list = [1, 2, 3, 5, 6, 7, 2, 4, 5, 9]
odd_list = [1, 2, 3, 4, 5, 6, 2, 5, 9]

# 2. sort the list. 
even_list.sort()
odd_list.sort()
print(even_list)
print(odd_list)

# 3. find the median value. The if else statement solves the problem of having a list with an even number of values.
def find_median(list_name):
    length = int(len(list_name))
    if length % 2 == 0:
        lower_median_index = list_name[int((length - 1) / 2)]
        higher_median_index = list_name[int(length / 2)]
        median_index = (lower_median_index + higher_median_index) / 2
    else: 
        median_index = list_name[int((length - 1) / 2)]
    return median_index

even_median=find_median(even_list)
odd_median=find_median(odd_list)

print(even_median)
print(odd_median)

# 4. find the top value.
def find_top_value(list_name):
    top_value = list_name[-1]
    return top_value

# print the results of step 4 (expect 9)
even_top_value = find_top_value(even_list)
odd_top_value = find_top_value(odd_list)

print("The top value for the even list is {}.".format(even_top_value))
print("The top value for the odd list is {}.".format(odd_top_value))

# 5. find the bottom value.
def find_bottom_value(list_name):
    bottom_value = list_name[0]
    return bottom_value

# print the results of step 4 (expect 1)
even_bottom_value = find_bottom_value(even_list)
odd_bottom_value = find_bottom_value(odd_list)
print("The bottom value for the even list is {}.".format(even_bottom_value))
print("The bottom value for the odd list is {}.".format(odd_bottom_value))



# 6. find the LQ (lower quartile) value. There are a few methods to do this that I can think of. I'm going to start by creating a slice of the lower half of the sorted list.
even_list_lower_half = even_list[0:int(find_median(even_list) + 1)]
print(even_list_lower_half)

odd_list_lower_half = odd_list[0:int(find_median(odd_list))]
print(odd_list_lower_half)

even_lower_quartile = find_median(even_list_lower_half)
print(even_lower_quartile)

odd_lower_quartile = find_median(odd_list_lower_half)
print(odd_lower_quartile)

# 7. find the UQ (upper quartile) value.
even_list_upper_half = even_list[int(find_median(even_list) + 1):]
print(even_list_upper_half)

odd_list_upper_half = odd_list[int(find_median(odd_list) + 1):]
print(odd_list_upper_half)


even_upper_quartile = find_median(even_list_upper_half)
print(even_upper_quartile)

odd_upper_quartile = find_median(odd_list_upper_half)
print(odd_upper_quartile)

# 8. print the values.
print("The IQR for the even list is: \nBottom Value: {even_bottom_value}\nLower Quartile: {even_lower_quartile}\nMedian: {even_median}\nUpper Quartile: {even_upper_quartile}\nTop Value: {even_top_value}.".format(even_bottom_value=even_bottom_value, even_lower_quartile=even_lower_quartile, even_median=even_median, even_upper_quartile=even_upper_quartile, even_top_value=even_top_value))

print("\n")

print("The IQR for the odd list is: \nBottom Value: {odd_bottom_value}\nLower Quartile: {odd_lower_quartile}\nMedian: {odd_median}\nUpper Quartile: {odd_upper_quartile}\nTop Value: {odd_top_value}.".format(odd_bottom_value=odd_bottom_value, odd_lower_quartile=odd_lower_quartile, odd_median=odd_median, odd_upper_quartile=odd_upper_quartile, odd_top_value=odd_top_value))

#  9. Calculate the IQR (Upper Quartile - Lower Quartile)
even_iqr = even_upper_quartile - even_lower_quartile
print("The IQR for the even list is {}.".format(even_iqr))

odd_iqr = odd_upper_quartile - odd_lower_quartile
print("The IQR for the odd list is {}.".format(odd_iqr))


# 10. Calculate the standardised IQR (result of step 9 / median)
even_standardised_iqr = even_iqr / even_median
print("The standardised IQR for the even list is {}.".format(even_standardised_iqr))

odd_standardised_iqr = odd_iqr / odd_median
print("The standardised IQR for the odd list is {}.".format(odd_standardised_iqr))

# 11. Make a statement comparing the variation
def find_most_variation(even, odd):
    if even > odd:
        return "The even list shows the most variation."
    elif odd > even:
        return "The odd list shows the most variation."
    else:
        return "The two lists have equal variance."

result = find_most_variation(even_standardised_iqr, odd_standardised_iqr)
print(result)