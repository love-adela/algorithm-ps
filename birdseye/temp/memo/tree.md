## Tree
### 정의 : Cycle이 없는 그래프
### 특징 : Graph의 부분집합
### 종류 
    * Binary Tree : 자식이 2개인 경우
        * Complete Binary Tree(완전 이진 트리)
        * Complete Binary Tree가 아닌 경우
    * N-ary Tree : 자식이 여러개인 경우
### 구성 : 
* Node : Graph에서 Vertex
* Root : 제일 부모인 애
* Depth : Root로부터 얼마나 떨어져있는가

### Binary Search Tree (BST, 이진탐색트리)] ,,, Ordered Map
 * Binary Tree인데 () 성질을 만족하는 트리.
  * Complete일 필요 없다.
  * 왼쪽 sub tree의 모든 값은 node의 값보다 작아야 하고, 오른쪽 sub tree의 모든 값은 node의 값보다 크다.
  * Python에서는 tuple로 짠다. 그러나 고칠 수 없다.
    ```
    Tree = (5,
                (3, None, (4, None, None)),
                (7, None, None),
    )
    ```
    수정하려면 class를 활용해야 한다.
    ```
    class Node:
        def __init__(self, ):
            pass
    ```
  * Invariant : 왼쪽 subtree의 값이 node 값보다 작아야 한다. && 오른쪽 subtree의 값이 node 값보다 커야 한다.
  * Time Complexity : Amortized O(log N)
  * Memory : 세타 N
  * Range Query : Amortized O(log N)
    * 만드는 방법 : skip
  * Insert : Amortized O(logN)
  * 최근 30개 : O(logN)


## Graph
### 구성
* Verte: 정점
  * 보통 Edge에 값을 저장한다. (리스트에 값을 저장하듯.)
  * Ex) Tuple 형식으로 (3, 7)
* Edge: 간선
* Cycle: 순환

--- 
## Splay Tree

### 특징

* 1985년

### Splaying 아이디어

---

## AVL

### 아이디어
얼마나 치우쳐져있는지 확인해서 치우쳐져 있지 않게 ~~

### 정의

### 특징
* 1962년
* BinarySearchTree의 일종
* 트리의 높이를 균형있게 제어(줄이는)하는 것이 핵심 -> 계산복잡성이 O(h)이기 때문에. --> h = Balance Factor

### 종류 

* rotation 방식에 따라 두 종류로 나뉜다.

* Invariant : 균형이 갖춰져 있는 상태
  * 균형 : Balance Factor (|왼쪽 - 오른쪽 자식의 높이| < 2)

#### (1) Single Rotation

#### (2) Double Rotation

rotation 한 번으로 원하는 결과를 못 낼 때 사용한다.
(U는 BF의 절대값이 2 이상이면서 새 노드와 가장 가까운 조상 노드, V는 U의 자식노드이면서 BF 절대값이 1이하)

* V가 U의 왼쪽 자식노드, V의 오른쪽 서브트리에 새 노드 삽입
* V가 U의 오른쪽 자식노드, V의 왼쪽 서브트리에 새 노드 삽입

### 구성

---
## Red Black Tree

### 특징

* 1972년
* 2-3-4 tree가 rb보다 cache friendly 하다.
  * 2 - 3 - 4 tree를 어떻게 binary로 만드는가?
  * 

---

## B Tree

### 특징

* 1971년

* 2 - 3 : order = 3
* 2 - 3 - 4 : order = 4
* 2 - 3 - 4 - 5: order = 5
* 2 - 3 - 4- ... - N : order = N

## 2 - 3

### 특징

* 1970년