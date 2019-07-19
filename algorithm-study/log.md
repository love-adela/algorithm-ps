진도
========

### 스터디 시작 전 예습
- 3//7과 3/7의 차이
- `[100, *range(3), 200, *range(2)]` 언패킹
- a, b = [1, 2] 디스트럭팅
- ' '.join(['a', 'b', 'c'])
- 'a b c'.split(' ')
- 주요 내장함수 all any enumerate filter input iter len map max min open range slice sorted sum zip 사용법 익히기
- 제네레이터와 이터레이터가 뭔지
- input() print() 함수 사용법. 예를들어 print(end='asdf') 이렇게 함수에 옵션줄수있는거 있는데 저런것들 다 https://docs.python.org/3/library/functions.html#print 여기서 찾아보기
- list comprehension

### 2019-03-01
기초
- Big-O notation의 정의 (상한)
- Big-Omega (하한), Big-Theta (상하한) 의 정의
- Time Complexity (시간복잡도), Space Complexity (공간복잡도)가 뭔지
- Amortized Time Complexity가 무엇인지

소팅
- 정렬 알고리즘들의 분류: 정렬 알고리즘은 Comparison Sort와 Non-comparison Sort로 나뉜다
- Comparison Sort는 크게
  - O(n^2) 소트: bubble sort, selection sort, insertion sort
  - O(nlogn) 소트: quick sort, merge sort, heap sort
  - O(n^2) 소트와 O(nlogn) 소트를 섞은것: intro sort, tim sort
- Non-comparison Sort는
  - radix sort, counting sort
- bubble sort, selection sort, insertion sort 직접 구현함

### 2019-03-09
- Recursion (재귀가 뭔지, Base Case가 뭔지)
- Memoization
- 유클리드 호제법: 최대공약수 계산기 만들기

### 2019-03-10
- brew, brew cask 사용법 익히기
- zsh 터미널 세팅하기
- VSCode 사용법 익히기
- 백준 1002번 어디가 틀렸는지 같이 보기

### 2019-03-17
ㅇㅅㅇ

### 2019-03-24
ㅇㅅㅇ

### 2019-03-30 ~ 2019-03-31
ㅇㅅㅇ

### 2019-04-06
Divide and Conquor, 분할정복
-   이름의 유래; https://en.wikipedia.org/wiki/Divide_and_rule 이민족들을
    정복했을 때 어떻게 숫자가 더 열세인 정복자들이 수적으로 더 다수인 이민족들을
    통치할 수 있는가? 여러 집단으로 쪼개어, 특정 집단에게만 특권을 몰아주고
    반대쪽 집단을 차별하는 방식으로 갈등을 조장하면, 적들이 단결하지 못해
    약해진다. (마키아벨리의 전술론) 이를 Divide et Impera라고 불렀고 여기서 유래함
-   분할정복 알고리즘의 예시
    - 이진탐색 (Bisect, Binary Search); 시간복잡도가 왜 O(logN) 인가?
    - 머지소트; 시간복잡도가 왜 O(N logN) 인지 계산해보기

Quick Sort
-   작동원리 설명
    - 영단어 Pivot의 뜻; [pívət]  피벗, 회전축, 회전축으로 회전하다
    - Pivot으로 지정한 원소는 한번 움직인 이후 절대로 자리를 바꾸지 않는것이 핵심
      힙소트나 머지소트처럼 배열이 정렬되는 과정에서 쓸데없이 움직이는 횟수가 적음
-   시간복잡도 계산해보기; 어느때가 최악의 경우인지 말할 수 있어야함
    - Amortized Time Complexity: O(N logN)
    - Time Complexity: O(N^2)

Sorting Algorithm의 Stability
-   Stable Sort, Unstable Sort는 무엇인가?
-   왜 Unstable Sort가 더 빠른가; 제약이 더 적으니까
-   Stable Sort는 어느때에 필요한가
-   지금까지 공부했던 소팅알고리즘들의 Stability 전부 대답하기
    - Bubble Sort, Insertion Sort, Merge Sort는 확실하게 stable sort
    - Selection Sort, Heap Sort는 확실하게 unstable sort
    - Quick Sort는 stable/unstable 버전 둘 다 존재한다

Cache, 캐시
-   Cash랑 발음이 비슷해서 $ 라고도 표시함
-   영어공부
    - Trade-off의 뜻; 둘중 하나를 취사선택하거나 적절히 타협해야하는 경우
    - Pareto Frontier의 뜻; 현재 선택할 수 있는 트레이드오프중 최선인것들의 모음
      https://en.wikipedia.org/wiki/Pareto_efficiency#/media/File:Pareto_Efficient_Frontier_1024x1024.png
      이 그림 참고
    - Pareto Optimal의 뜻; Pareto Frontier에 있는것들을 골랐다
    - Pareto Improvement의 뜻; Pareto Frontier를 오른쪽 위 방향으로 이동시켰다,
      더 나은 선택지를 만들었다
-   메모리에서의 Trade-off; 싸면 느리고, 빠르면 비싸다
    - NOTE: 싸다/비싸다 = 단위가격당 용량이 싸다/비싸다, 메모리가 싸다는 뜻은
      용량이 많다는 말과 같음
-   Locality of Reference; 컴퓨터가 메모리를 사용하는 패턴을 옆에서 지켜봤더니
    관찰된 특징들
    - Temporal Locality; 한번 접근한 메모리는 근시일 내에 또 접근할것이다
    - Spatial Locality; 한번 어딘가를 접근했으면, 다음에는 멀리 떨어진곳이 아닌
      그 근처를 접근할것이다
    - 이 외에도 몇가지 더 있으나 Temporal이랑 Spatial이 제일 중요함

    ```c
    // Locality of Reference 예시

    for (int i = 0; i < 100; ++i) {
      // 한번 사용한 i를 자꾸만 사용함. Temporal Localtiy

      data[i] = 100;
      // data[i]에 접근했다면, 다음번엔 data[i+1]에 접근할것임. Spatial Locality
    }

    이 외에도 많은 코드가 이런식임
    ```

-   처음에는 정부에서 대학들에게 금덩이같이 비싼 메모리를 엄청 많이 컴퓨터에
    붙여줬으나, 돈낭비라는것을 깨닫게 되었다. 어차피 100GiB의 RAM을 붙여줘도,
    대부분의 메모리는 접근하지 않고 자고있고 극소수의 메모리만 활발하게 사용함.
    (Power Law https://en.wikipedia.org/wiki/Power_law ) 그래서 용량 많고 느린
    메모리와  용량 적고 빠른 메모리를 동시에 쓰는것이, 빠른 메모리를 비싼돈주고
    왕창 다는것보다 싸다
-   Memory Hierarchy https://en.wikipedia.org/wiki/Memory_hierarchy
    - Cache의 아이디어; 자주 접근하는 메모리는 작지만 더 빠른 캐시에 임시로
      가져와서 사용하면 효율적이겠다
    - 보조기억장치의 아이디어; 자주 접근하지 않는 메모리는 느리지만 더 저렴하고
      용량이 많은 HDD같은 장치에 저장하면 효율적이겠다
-   2019년에 흔히 보이는 Memory Hierarchy; 느리고 싼거에서, 비싸고 빨라지는 순서로
    - 자기테이프: >100TiB, 공공기록물 백업하는곳이나 학교 서버 백업장치같은곳에서 씀
    - HDD: 1~100TiB, 싸고 용량 많으나 느림
    - SSD: 0.1TiB~1TiB, HDD보다 빠르나, 비싸고 용량 적음
    - RAM: 4GiB~32GiB, 주 기억장치
    - L3$: 4MiB ~ 32MiB, 여러 코어가 공유하는, CPU에 하나씩 있는 큰 캐시
    - L2$: 1MiB ~ 4MiB, 코어별로 하나씩 갖는 캐시
    - L1d$, L1i$: ~0.5MiB, 코어별로 하나씩 갖는 더 빠르고 더 작은 캐시. 데이터를
      저장하는 L1d cache와, instruction(명령어)를 저장하는 L1i cache로 나뉜다
-   캐시 간단한 작동원리 설명
    - RAM 한곳을 접근할때, 그 근처 인접한 수 KiB를 한번에 다 가져와서 CPU에 놓고
      사용한다. 캐싱된 영역은 쓸때마다 매번 RAM에다가 직접 쓰는게 아니라 CPU에
      있는 캐시에다가만 쓰고 RAM에는 반영을 안한다. 그 캐시를 그만 쓰게될 때
      그제서야 RAM에 한번에 쓰게된다.
    - Direct Mapped Cache, Set Associative Cache 등은 설명 안함
    - Cache Eviction Rule (LRU, 등) 도 설명 안함

Cache Friendlyness, 캐시 친화적인 코드/알고리즘이란 무엇인가
-   Schlemiel the Painter's algorithm, 러시아 페인트공 알고리즘
    https://en.wikipedia.org/wiki/Joel_Spolsky#Schlemiel_the_Painter's_algorithm
    페인트통을 들고 움직이면 빠른데 바보같이 하고있음
-   컴퓨터의 Memory Hierarchy는 Locality of Reference가 맞다는 가정 하에
    설계되어있음. 한곳을 비슷한 시간간격 내에 자주 접근하고, 한곳을 접근했다면
    미래엔 전혀 쌩뚱맞은곳이 아니라 그 근처를 접근할것이라는 가정이 맞다면
    컴퓨터가 빠르게 돌아감
-   뒤집어서 말하면, Locality of Reference를 안지키면 캐시가 작동을 안해서
    느려진다는 듯임
    - 특정 메모리를 반복해 읽는게 아니라, 한번씩만 읽기/쓰기 하고 더이상 안쓰기
    - 메모리를 한번 접근할때에 한번에 비슷한 위치의 메모리를 읽는게 아니라 자꾸
      쌩뚱맞은 위치의 메모리에 접근함
-   예시; 똑같이 배열 안에있는 값들의 합을 더하는 프로그램이지만 성능이 다름
    ```
    const int data[10000] = { /* 값이 들어있음 */ };

    int sum1 = 0;
    for (int i = 0; i < 10000; ++i) { sum1 += data[i]; }

    int sum2 = 0;
    for (int i = 0; i < 10000; ++i) {
      const int index = i*7691 % 10000;
      sum2 += data[index];
    }
    // 7691과 10000이 서로소여서, 저렇게 루프돌면 data[10000]의 모든 숫자를
    // 한번씩만 순회하기때문에 합이 구해지기는 함. 그러나 저렇게 짜면 접근을
    //
    //   data[0] + data[7691] + data[5382] + data[3073] + ...
    //
    // 이런식으로 하게됨
    ```
-   Cache Friendlyness란?
    - Cache Unfriendly; 위와 같이 Locality of Reference를 안지켜서 느린 프로그램들을 부르는 말
    - Cache Friendly; Locality of Reference를 잘 지켜서 빠른 프로그램들을 부르는 말
-   시간복잡도뿐만이 아니라 아예 연산회수가 정확히 일치하는데도 실제로
    구현해보면 성능차이가 나는경우가 있음. 그 경우 보통 원인이 다 Cache
    Friendlyness 때문임.
-   연습문제
    - 왜 Selection Sort보다 Insertion Sort가 더 빠를까요; 길이가 10만 이상인
      엄청나게 큰 배열을 정렬한다고 상상하고 메모리 액세스 하는 패턴을 들여다보자
    - 왜 Merge Sort보다 Quick Sort가 더 빠를까요; Quick Sort가 쓸데없는 이동
      숫자가 더 적기도 하지만, 더 캐시프렌들리하다. 왜인지는 역시 길이가 10만
      이상인 엄청나게 큰 배열을 정렬한다고 상상하고 메모리 액세스 하는 패턴을
      비교해보자

Radix Sort, 기수정렬
-   Radix, 기수의 의미: 10진법을 쓸때엔 10이 기수다. 16진법을 쓸때엔 16을
    기수라고 부른다
-   우리가 숫자를 비교하거나 정렬할때, 대충 자리수가 몇개인지 보고 맨앞자리가
    몇인지 보지 숫자를 맨끝까지 읽으면저 정렬하지 않는다. 이걸 그대로 코드로
    옮긴것임. 작동원리는 잘 설명해주세요
-   MSD, LSD의 의미; Most Significant Digit, Least Significant Digit
    - 이진수에서 제일 큰비트를 MSB, 제일 낮은비트를 LSB라고 부르는것과 같음
-   보통 정수, 고정소수점 실수, 문자열(사전순 정렬)에 대고 쓸 수 있음.
    부동소수점 정수에는 쓰기 곤란함 (왜인지 알으려면 부동소수점이 어떻게
    구현되어있는지 알아야하는데 패스)
-   시간복잡도 계산해보기; 왜 O(kN) 인가?
-   구현할 때 주의할점; 자리수가 다를 때 숫자는 오른쪽정렬되지만 문자열은
    왼쪽정렬된다. 그림 참고
    ```
    1004    cat
      42    apple
     113    heat
    ```

Hash Table, 해시테이블
-   우리가 `{'a': 100, 'b': 200}` 이런거 흔히 쓰는데, 저거 구현할 때 쓰는게
    해시테이블, 거의 모든 언어에 다 들어있음
-   Hash Map, 해시맵이라고도 함
-   해시테이블은 아주 많이 쓰는 자료구조이고, 기본 원리 자체는 간단한데, 실제로
    짜려고하면 매우 복잡하다. 왜 복잡한지는 해시콜리전 챕터에서 설명
-   해시테이블 작동원리; 키를 숫자로 변환시켜주는 함수를 하나 만든 뒤, 큰 배열
    잡아서 거기에 저장하기. 잘 설명해주세요
-   저 "키를 숫자로 변환시켜주는 함수"를 Hash Function, Hasher라고 부른다
-   Hash Table의 시간복잡도; Hash Function이 상수시간만에 작동한다는 가정 하에
    - 삽입 연산의 Amortized Time Complexity: O(1)
    - 읽기 연산의 Amortized Time Complexity: O(1)
    - 삭제 연산의 Amortized Time Complexity: O(1)
    - 최악의경우가 있다는 뜻임. 디테일은 해시콜리전 챕터에서 설명

Hash Function
-   h : T → Integer [0, N)
    - 문자열, 정수, 구조체 등 임의의 타입 T를 받아 0이상 N미만 반환하는 함수
    - [0, N) 구간 표기 무슨뜻인지 다들 아시죠? https://en.wikipedia.org/wiki/Interval_(mathematics)#Including_or_excluding_endpoints
-   해시 함수가 지키면 좋은 성질들
    - 입력이 다른데 출력하는 정수가 같은경우(Hash Collision, 해시충돌)가 적어야한다
      - 왜 충돌이 적어야하나요? 다음챕터에서 다룸
    - 분포가 균일해야한다 (Uniform Distribution)
      - 왜 분포가 균일해야하나요? 다음챕터 끝나면 대답할 수 있게됨

Hash Collision
-   비둘기집의 원리에 의해 원소를 일정이상 많이 넣으면 해시충돌은 무조건 일어나게되어있음
    https://en.wikipedia.org/wiki/Pigeonhole_principle
-   일정이상 많이 넣지 않아도 원소를 충분히 많이 넣으면 확률적으로 일어날 수 있음
-   해시충돌이 일어났더니 딕셔너리가 작동 안하면 얼마나 빡칠까
    ```
    dict['A'] = 'cat'
    dict['B'] = 'dog'

    print(dict) # 했더니 { 'A': 'cat' } 만 출력되면??
    ```
-   우리는 해시충돌이 일어나는 경우에도 멀쩡하게 동작하는 딕셔너리를 만들어야함.
    그 전략이 크게 두가지 있다. (각각의 원리는 그림 보면서 잘 설명해주세요)

    1.  Separate Chaining; 느리다, 구현이 단순하다
        https://en.wikipedia.org/wiki/Hash_table#Separate_chaining_with_linked_lists
    2.  Open Addressing; 빠르다(Cache Friendly, SIMD Friendly), 구현이 더 복잡하다

-   우리가 쓰는 거의 모든 해시테이블은 구현이 복잡해도 되니까 빠른게 더 중요해서
    Open Addressing으로 구현되어있음. 근데 Open Addressing 쓴다고 땡이 아니라
    고려해야하는 상황이 더 있음

Open Addressing에서 원소 삭제 처리
-   https://gankro.github.io/blah/hashbrown-insert/ 참고
-   (이거 복잡한데 종찬님이랑 석주님 계시니 설마 설명 못하진 않으리라 믿습니다)
    Open Addressing을 쓰는바람에 이렇게 똑같은 해시를 갖는 원소 여러개가 딱
    붙어있는 상황에서

    `[ ..., A, B, C, D, ... ]`

    C를 삭제하면

    `[ ..., A, B, 🤔, D, ... ]`

    A-B 와 D 체인이 끊겨서, D는 lookup 하지 못하게 된다. 이를 해결하는 방법이
    두가지가 있는데

    1.  Backshifting: 땡기기. `[ ..., A, B, D, ... ]`
        - C 뒤에있던걸 땡겨서 이렇게 붙이면 해결
        - 삭제의 시간복잡도가 더이상 O(1)이 아니게됨
    2.  Tombstone: 묘비남기기 `[ ..., A, B, _, D, ... ]`
        - C 자리에 tombstone을 남겨서 "여기에는 값이 남아있지 않지만, 이 뒤에 더
          lookup해야할 값들이 남아있으니 지나가세요" 를 설명
        - 삭제의 시간복잡도가 O(1)로 유지됨
        - 구현이 복잡한게 단점

    이 역시 보통 더 빠른 Tombstone으로 구현되어있음

-   사실 Tombstone 배치 외에 할게 더 있는데, 해시충돌때문에 여러 값이 붙어있으면
    끝 지점을 표시할 수단도 필요함 `[ ..., A, B, _, D, 🥅, ... ]`

    왜 이런게 필요한지 간단히 요약하자면

    `[ ..., A, B, C, X, Y, Z, ... ]`

    A B C의 해시는 10으로 같았고, X Y Z 의 해시가 13으로 같았다고 쳐보자. 딱히
    A B C X Y Z 여섯개 모두의 해시가 충돌하진 않았으나 우연히 저 세개가 딱
    붙어있게되었음. 끝지점을 표시 안하면 이런 상황이 생길 수 있는데 이런
    상황에서 어떻게 느려지는지 생각해보자

Pearson Hashing https://en.wikipedia.org/wiki/Pearson_hashing
-   결국 해시알고리즘이 해시테이블의 품질을 결정하는데, 우리가 면접장에서 간단한
    해시테이블을 직접 구현해야할 때 쩌는 해시함수를 짜고있기엔 해시함수의 구현은
    너무 복잡하다. 간편하게 쓸 수 있고 적당히 퀄리티가 좋은 해시함수임.
    작동원리는 잘 설명해주세요

Hash Set 만들기
-   Set, 집합: 배열이랑 똑같은데 안에 중복된 원소가 있으면 안됨
-   Set은 키만 들어있고 값이 없는 딕셔너리와 동치임
    ```
    {
      'A': None,
      'B': None,
      'C': None,
    }
    ```
    딕셔너리는 키의 중복을 허용하지 않으니까!
-   실제로 Hash Set 구현도 그냥 값이 없는 Hash Table로 되어있음

눈으로 ASCII 읽는법
-   2진수<->10진수<->8/16진수 변환하는법은 다들 아시죠?
-   아스키는 [0, 128) 의 값을 가짐. 2^7 이하이기때문에, 무조건 맨 앞자리가
    0이다. 만약에 아래처럼 8글자마다 0이 반복된다면 이건 아스키가 아닌지 일단
    의심해봐야한다.
    `01001000 01100101 01101100 01101100 01101111`
-   그리고 이진수가 `010_____` 꼴이면 대문자 알파벳이고, `011_____` 꼴이면
    소문자 알파벳이다. 예를들어
    `01000001` 은 대문자중 첫번째 글자니까 A
    `01100101` 은 소문자중 다섯번째니까 e
    이진수를 8글자로 끊었을때 자꾸 `010_____` `011_____` 가 반복되면 아스키
    영어가 아닌지 의심해야한다.
-   아래는 보면 알파벳 8번째, 5번째, 12번째, 12번째, 15번째 글자니까 hello다.
    그리고 맨앞글자는 대문자, 그 외에는 소문자이므로 'Hello'임.
    `01001000 01100101 01101100 01101100 01101111`
-   이건 기본이고 정말 중요한건 이진수 보고 이게 쌩 아스키만 있는지, UTF-8인지,
    EUC-KR(CP949) 인지 구분하는게 필요한데 이건 매우 실용적으로 자주 사용됨

XOR, Exclusive OR 하는법
-   XOR은 보통 `^` 기호를 써서 표시한다.
-   진리표, Truth table이란 무엇인가?
-   XOR의 진리표 (그림참고)
-   XOR은 왜 이름이 XOR일까; OR랑 같은데 두 입력 모두 1인 경우만 배제하기때문에
-   XOR 하는법; 13 ^ 7 은?
    1. 양변을 이진수로 표시; 0b1101 ^ 0b111
    2. 자리수가 다른경우, 앞에 가상의 0이 붙어있다고 생각하면 됨; 0b1101 ^ 0b0111
    3. 같은 자리수 비트들끼리 XOR 해주면 됨; 0b1010 = 10
    13 ^ 7 == 10
-   0b111, 0o123, 0x1a 저 앞에 붙은 0b 0o 0x 다 무슨뜻인지 아시죠? binary,
    octal, hexadecimal 의 약자

SIMD가 뭐에요?
-   아까 Tombstone이 Backshifting보다 더 나은 이유 거론하면서 잠깐 등장함
-   Single Instruction Multiple Data
-   이런 코드 있을때에 절대로 배열 안에있는 정수를 하나 하나 더하지 않음
    ```
    int data[128] = { /* 데이터 */ };
    for (int i = 0; i < 128; ++i) {
      data[i] += 1;
    }
    ```
-   잘 설명해주세요

MSD Radix Sort vs LSD Radix Sort
-   성능은 별 차이 안나고 LSD Radix Sort쪽이 구현하기 쉬워서 보통 LSD Radix
    Sort를 씀

Hash Table의 Capacity와 Dynamic Resizing
-   해시테이블이 50% 이상 차면 크기를 두배로 늘려줘 이런식으로 테이블 리사이징을 함
-   All-at-once Rehashing: 문제는 해시알고리즘 특성상 테이블 크기가 변하면 기존
    테이블 안에있던 원소들을 모조리 움직여줘야한다. 보통은 해시 안에 원소를
    백만개씩 넣고 그러지 않으니 괜찮지만, 해시가 너무 커서 All-at-once
    rehashing을 못쓰는 경우엔 어떻게할까?
-   Incremental Rehashing: 일시적으로 기존 테이블과 크기가 두배로 커진 테이블
    두개를 동시에 운용하고, 일시적으로는 삽입/접근 연산을 할때에 테이블 두개를
    모두 접근함. 테이블 두개를 모두 접근할때마다 기존 테이블에 있던 원소를 새
    테이블로 옮겨감.
-   (그래프 참고) Incremental Rehashing은 All-at-once rehashing과 비교하면,
    한번에 리해싱하느라 특정시점에 쏠린 부하를 여러 시간에 조금씩 퍼뜨린것과
    같음

> 전주팟에서 내가 먼저 진도 나간 뒤 서울팟에서 같은거 함
>
> 전주팟: 지현 낙엽 아델라 디디
> 서울팟: 종찬 눈눈 석주

### 2019-04-13
참여가 저조해서 쉼.


### 2019-04-21
- Invariant
- Graph (짧게)
- Tree
  - 정의
  - 각종 용어설명
  - Binary Tree
    - Complete Binary Tree
  - N-ary Tree
- Binary Search
- Ordered Map vs Unordered Map 비교
- BST
  - BST의 Invariant
  - find, insert, range query

### 2019-05-06
- 트리 순회
  - BFS, DFS
  - pre-order, in-order, post-order
  - postfix notation
- 트리 회전

### 2019-05-11
- Splay Tree 작동원리와 아이디어
  - Splaying 작동원리, Zig, Zig-Zig, Zig-Zag
- AVL 작동원리 (insert만)
- 2-3-4 Tree 작동원리 (insert만)
- 2-3-4 Tree와 RBTree가 왜 동치인지
- RBTree가 왜 좋은지 RBTree의 invariant가 왜 성립하는지
  - 왜 '제일 깊은 leaf의 깊이'와 '제일 얕은 leaf의 깊이'가 2배 이상 차이가 안날까
- RBTree와 AVLTree의 비교
  - 왜 RBTree가 더 좋을까
- 2-3 트리, 2-3-4 트리, 2-3-4-5 트리, 2-3-...-N트리를 BTree라고 부름
- BTree가 왜 RBTree보다 Cache Friendly한지
- 발달 역사
  - 1962 AVL
  - 1970 2-3 Tree
  - 1971 BTree
  - 1972 RBTree
  - 1985 Splay
- malloc() 만들 때 어떻게 RBTree를 쓰는지

### 2019-05-18
오늘 한거
- XO, 눈눈님 안계실 때 한것중 중요한거 리뷰
  - Big O, Big Omega, Big Theta
- Trie
  - N진트리
  - Prefix Tree, Suffix Tree
  - Radix Sort 와 아이디어가 비슷함
  - Bit-wise Trie (= Binary Tree)
  - find, insert, delete 하기
- 연습 문제
  - https://boj.kr/5052
  - https://boj.kr/11590

### 2019-05-26
- 그래프
  - 유향그래프, 무향그래프
  - 듀얼
- 그래프 표현
  - 포인터, 인접행렬, 인접리스트, 인접집합/맵
  - Weighted, Directed, 자기자신 가리키기, 정점에 값넣기, 두 정점 사이의 간선이
    복수개인 경우
- 그래프 탐색
  - DFS, BFS

### 2019-06-02
- Dijkstra Algorithm
  - 기본 원리
  - Metric Space가 뭔지, 거리함수의 정의
  - Dijkstra 알고리즘을 못쓰는 경우
- Heap, 우선순위 큐
  - Binary Heap 작동원리, Heap invariant
  - 완전이진트리 배열로 표현하는법
  - 힙소트

### 2019-06-29
12015번 품

### 다음에
- A*
- 피보나치 N번째 항 구하기
- 피사노 주기
- IEEE 754 부동소수점 작동원리
- 큰수
- 계산기 만들기
