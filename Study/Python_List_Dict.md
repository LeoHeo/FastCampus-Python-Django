#Python

##List & Dictionary 공통점 & 차이점
#공통점
 
~~~python
list = [1, 2, 3, 4]
dict = { 'one': 1, 'two': 2}

# Get Element
print(list[0]) -> 1
print(dict['one']) -> 1

# Delete Element
del(list[0]) # -> [2, 3, 4, 5]
del(dict['one']) # -> {'two' : 2}

# Length Check
len(list) # -> 4
len(dict) # -> 1

# Element in
2 in list # -> True
7 in list # -> False

# default dict.keys()
# dict == dicy.keys()
'one' in dict # -> True
'one' in dict.keys() # -> True
'on' in dict # -> False

1 in dicy.values() # - > True

#Clear
list.clear()
dict.clear()
~~~

#차이점
~~~python
list = [1, 2, 3, 4, 5]
dict = { 'one': 1, 'two': 2}

# 두번째의 요소를 가져올때 항상 2가 아님
# pop을 하고 나면 값이 바뀜
print(list[2]) # -> 3
list.pop(0)
print(list[2]) # -> 4

# dictionary는  키값으로 가져오기 때문에 항상 동일
~~~


#Tuple 
###Packing, Unpacking

~~~python
# Packing
x = 10
y = 20

packing = x, y
print(packing) # -> (3, 5)

# Unpacking
packing = (10, 20)
x, y = packing
print('x : {}, y: {}'.format(x, y)) # -> x: 10, y: 20

# Swap
# 여태까지 Swap을 할려면 temp변수를 만들어서 바꿔주는 작업을 했어야 했음
a = 10
b = 20

# before - Tuple Not Use
# 이제까지 내가 Java에서 하던 것
temp = a
a = b
b = a

# After = Tuple Use
a,b = b,a

# Swap이 이리도 간단히 되다니....-_-;;
~~~


### List, dictionary For loop
~~~python
dict = {'Test1': 1, 'Test2': 2, 'Test3': 3}
for key, value in dict.items():
	print('key : {}, value : {}'.format(key, value))


# For loop 어떻게 해서 key, value를 가지고 올수 았나?
# loop를 돌면서 딕셔너리 값(Tuple)들을 key, value로 unpacking
# 위에 for loop는 아래와 같이 축약 할 수 있음

for e in dict.items():
	print('key : {}, value : {}'.format(*e))

# 위와 같은 For loop 축약 가능
# *e -> 알아서 쪼개라는 의미
~~~