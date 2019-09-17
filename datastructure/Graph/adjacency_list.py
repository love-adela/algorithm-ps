# dictionary를 이용해 인접리스트 만들기 

a, b, c, d, e, f = range(6)
N = [{b:2, c:1, d:4, f:1}, {a:4, d:1, f:4}, {a:1, b:1, d:2, e:4}, {a:3, e:2}, {a:3, b:4, c:1}, {b:1, c:2, d:4, e:3}]
print(b in N[a]) # True
print(len(N[f])) # degree
print(N[a][b]) # (a, b) 의 간선 가중치

# dictionary 안에 set 을 활용해 유연하게 인접리스트 만들기

a, b, c, d, e, f = range(6)
N = {'a': set('bcdf'), 'b': set('adf'), 'c':set('ae'), 'e':set('abc'), 'f': set('bcde')}
print('b' in N['a']) # True
print(len(N['f'])) # degree
