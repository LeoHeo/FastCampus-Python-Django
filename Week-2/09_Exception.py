# 디버깅( Debugging )

# 오류( erros )
# 예외( Exception ) 처리( Handling )

# Error, Exception Handling

# SyntaxError은 실행자체가 되지 않는다.
# SyntaxError => parsingError
if True
    print("Hello")


# from functools import reduce
# n = 10
# fibo = reduce( lambda x, _: x + [x[-1] + x[-2]], range(n-1), [0, 1])

def fibo(n):
    if n < 0:
        raise FibonacciShouldNotHaveNegativeNumberException(n)
    if n == 1:
        return 1
    
    return fibo(n-1) + fibo(n-2)


class FibonacciShouldNotHaveNegativeNumberException(Exception):
    
    def __init__(self, n):
        self.n = n
    
    # 에러 메시지 노란색
    def __str__(self):
        return "피보나치 수열은 index값으로 양수를 받아야 합니다. 입력받은 값: {n}".format(n = self.n)

