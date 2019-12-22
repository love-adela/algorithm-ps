## 1. GCD

### 1.1 Characteristics  

* Decomposition the two numbers to obtain a common argument.
* LCM(m, n) = m * n / GCD(m, n)
* GCD(p, GCD(m, n)) = GCD(GCD(p, m), n)

### 1.2 How to get GCD(Greatest Common Divisor) effectively?

#### [Euclidean Division]()

* [Description](https://en.wikipedia.org/wiki/Euclidean_division)
* Time Complexity : O(log(n+m))

## 2. Prime Number

When N is divided from 2 to N ** 1/2 (square root), the result of modulo computation is not a prime number if zero.

### 2.1 Primality Test

[Fermat's little theorem]()

* It's also called probabilistic primality test.
* Determine which number is likely to be prime number.
* [Description](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
* **소수 P에 대해 N < P의 N^P % P = N이라는 식이 성립**
소수 5보다 작은 수(1, 2, 3, 4)를 각각 5제곱해보자

```
4 ^ 5 (= 1024) % 5 = 4
3 ^ 5 (= 243) % 5 = 3
2 ^ 5 (= 32) % 5 = 2
1 ^ 5 (= 1) % 5 = 1
```

반면 합성수(composite number) 6으로 같은 연산을 하면 규칙이 보이지 않는다.

```
5 ^ 6 (= 15625) % 6 = 1
4 ^ 6 (= 4096) % 6 = 4
3 ^ 6 (= 729) % 6 = 3
2 ^ 6 (= 64) % 6 = 4
1 ^ 6 (= 1) % 6 = 1
```