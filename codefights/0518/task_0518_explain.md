## 문제 설명
changes[i][0]값이 lastBackupTime보다 큰걸 찾아내서 changes[i][1] 값을 리턴하는 문제 단, 중복이 있으면 안된다.

## TestCase
```
Input:
	lastBackupTime: 461620200
changes: 
[
 [461620475,17], 
 [461620543,29], 
 [461625137,24], 
 [461626523,60], 
 [461627714,78]
]
Output:
[17, 24, 29, 60, 78]
Expected Output:
[17, 24, 29, 60, 78]
Console Output:
Empty
```

## 새롭게 알게 된것
[Python3 Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)

sorted 함수에서 key에 lambda를 쓸 수 있다는걸 알게되었다.

sorted 함수는 Python Built-in 함수중에 하나로써
sort함수는 list만 가능하지만 **sorted는 dict, list, duple 모두 가능하다.**

```python
# sorted(iterable[, key][, reverse])

# dimensional list
# [[461620475, 17]]
# data[0] -> 461620475
# data[1] -> 17
sorted_list = sorted(changes, key=lambda data:data[1])
```