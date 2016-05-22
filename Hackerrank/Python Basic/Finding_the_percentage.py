# You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
#
# Input Format
#
# The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
#
# Output Format
#
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#
# Constraints
#   2 <= N <= 10
#   0 <= Marks <= 100
#
# Sample Input
#
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
#
# Sample Output
# 56.00


count = int(input())
info_dict = {}

for i in range(count):
    info_input = input().split()
    info_dict[info_input[0]] = sum(map(float, info_input[1:])) / len(info_input[1:])

name = input()
print(format(info_dict.get(name), ".2f"))
