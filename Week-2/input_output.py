username = input("이름이 뭐니?")


# Python 3.x => input
for i in range( int(input("별 몇개?"))):
    print("*" * (i + 1))

 

# Python 2.x => raw_input()


# ./ => 현재 폴더
# ../ => 상위 폴더

# ./test.txt => 현재 폴더에 있는 test.txt
# ../test.txt => 상위 폴더에 있는 test.txt
# ../../test.txt => 상위 폴더의 상위 폴더에 있는 test.txt

# open("경로", "mode")
f = open("../animals.txt", "r")

f.read()
# f.realine()
# f.readlines()


# 함수
# 작업 자동화
# 우리가 반복적으로 사용할 어떤 특정 기능들에 대해서 => 재사용 가능한 코드 덩어리

def greeting():
    username = input()
    print("{username}님, 가입을 축하드립니다.".format(username=username))



# greeting() => 실행방법

# 매개변수
def print_pretty_star(count):
    """
    이 함수는 별찍기 함수입니다.
    """
    for i in range(count):
        print("*" * (i + 1))


# print_pretty_star(5)
# print_pretty_star(int(input("몇개의 별을 입력할까요?")))
