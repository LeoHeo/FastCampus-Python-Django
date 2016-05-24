# Let's delve into one of the most basic data types in Python, the list. You are given  numbers. Store them in a list and find the second largest number.
#
# NOTE: Do not use the insertion sort method.
#
# Input Format
#
# The first line contains . The second line contains an array [] of  integers each separated by a space.
#
# Output Format
#
# Output the value of the second largest number.

number = int(input())

sorted_number_list = sorted(
     list(
         map(
             int,
             list(set(input().split())))
     )
)

print(sorted_number_list[-2])

