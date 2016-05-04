# 내가한것
for i in range( 6):
    for j in range( 6):
        if(i > j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 1번 방식
for i in range(5):
    star = ""
    for j in range(i+1):
        star += "*"
    print(star)

# 2번 방식
star = ""

for i in range(5):
    star += "*"
    print(star)


# 3번 방식(python)
for i in range(5):
    print("*" * (i + 1))

 
