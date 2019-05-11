# 5 / 8 : Memory
* a is b -> 메모리 주소 등으로 같은 것인지 검사

* a == b -> 같은 내용을 가지고 있는지 검사

## array와 list

#### array : 물리적 인접성이 있다.

  * 미리 메모리를 할당해야 한다.
  * Array 타입이나 크기 제한이 있다.
    * int arr[10]
  * Direct Access (= Random Access)
    * Array에서 값을 조회할 때 시간복잡도는 O(1)이다.
    * index 번호를 알았을 때 바로 접근이 가능하다.
    * TODO: Memory Address / 컴퓨터구조 (32비트 운영체제에서의 메모리주소가 4바이트, 64비트는 ? 8)
  * Cache Hit가 잘 발생한다.
    * Cache Hit : 원하는 것이 Cache에 있다.... 여러 책을 빌려 꽂아두어 책장에 원하는 책이 있다.
      * Cache : CPU에 들어있다. (1 word: CPU가 처리하는 기본 단위)
        * Cache를 가져올 때 Cache Line(한 번에 가져올 수 있는 데이터의 개수)을 가져온다. 한 번 도서관에 갔다올 때마다 항상 5권을 반납하고 5권을 가져와야함. (CPU마다 권수는 다름. 어떤 CPU는 무조건 1kb를 반납하고 1kb를 가져와야함.)
      * Cache miss : 원하는 것이 Cache에 없다... 책 하나 보려고 도서관에 한 시간 걸려서 간다.
    * Cache란? Cache에 저장되면 더 빠르다.
      * https://ko.wikipedia.org/wiki/CPU_%EC%BA%90%EC%8B%9C
    * 원인: 지역성(locality) : 메모리에서 CPU 내의 캐쉬로 데이터를 가져왔을 때 근처 데이터를 한번에 가져옴. 어떤 데이터를 불러오면 근처에 있는 데이터를 참조할 확률이 높기 떄문에.
    * 최대한 가져올 수 있는 여러개의 데이터를 가져온다. 
    
  * register 단위와 data 단위와 word단위가 보통 일치.
    * 32 register = 32 data = 32 bit address...로 쉽게 구현
    - 32 bit CPU에서 24 bit address를 쓰는 경우도 있음. (충분하다. 32비트는 너무 크다고 생각했기 때문.)
    * 64 register에서의 문제 : 64 bit address 는 너무 광활한 주소이지 않냐. 32 bit data를 쓰기도 한다.
    * => 다양하게 단위 크기를 조합한다. // 64비트 데이터 모델 : LP64, ILP64, SILP 64, LLP64...운영체제가 정할 수 있음.
      - 예를 들어 C언어에서 int 자료형을 다음으로 표현한다. 
      - 8 bit computer : 1byte, 8 bit
      - 16 bit computer : 2byte, 16bit
      - 32 bit computer : 4byte, 32 bit
      - 64 bit computer : 8byte, 64 bit 데이터 모델을 사용.. -> 메모리나 디스크가 아까워서.


==========

#### Processor -> Cache -> Main Memory

#### list : 리스트 값의 타입이나 크기 제한이 없다.

  * python에서는 array가 없고 list를 활용한다.
    * 고급 언어여서. 더 나은 구조를 기본으로 쓰게 해준다.
    * 참고로 기본으로 dictionary를 사용하고 이는 hash table 구조를 취함.
  * Array와 달리 List는 배열의 크기를 미리 설정해두지 않아도 되는데, 대신 값을 조회할 때 direct access가 어렵다. 모든 값을 순회해야 함(Linked List). 즉, O(N)
  * Cache hit 잘 안 남.


눈눈쨩

눈눈님 설명 조리있게 자신 있게 잘 하심.

** 명확하게 말하는 습관을 들이자고 하심. ** 

눈눈님 칭찬 잘 하심.

#### Hash Table

* 배열 + 해쉬
  * 해쉬함수 : 어떤 데이터를 넣었을 때 고정된 길이의 다른 데이터로 맵핑해주는 함수

# 5/ 9 : Sorting Algorithm

#### 
