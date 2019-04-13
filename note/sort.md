# 정렬과 탐색 (Sort and Search)

* Stable
: Merge Sort, Insertion Sort, Bubble Sort

* Not Stable
: Quick Sort(typical in-place sort is not stable; stable versions exist.)
Heap Sort, Selection Sort(typical in-place sort is not stable; stable versions exist.)


## 1. 정렬 (Sorting Algorithm)

numbers라는 list의 요소들을 정렬시켜보자.

```

numbers = [int(param) for param in input().split(' ')]

```

### 1.1 비교 정렬(Comparison Sort)

    * Quicksort / Heapsort /Shellsort /Merge sort / Introsort / Insertion sort / Selection sort / Bubble sort / Odd–even sort / Cocktail shaker sort / Cycle sort / Merge insertion (Ford–Johnson) sort / Smoothsort / Timsort

#### 1.1.1 버블 정렬(Bubble Sort)

버블 정렬은 배열의 첫 원소부터 순차적으로 진행하며, 현재 원소가 그다음 원소의 값보다 크면 두 원소를 바꾸는 작업을 반복한다. 이런 식으로 배열을 계속 살펴보면서 완전히 정렬된 상태가 될 때까지 반복한다.

    * 평균 및 최악 실행시간 : O(n^2)
    * 메모리 : O(1)
    * 가장 느리다/ 잘 안 씀 / 큰 수를 가장 오른쪽으로 옮기기

* 코드 예시

```
for i in range(len(numbers)):
    for iteration in range(len(numbers) - (1 + i)):
        if numbers[iteration] > numbers[iteration + 1]:
            numbers[iteration], numbers[iteration + 1] = numbers[iteration + 1], numbers[iteration]
print(' '.join(str(num) for num in numbers))
```

#### 1.1.2 선택 정렬(Selection Sort)

배열을 선형 탐색(linear scan)하며 가장 작은 원소를 배열 맨 앞으로 보낸다(맨 앞에 있던 원소와 자리를 바꾼다.).
그 다음에는 두 번째로 작은 원소를 찾은 뒤 앞으로 보내 준다. 이 작업을 모든 원소가 정렬될 때까지 반복된다.
    * 평균 및 최악 실행시간 : O(n^2)
    * 메모리 : O(1)

* 코드 예시

```
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(' '.join(str(num) for num in numbers))
```

#### 1.1.3 삽입 정렬(Insertion Sort)

정렬되지 않은 배열을 정렬된 배열에 insert
    * 평균 및 최악 실행시간 : O(n^2)
    * 메모리 : O(1)

* 코드 예시 (1) 두 배열을 활용하는 방법 # 첫번째

```
list = []
for i in range(len(numbers)):
    is_inserted = False
    for j in range(len(new_list)):
        if numbers[i] < new_list[j]:
            is_inserted = True
            list.insert(j, numbers[i])
            break
    if not is_inserted:
        list.append(numbers[i])
print(' '.join(str(num) for num in new_list))
```

* 코드 예시 (2) 두 배열을 활용하는 방법 # 두번째

```
def insertion_sort(numbers: list) -> list:
    sorted_list = []
    for number in numbers:
        not_inserted = True
        for i in range(len(sorted_list)):
            if number < sorted_list[i]:
                not_inserted = False
                sorted_list.insert(i, number)
                break
        if not_inserted:
            sorted_list.append(number)
    return sorted_list
```

* 코드 예시(3)

```
def delete(list, index):
    new_list = list.copy()

    for i in range(index, len(list) - 1):
        print(new_list)
        new_list[i] = new_list[i+1]
    new_list.pop()
    return new_list
```

* 코드 예시(4)

```
def insert(list, index, new_element):
    new_list = list.copy()
    new_list.append(None)
    for i in range(index +1, len(list) - 1):
        print(new_list)
        new_list[i] = new_list[i+1]
        # new_list[index] = new_element
        # new_list += new_list[index]
    return new_list

result = insert(['a', 'b', 'c', 'd', 'e'], 1, 'f')
print(result)
```

#### 1.1.4 기수 정렬(Radix Sort)

    * 낮은 자리수부터 비교하여 정렬하는 알고리즘
    * 시간복잡도 : O(kn)
    * 데이터 전체 크기에 대한 기수 전체의 테이블이 비례하기 때문에.
    * stable
    * Non-Comparison Sort
    * 자리수가 없을 때 못 쓴다. ex. 벡터값 (1, 3), (2, 4), (3, 6)

#### 1.1.5 병합 정렬(Merge Sort)

[중요]

    * 평균 및 최악 실행시간 : O(nlogn)
    - 분할 => logn
    - 머지 => n
    * Quick Sort를 사용할 수 없을 경우 유용하다. 

#### 1.1.6 Heap Sort

    * 평균 및 최악 실행시간 : O(n^2) + O(nlogn)
    * 메모리 : 

#### 1.1.7 퀵 정렬 (Quick Sort) 

[중요]
    * 평균 : O(nlogn)
    * 최악 : O(n^2)
    * 메모리 : O(logn)

### 1.2 비-비교 정렬 (Non-Comparison Sort)

하나 하나 비교하는 것이 아니라, 고차원적인 성질을 비교하는 방법. 주로 정렬해야 하는 대상의 특징이 다를 때 사용한다. 예를 들어, type이 다를 때.

* 메모리 아끼면서 하는 방법?
* 구하는 방법에 관한 예시 : nC2
* 시간 복잡도 :  kn (단, 여기서 k는 자리수)