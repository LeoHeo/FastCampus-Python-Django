# Given an integer n consisting of an even number of digits, swap pairs of adjacent digits in it, i.e. swap the first digit with the second one, the third digit with the fourth one, etc.

# Example

# For n = 1234, the output should be
# swapNeighbouringDigits(n) = 2143.

# [input] integer n

# A positive integer consisting of an even number of digits which does not contain 0s.

# [output] integer

# Test1
# Input:
# 	n: 1234
# Expected Output:
# 	2143

# Test2
# Input:
# 	n: 12345678
# Expected Output:
# 	21436587

# Test3
# Input:
# 	n: 12
# Expected Output:
# 	21


def swapNeighbouringDigits(n):
  number_to_string = str(n)

  # Tuple 사용 swap
  for i in range(1, len(number_to_string), 2):
  	number_to_string[i-1], number_to_string[i] = number_to_string[i], number_to_string[i-1]
        
  return int(''.join(number_to_string))


# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Example

# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.
# [input] integer n

# A ticket number represented as a positive integer of even length.

# [output] boolean

# true if n is a lucky ticket number, false otherwise.

# Test 1
# Input:
# 	n: 1230
# Expected Output:
# 	true

# Test 2
# Input:
# 	n: 239017
# Expected Output:
# 	false

# Test 3
# Input:
# 	n: 134008
# Expected Output:
# 	true


def isLucky(n):
  number_to_string = str(n)
  mid = len(number_to_string) / 2

  first_sum = sum(
  	map(
  		int,
  		number_to_string[:mid]
  	)
  )

  second_sum = sum(
  	map(
  		int,
  		number_to_string[mid:]
  	)
  )

  return first_sum == second_sum
