# [1, 2, 3] => [1, 4, 9]

# 배열로 받는거 제곱
def get_square_list(number_list):
    square_list = []
    
    for i in number_list:
        square_list.append( i ** 2)
        
    return square_list

get_square_list([1, 2, 3])

# 받는 모든 수 제곱
def get_square_list(*args):
    square_list = []
    
    for i in args:
        square_list.append( i ** 2)
        
    return square_list

get_square_list(1, 2, 3)
get_square_list(1, 2, 3, 4)

# [1, 2, 3] => [2, 3, 4]
# 이렇게 계속 함수 만들어 줘야되?! 귀찮게...-_-;;
# def get_increment_list()

# lambda, map
def square(x):
    return x ** 2

list(map(square, [1, 2, 3]))

# 위에꺼 좀더 리팩토링 안되?
# 람다로 해봐
list(map(lambda x: x ** 2, [4, 5, 7,9]))

# 조건을 줄려면 어떻게?
# filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x > 5, numbers))

a = map(lambda x: x ** 8, [1, 2, 3, 4, 5])
for i in a:
    print(i)
    
    
import time
def sleeping_numbers(x):
    time.sleep(1)
    return x ** 2

#map(sleeping_numbers, )

# Map => 모든 Elements => 새로운 List
# Filter => 모든 Elements => True인 Element만 새로운 List

# Reduce
# 줄이는 아이
# 하나만 남기는 애
# Python3 => functools로 분리 import필요

# 뭔소리이야?
import functools
functools.reduce(lambda x,y: x + y, [10, 20, 30, 40])

# 이런게 되는거지
def sum(x, y):
    print((x, y))
    return x + y

functools.reduce(sum, [10, 20, 30, 40])

# 리스트에서 최대값을 뽑는 함수
# Python답지 않아!
def max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

max([1, 9, 2, 3, 7, 11, 4])


# [참일 때의 값] if [조건문] else [거짓일때의 값]
functools.reduce(lambda x,y: x if x > y else y, [1, 9, 2, 3, 7, 11, 4, 15, 20])


# Lambda Operator => 숫자인 애들만 제곱해서 새로운 리스트 만드는거
awesome_list = [1, 2, "안수찬", {}, 4, 5]
#list(filter(lambda x: isinstance(x, int), awesome_list))
list(map(
    lambda x: x ** 2,
    filter(
        lambda x: isinstance(x, int),
        awesome_list
    )
))

# List Comprehension
[i ** 2 for i in range(10)]
list(map(lambda x: x ** 2, range(10)))

[i ** 2 for i in range(9 + 1) if i < 5]
awsome_list = [i for i in range(0, 9+1)]

filter(lambda x: x>5, awsome_list)

square = map(
    lambda x: x**2,
    filter(lambda x: x>5, awsome_list)
)


 
