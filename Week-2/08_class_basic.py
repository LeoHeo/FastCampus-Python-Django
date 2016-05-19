# Object Oriented Programmning
# 객체(데이터, 각각의 데이터를 처리하는 방법) <=> 객체: 메세지를 전달

# 함수형 프로그래밍 => Lambda, Lambda Operator, List Comprehension

# Object에 대한 이해
# 허진한 학생
# 학생이 무엇인가?

class Student():
    __campus = "패스트캠퍼스"
    
    def __init__(self, name, age):
        '''
        init => initialize( 초기화하다)
        Student() => __init__ 함수가 실행되는 것
        '''
        self.name = name
        self.age = age
        print("학생. {name}{age}가 태어났습니다.".format(
            name = self.name,
            age = self.age
        ))
    
    # 자기소개를 할 수 있다.
    def introduce(self):
        print("안녕하세요. 저는 {campus}다니는 {age}살 {name}입니다".format(
            campus = self.__campus,
            name = self.name,
            age = self.age
        ))
        
# 근데 아래 코드는 올바르지 않다.
# 이름을 입력을 안했을때 => 객체가 생성되면 안된다.
# jinhan = Student()
jinhan = Student("허진한", 28)

# 바꿀수가 있다
# _Student__campus를 부르지 않기로 약속함
jinhan.campus = "경쟁사"
jinhan.introduce()

# jinhan Object안에 있는 함수나 변수보기
dir(jinhan)


class Rectangle():
    #width = ""
    #height = ""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self): # 면적
        return self.width * self.height
    
    def girth(self): # 둘레
        return (self.width + self.height) * 2
    
    def is_bigger(self, another):
        return self.area() > another.area()

rec1 = Rectangle(10, 10)
rec2 = Rectangle(20, 30)

print( rec1.area())
print( rec1.girth())

rec1.is_bigger(rec2)
rec2.is_bigger(rec1)


# information class만들고
# csv파일 열어서 information List 만들기

class Information():
 
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def print_introduce(self):
        print("{name}님 주소는 {address}입니다".format(
            name = self.name,
            address = self.address
        ))   


with open("../../users.csv", "r") as f:    
    # f.readlines()는 파일 오픈당 한번만 유효함
    # 그래서 위에 주석처리한거나 아래 List Comprehension 둘중에 하나만 써야함
    information_list = [
        Information(
            user.split(",")[0],
            user.split(",")[1].replace("\n", "")
        )
        for user
        in f.readlines()
    ]
    
    for info in information_list:
        info.print_introduce()
