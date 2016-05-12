# Lambda
# 이름이 없는 함수(익명 함수)
# lambda argument_list: expression

(lambda x,y: x + y)(2, 3)
(lambda x, y: x ** y)(2, 3)


# [1, 2, 3] => [1, 4, 9]
# map(func, seq)
def square(x):
    return x ** 2

a = list(map(square, [1, 2, 3]))

# 위에꺼 좀 더 리팩토링 해보자
# 람다로 바꿔보자
list(map(lambda x: x ** 2, [1, 2, 3]))

# 1 + 2 => 3
# 2 + 3 => 5
# 4 + 3 => 7
list(map(lambda x,y:x + y, [1, 2, 3], [2, 3, 4]))
list(map(lambda x,y:x + y, (1, 2, 3), (2, 3, 4)))

# 짧은거 기준까지 더함
# 2 + 2 = 4
# 3 + 3 = 6
# 4 + 4 = 8
list(map(lambda x,y:x + y, [2, 3, 4, 5], [2, 3, 4]))

# filter
# filter(func, seq)
# 조건을 줄때
number_list = list(range(1, 101))

# 짝수 구하기
list(filter(lambda x: x % 2 == 0, number_list))
list(filter(lambda x: x > 5, number_list))

# Reduce
# 줄이는 아이
# 하나만 남기는 아이
# Python3 => functools로 분리 import필요

# 배열의 요소들의 합
# 연산과정
'''
10 + 20 = 30
30 + 30 = 60
60 + 40 = 100
'''
import functools
functools.reduce(lambda x,y: x + y, [10, 20, 30, 40])

# 리스트중에 가장 큰 값 찾기
# [참일때의 값] if [조건문] else [거짓일때의 값]

# 최대값은 x와y를 비교하면 10>20이 false기 때문에 20이 남는다.
functools.reduce(lambda x,y: x if x>y else y, [10, 20, 30, 40])

# 최소값은 x와y를 비교하면 10<20이 true이기 때문에 10이 남는다.
functools.reduce(lambda x,y: x if x<y else y, [10, 20, 30, 40])

# 숫자인 애들만 제곱해서 새로운 리스트 만들기
# lambda에서 조건없이 연산을 해야 한다. => map
# lambda에서 조건으로 값을 걸러낸다. => filter
# lambda에서 하나의 값만 얻어내야 한다. => reduce
awesome_list = [1, 2, "안수찬", {}, 4, 5]
list(map(
    lambda x: x ** 2,
    filter(
        lambda x: isinstance(x, int), 
        awesome_list
    )
))


# 1~100까지 합 구하기
functools.reduce(
    lambda x,y: x + y, 
    [i for i in range(1, 101)]
)
functools.reduce(
    lambda x,y: x + y, 
    list(range(1, 101))
)

# 1~100까지 짝수 합
functools.reduce(
    lambda x, y: x+y,
    filter(
        lambda x: x%2 == 0,
        list(range(1, 101))
    )
)

# FizzBuzz
# 3의배수 이면 Fizz
# 5의배수 이면 Buzz
# 15의배수 이면 FizzBuzz

# 3, 6, 9, 12, 15
# 5, 10, 15, 20, 25
# 15, 30, 45, 60

# 3으로도 나눠지고 5로도 나눠지면 15의 배수

'''
list(
    filter(
        lambda x: x%3 == 0 or x%5 == 0,
        
    )
)
'''

# List Comprehension
# 3의 배수
[i for i in range(1, 101) if i % 3 == 0]

# 1~100까지 숫자 중에서 짝수인 애들의 제곱 리스트
[i ** 2 for i in range(1, 101) if i % 2 ==0]


# palindrome
# 기러기 => 기러기
# 소주만병만주소 => 소주만병만주소

# 정의부터 해놓고 보자
# 정의 => 문자열을 받아서, 뒤집었을때 같으면 True, 틀리면 False

word = "기러기"
len(word)

# 가장 기초적인 방법
def reverse(word):
    reversed_word = ""
    for i in range(len(word)):
        reversed_word += word[len(word)-1-i]
    return reversed_word


# python slice
# [start:end:step]
"기러기는기러기다"[::-1]

def is_palindrome(word):
    return word == word[::-1]
    
is_palindrome("소주만병만주소")

# 한줄이다 lambda를 이용해보자!!
(lambda x: x == x[::-1])("가나")