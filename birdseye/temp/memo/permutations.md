# [pandita's algorithm](https://en.wikipedia.org/      wiki/Permutation#Generation_in_lexicographic_orde      r)

주어진 순서의 모든 순열을 체계적으로 생성하는 방법은 여러 가지가 있다. 고전적이고 단순하며 유연한 알고리즘 중 하나는 어휘목록 순서(lexicographic ordering)에서 다음 순열을 찾는 것을 기반으로 한다. 

- 반복되는 값을 처리할 수 있다. 이 경우 각각 구별되는  multiset 순열을 한 번 생성한다.

일반적인 순열의 경우, Lehmer 코드 값을 사전순으로 생성(factorial number system을 사용할 가능성이 있음)해, 이를 순열로 변환하는 것보다 훨씬 효율적이다.

(약하게) 증가하는 순서에 따라 순서를 정렬하는 것으로 시작하고(이 순서는 사전적으로 minimal permutation을 제공한다), 한 사람이 발견되는 한 다음 순장으로 진격하는 것을 반복한다. 이 방법은 14세기 인도의 나라야나 판디타(Narayana Pandita)로 거슬러 올라가, 자주 재발견되었다.
