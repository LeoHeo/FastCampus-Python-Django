# Test 1
# 1~100까지의 숫자중 3또는 5로 나누어 떨어지는 수를 지정하는 list만들기
# 2가지 방법으로 만들어보기
# List Comprehension 1개 and map, filter, reduce 사용해서 1개

# List Comprehension
[
    i 
    for i 
    in range(1, 100+1) 
    if i%3 == 0 or i%5 == 0
]

# filter
list(
    filter(
        lambda x: x%3 == 0 or x%5 == 0,
        range(1, 100+1)
)

# Test 2
# 3의 배수가 입력되면 "fast" 5의 배수가 입력되면 "campus" 15의 배수가 입력되면 "fastcampus"를 출력해라

# 내가 했던 방법
# 15의 배수는 3의 배수 + 5의 배수
def print_fastcampus():
    result_list = []
    for i in range(1, 100+1): 
        word = validation_fastcampus(3, i, "fast")\
            + validation_fastcampus(5, i, "campus")
    
    return result_list
            

def validation_fastcampus(divide, number, word):
    return word if number % divde == 0  else ""


# 함수처리 안하고 List Comprehension으로
fast_list = [
    "fast" if number % 3 == 0 else ""
    #validation_fastcampus(3, number, "fast")
    for number
    in range(1, 100+1)
]

campus_list = [
    "campus" if number % 5 == 0 else ""
    #validation_fastcampus(5, number, "campus")
    for number
    in range(1, 100+1)
]

fastcampus_list = [
    fast_list[i] + campus_list[i]
    for i
    in range(100)
]


# Test3
# 삼각형 별찍기
def triangle_star():
    count = int(input("몇 줄의 별을 찍으시겠습니까?"))
    for i in range(count + 1):
        #print("  " * (count - i) + "* " *(2 * i - 1)) # 별크기가 2배
        print(" " * (count - i) + "* " * (i + 1))



# Test4
# dictionary의 사용법 익히기
# 에러 찾아서 디버깅
def we_are_the_best(name, **kwargs):
    
    result_word = "{name}님은 {school}과정을 통해 {company}로 최종 {goal} 히셨습니다.".format(
        name = name,
        #company = company,
        #goal = goal,
        #school = school
        # 위가 원본 문제 dict는 값을 가져올때 kwargs[key]로 가져와야 함
        
        # Debugging
        company = kwargs["company"],
        goal = kwargs["goal"],
        school = kwargs["school"]
    )
    
    return result_word


value = {
    "school": "웹 프로그래밍 스쿨",
    "company": "패스트캠퍼스",
    "goal": "합격"
}

# we_are_the_best("허진한", **value)