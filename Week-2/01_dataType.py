a = 3
type(a) # int

a = 3.0
type(a) # float

# 다시 int로 변환
a = int(a)

#a = a + 1
a += 1

# 제곱
a * a
a * a * a

# 같은 코드가 계속 반복
a ** 2 # 2제곱
a ** 3 # 3제곱

# 문자열 끼리 덧셈가능
name = "허진한"
name + "님 안녕하세요"

print(name[0]) # 허
print(name[1:]) # 진한

# Python2 방식
# 많아지면 관리가 힘들어짐
"%s님 안녕하세요" % "안수찬"

# 많이 나아지긴 했으나 명시적이지 않음
"{0}님 안녕하세요.".format("안수찬") 


"{name}님 안녕하세요".format(name="허진한")

"안녕하세요. {name}님 안녕하세요. 저는 {course}를 수강하고 있습니다".format(name="허진한", course="웹프스쿨")


# Key Error
"안녕하세요. {name}님 안녕하세요. 저는 {course}를 수강하고 있습니다".format(name="허진한")

# List, Tuple, Dict, Set

# List => 순서가 있는 배열

animals = ["강아지, "고양이", "이구아나"]

# 추가
animals.append("물고기")

# 삭제
animals.pop(0)

# 고양이에서 고만 뽑아오기
animals[0][0]

# Tuple => List와 동일하지만 Element값이 변결이 될 수 없습니다.

width_and_height = (120, 240)
width, height = width_and_height

width # 120

heigth # 240

# Set => 집합
# 순서가 보장이 안되고, Element unique

name_set = set(["허진한", "허진한", "김승현", "홍길동"])

name_set #김승현, 허진한, 홍길동

# 중복제거의 가장 Python 다운 방법
name_list = {"안수찬", "안수찬", "안수찬", "김승현", "김승현"}
name_list = list(set(name_list))


# Dictionary
detail_dict = {"name": "홍길동", "age": 24, "phone_number": "010-2222-3333"}

del detail_dict["age"]

# get
detail_dict["name"]

## Boolean

# 아래와 같은 방법도 있지만
True & True

# 명시적으로
True and True

# 아래와 같은 연산이 있다면
# 1. 로직을 점검해라 좀 더 단순화 할 수 있는 방법을 찾아라
# 2. 아래 방법이 최선이라면 괄호를 쳐라

True and True or False
(True and True) or False
