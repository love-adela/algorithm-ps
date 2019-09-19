# Invariant (불변성)
- 특정 시스템에서 변하지 않는 성질

* (참고) Item 찾는 Query
  * unsorted array : O(N) ... Unordered Map => 문제 Domain(최적화)을 사용한 최적화
    * 탐색 속도가 빠르다.
    * 메모리를 많이 사용한다. (buffer를 마련해야 하기 때문에.)
    * 예시로 Hash Table이 있다.
    * 이 경우 삽입 속도: Amortized O(1)
    * Range Query : O(logN)
  * sorted array : O(log N) ... Ordered Map
    * 탐색 속도가 느리다.
    * 메모리를 N만큼 사용한다.
    * 원소 추가하는 것이 수행이 너무 어렵다, 즉 비싸다?.
    * 삽입 속도 : O(N)
    * Range Query : O(1)
    * Binary Search Tree를 사용할 수 있다.

* Range Query(범위를 정해서)
  * (예시) Femiwiki 게시글 중 3월 ~ 6월 게시글
  * Time Complexity : O(log N)

* (예시) Insertion Sort
  * Sorted List와 Unsorted List를 두고 Unsorted List의 item을 Sorted List로 삽입시키는 방식
  * Sorted List는 항상 정렬되어야 한다는 Invariant를 가진다.