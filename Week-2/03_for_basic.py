# list 출력방법
# 4번째 인덱스 파이썬으로 바꾸기
animals = ["강아지", "고양이", "이구아나", "물고기", "참새"]

# index 함수 사용하기
for animal in animals:
    index = animals.index(animal)
    if( index == 4):
        animals[index] = "파이썬"
        
print( animals)

# 왜 리스트는 dict같은 items()가 없나
# enumerate 사용
# (index, value) => Tuple
# 2번째 인덱스 닭으로 변경
for key, value in enumerate(animals):
    if( key == 2):
        animals[key] = "닭"

        
# value가 사용되지 않으니 아래처럼 바꿀수도 있음
# underscore
for key, _ in enumerate(animals):
    if( key == 2):
        animals[key] = "닭"
        

# dict for loop
# dict - 1
my_information = {
    "name": "허진한",
    "age": "28"
}

# 그냥 돌리면 키값만 받아옴
for info in my_information:
    print(info)

# Tuple로 받아옴    
for info in my_information.items():
    print( info)

# unpacking
for key, value in my_information.items():
    print( key, value)
