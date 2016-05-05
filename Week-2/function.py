# Parameter로 받은걸 모두 더해주는 `sum`함수를 만들어라.

# Parameter로 받은 모든걸?
# 일단 리스트로 구현방법
def sum(number_list):
    total = 0
    for i in number_list:
        total += i
    return total

# 흠..리스트는 알겠는데 파라미터가 가변적이면?
# e.g) sum(1, 2, 3) sum(1, 2, 4, 7)
# unnamed => *args(tuple) => argument(args)
def sum(*args):
    total = 0
    for i in args:
        total += i
    return total


# 1, 2, 3 arguments가 여러개인데 *args로 받을 수 있는 이유는?
# python의 packing / unpacking 덕분에

# unpacking
a, b = (1, 3)
print(a, b)

# packing
e = 2, 4
print(e)

# *args를 활용한 greeting
# named Parameter 안됨

def greeting(*values):
    print(values)
    for value in values:
        print(value)

values = ["허진한", "웹프"]
values2 = {"홍길동", "데이터사이언스"}
values3 = ("고길동", "마케팅")

# dict를 전해주기엔 *args는 적합하지 않음
# 뭐가 좋을까?
values4 = {
    "name": "유시진",
    "course": "영어회화"
}

# **kwargs => named parameter => keword argument
# named_parameter 지정가능
# dict에 적합함
def print_all_information(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_all_information(**values4) 
# print_all_information(**values2) => ERROR(dict 빼고는 모두 에러)
print_all_information(
    named="김지원", 
    course="프론트엔드"
)

# 라이브러리 만들때 아래와 같이 만드는 경우 많음
def some_function(___, ___, *args, *kwargs):
    
