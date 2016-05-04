if True:
    print("True")

if False:
    print("False")


a = 13
b = 12

if a < b:
    print("a({a})가 b({b})보다 작다.".format( a=a, b=b))
else:
    print"a({a})가 b({b})보다 크다.".format( a=a, b=b))



# in, not in
animals = ["강아지", "고양이", "이구아나"]

if "이구아나" in animals:
    print("이구아나를 키우고 있습니다.")
else:
    print("이구아나를 키우고 있지 않습니다.")


"이구아나" in animals # True
"카멜레온" not in animals # True


age = 20

while age < 30:
    print("20대에 나이를 먹었습니다. 현재나이:{age}".format(age=age))
    age += 1


list( range(10) # [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

animals = ["강아지", "고양이"]

for animal in animals:
    print("{animal}".format(animal=animal))


# 변수 값을 사용안할때
for _ in range(10):
    print("Hello World")


# 별찍기


