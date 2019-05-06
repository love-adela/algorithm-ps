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

## 