# 160520 Codefights

## 새롭게 알게 된것

[Python3 Sum Document](https://docs.python.org/3/library/functions.html#sum)

`map에서 한번에 형변환`을 할 수 있다는걸 알게 되었다.

```python
# str_list -> int_list
list( map( int, ['1', '2', '3'])) # [1, 2, 3]

# str_list -> float_listß
list( map( float, ['1', '2', '3'])) # [1.0, 2.0, 3.0]

# float_list, int_list -> str_list
list( map( str, [1, 2, 3])) # ['1', '2', '3']
list( map( str, [1.0, 2, 3])) #['1.0', '2', '3']

# sum함수를 사용해서 list 합계 구하기 가능
sum( list( map( int, ['1', '2', '3'])))

```