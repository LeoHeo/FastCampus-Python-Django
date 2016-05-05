# 내가 한것
def star():
    '''
    좀더 심화된 별찍기 모래시계
    모래시계를 4개로 분할해서 생각해봄
    '''
    count = int(input("별의 갯수?"))
    for i in range(count):
        top_front = " " * i + "*" * (count - i) 
        top_back = "*" * (count - (i - 1))
        
        print(top_front + top_back)

    for i in range(count):
        bottom_front = " " * (count - i) + "*" * i
        bottom_back = "*" * (i + 1)

        print(bottom_front + bottom_back)


star()

print("조교가 한것")

# 조교가 한것
def star_staff():
    '''
    조교가 한것
    '''
    cnt = int(input("숫자 입력:"))
    for i in range(1, cnt):
        print(" " * (i - 1), end="")
        print("*" * (-2 * i + (2 * cnt + 1)), end="")
        print()
    for i in range(1, cnt+1):
        print(" " * (-1 * i + cnt), end="")
        print("*" * (i * 2 -1), end="")
        print()

star_staff()
