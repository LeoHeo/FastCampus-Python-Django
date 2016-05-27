# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# input
#  3 16
#
# output
#   3
#   5
#   7
#   11
#   13

n, m = map(int, input().split())

check = [False] * (m+1)
# check[i] == True: i는 지워짐
# check[i] ==  False: i는 지워지지 않음
primes = []

for i in range(2, m+1):
    # 지워 졌으면 스킵
    if check[i]:
        continue

    # 지워지지 않으면서 가장 작은 수
    if i >= n:
        primes.append(i)

    # i*i부터 i의 배수를 모두 지워버린다
    for j in range(i*i, m+1, i):
        check[j] = True


print("\n".join(map(str, primes)))