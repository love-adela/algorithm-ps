1 이진검색
========
이진검색은 배열에 있는 인덱스 값을 범위를 좁혀 찾아내는 방식입니다.
순차 검색을 이용하면 처음부터 일일이 나올 때 까지 찾아야 하지만 이진검색은 중간 값을 기준으로 앞/뒤의 범위를 나누어 범위를 좁혀가며 값을 찾아나가므로 이 방법을 활용하면 검색 속도가 빨라집니다.

## 1.1 이진검색 의사코드

1. min = 1, max = n라고 둡시다.
2. max와 min의 평균을 구하되, 정수가 되도록 내림합니다.
3. 추측이 맞으면 끝냅니다. 숫자를 찾았습니다!
4. 추측값이 너무 작으면 min을 추측값보다 1 크게 설정합니다.
5. 추측값이 너무 크면 max를 1 작게 설정합니다.
6. 2단계로 돌아갑니다. 

* 알고리즘의 입력값과 출력값을 분명하게 설정하고 "평균을 구함" 이나 "끝냅니다" 같은 명령이 정확히 의미하는 바를 명시하면 의사코드를 훨씬 더 명확하게 만들 수 있습니다. 

## 1.2 배열 안에서 검색이 가능하도록 수정된 이진 검색 의사코드

* 참고 ) 입력값 : 배열 (array), array의 요소의 개수 n, 검색 대상의 수 target입니다. 결과 값은 array 속 target의 인덱스 값입니다.  

1. min = 0이고 max = n-1 이라고 합니다.
2. guess의 값은 max와 min의 평균값을 정수가 되도록 버림한 값입니다.
3. array[guess]의 값이 target과 같다면 검색을 멈춥니다. 타겟을 찾았습니다. guess를 결과값으로 반환합니다.
4. 추측값이 더 작다면 즉, array[guess] < target이라면, min = guess + 1으로 바꿉니다.
5. 아니면 추측값이 더 큽니다. 그럼 max = guess - 1로 바꿉니다.
6. 2 단계로 돌아갑니다. 

## 1.3 검색 대상이 배열에 없는 경우를 처리하는 이진 검색 의사코드

1. min = 0 이고 max = n-1이라고 합니다.
2. max < min이면 검색을 멈춥니다: target이 array에 존재하지 않습니다. -1을 반환합니다.
3. guess 의 값은 max 와 min 의 평균값을 정수가 되도록 버림 한 값입니다.
4. array[guess]의 값이 target과 같다면 검색을 멈춥니다. 타겟을 찾았습니다. guess를 결과값으로 반환합니다.
5. 추측값이 더 작았다면 즉, array[guess] < target이라면, min = guess + 1으로 바꿉니다.
6. 다른 경우로는 추측값이 더 클 수 있습니다. 그러면 max = guess - 1로 바꿉니다.
7. 2단계로 돌아갑니다.

### 1.3.1 의사코드를 어떻게 해야 자바스크립트 프로그램으로 바꿀 수 있을까요? 

1. 먼저 함수를 생성해야 합니다. 왜냐하면 입력을 받아서 값을 반환하는 코드를 작성해야 하고 또, 이 코드를 다른 곳에서 다른 입력값을 받아서 써야 하기 때문입니다. 함수의 매개변수로는 배열과 찾고자 하는 대상 값이 있고 반환할 값은 찾고자 하는 값의 위치를 나타내는 인덱스입니다.
2. 6단계는 2단계로 돌아가라고 합니다. 반복문처럼 보이네요. for또는 while 문 중 무엇을 써야 할까요? for 문을 꼭 사용하고 싶다면 그럴수도 있지만 이진검색에서 추측하는 인덱스는 for문과 같이 순서대로 커지지 않습니다. 처음에는 인덱스 12번을 추측하고 그 후에는 계산하여 18번으로 추측했습니다. 그래서 while 문이 더 좋은 선택입니다.

### 1.3.2 배열의 이진검색에서 고려해야 하는 요소도 있어요!

추측 게임 알고리즘을 짤 때 만든 의사코드에서는 중요하지 않았지만, 배열의 이진 검색에서는 한 가지 중요한 단계를 빠뜨렸습니다. 만약 찾고 싶은 숫자가 배열에 없다면 어떤 일이 일어날까요? 이 경우에는 binarySearch 함수가 돌려주어야 하는 인덱스값을 먼저 결정합니다. 이 값은 배열에서 인덱스가 될 수 없는 숫자여야 합니다. -1은 배열 내 인덱스가 될 수 없으므로 -1을 사용하기로 합시다. (사실 아무 음수 모두 괜찮습니다.) 앞서 선언한 min이 0이기 때문입니다.

## 1.4 의사코드가 실현된 자바스크립트 프로그램
* 이진 검색을 보다 효과적으로 시각화하기 위해 각 단계의 guess를 출력하는 println() 문을 추가하세요. 
* 참고 ) guess의 인덱스가 가리키는 요소의 값이 아닌 인덱스 자체를 출력해야 합니다.

<pre><code>
/* Returns either the index of the location in the array,
  or -1 if the array did not contain the targetValue */
var doSearch = function(array, targetValue) {
	var min = 0;
  var max = array.length - 1; // 첫 번째 인덱스는 1이 아니라 0에서 시작합니다. 
  var guess;
  var targetValue;
  var count = 0; //count 변수를 0으로 초기화시킵니다.
  while(max >= min){ //max 값이 min보다 커야 반복문이 실행됩니다.
      guess = Math.floor(( max + min )/2); // 받은 인자에 Math.floor 함수를 써서 가운데 인덱스 값의 소수점을 버릴거에요.
      println(guess); // 각 단계의 guess를 출력하게 할래요.
      count++; // 반복문이 실행될 때마다 카운트를 1회씩 증가시킵니다.
      if(array[guess] < targetValue){ // 우리가 추론한 guess 값이 targetValue보다 작을 경우,  
          min = guess+1;  //범위를 하나씩 더 늘립니다.
      }
      else if(array[guess]> targetValue){ //우리가 추론한 guess 값이 targetValue보다 클 경우,
          max = guess-1; // 범위를 하나씩 더늘립니다.
      }
      else { //추론한 guess 값이 targetValue와 일치하다면
          println(count); // 마지막 반복문에서 최종 카운트된 횟수를 출력합니다.
	  return guess; // guess를 반환합니다.
      }
    }    
	return -1; // 배열에 targetValue가 없을 경우, -1을 반환합니다. 즉 max < min이면 더이상 반복문을 돌리지 않습니다.
};

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

var result = doSearch(primes, 73);
println("Found prime at index " + result);

Program.assertEqual(doSearch(primes, 73), 20);
Program.assertEqual(doSearch(primes, 89), 23); // 다른 수도 검사해볼까요?
Program.assertEqual(doSearch(primes, 13), 5);  // 다른 수도 검사해볼까요?
</code></pre>



본 문서는 칸 아카데미의 알고리즘 강좌 중 이진검색 단원를 참조하였습니다.
출처: [칸아카데미](https://ko.khanacademy.org/computing/computer-science/algorithms/binary-search)


