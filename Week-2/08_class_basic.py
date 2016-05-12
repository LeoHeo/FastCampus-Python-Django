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

dir(jinhan)

