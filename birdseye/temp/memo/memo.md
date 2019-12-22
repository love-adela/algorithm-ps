# string


## 문자열의 각 문자를 리스트에 담기

* 'string' => ['s', 't', 'r', 'i', 'n', 'g']

```
[letter for letter in string]
```

## 두 문자에 input을 각각 integer casting 하는 방법

```
a, b = map(int, input().split())
```

# sequence

# input이 무작위 시퀀스로 들어올 때 list로 나타내는 방법

```
[int(param) for param in input().split()]
# input : 32423 324792384 23489128
# output : [32423, 324792384, 23489128]
list(map(int, input().split())) # 아주 조금 더 빠르다
```

# list 아이템을 연산된 시퀀스로 출력하는 방법

```
print(' '.join(str(num) for num in numbers)

```

# hash

## key가 출현하는 횟수를 dictionary 형태로 찾는 방법

```
>>> {x:1 for x in 'hello'}
{'h': 1, 'e': 1, 'l': 1, 'o': 1}
>>> from collections import Counter
>>> Counter('hello')
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```
