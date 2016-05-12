
count = 5

# stat_1
for i in range(5):
    print("*" * (i + 1))

# star_2
for i in range(count):
    # 앞에 공백(blank)은 총 갯수(count)에서 i가 증가하는것 만큼 감소
    # 뒤에 별표(asterisk)는 i가 증가하는것 만큼 증가
    print(" " * (count - i) + ("*" * (i + 1)))


# star_3
for i in range(count):
    # (총갯수 - i) 만큼 * 추가
    print( "*" * (count - i))


# star_4
for i in range(count):
    print(" " * (i + 1) + "*" * (count - i))
