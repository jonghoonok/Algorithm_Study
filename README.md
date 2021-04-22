# Algorithm

기초 알고리즘부터 심화까지 이론 정리 및 문제 풀이를 업로드하는 저장소

숫자로 시작하는 문제는 [Leet Code](https://leetcode.com/)문제

문자로 시작하는 문제는 [백준](https://www.acmicpc.net/) 문제이다. (G4_5052_전화번호목록은 Gold4 레벨의 5052번 문제라는 뜻)



참고자료

- 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 나동빈
- 알고리즘 문제 해결 전략 - 구종만



[TOC]

## 0. 알고리즘 문제 해결에 편리한 문법



### 1. Python

입출력

- 입력되는 데이터가 많은 경우 `sys.stdin.readline()` 이용
  - `input()` 과 거의 동일하게 이용할 수 있음
  - `split()` 을 이용하는 경우가 아니면 오른쪽에 줄 바꿈 기호가 남으니 `sys.stdin.readline().rstrip()` 필요



파이썬 문자열 처리 관련 함수

- 대문자, 소문자
  - `string.upper()` : 대문자로 변환
  - `string.lower()` : 소문자로 변환
- 문자열 바꾸기
  - `string.replace(string1, string2)` : 문자열 내의 문자열1을 문자열2로 변환
  - 일부 글자를 바꾸거나 삭제할 수 있고, 공백을 없애는 데 편리함
  - 변환하면 string이 바뀌는 것이 아니라 **새로운 문자열을 리턴함**
- 문자열 찾기
  - `string.find(word)` : 찾는 문자열이 처음 나오는 위치 리턴, 없으면 -1 리턴
  - `string.count(word)` : 해당 문자열의 갯수를 리턴
- 문자열 슬라이싱
  - `string[start:end]` : start에서 end-1번 인덱스에 해당하는 문자열을 추출
  - `string[::2]` (2개씩 건너뛰며 추출), `string[::-1]` (뒤에서부터 출력)
- 문자열 분리, 결합
  - `string.split(word)` : word를 기준으로 분리
  - `"word".join(string)` : string의 각 원소 사이에 word를 삽입 
- 문자열 공백 제거
  - `string.strip()` : 양쪽 공백 제거
  - `string.lstrip()` : 왼쪽 공백 제거
  - `string.rstrip()` : 오른쪽 공백 제거
  - `string.strip(letter)` : 양쪽에서 letter가 나오지 않을 때까지 제거
  - `string.lstrip(letter)` : 왼쪽에서 letter가 나오지 않을 때까지 제거
  - `string.rstrip(letter)` : 오른쪽에서 letter가 나오지 않을 때까지 제거
  - `string.strip(ab)` : 양쪽에서 a 또는 b가 나오지 않을 때까지 제거
- 아스키 코드 관련
  - `chr(num)` : 아스키 코드를 입력받아 문자를 출력
  - `ord(letter)` : 문자를 입력받아 아스키 코드를 출력



리스트 관련 함수

- `list.reverse()` : 리스트를 뒤집어줌
  - 리턴 값 없이 리스트 내부에서 실행되고, 원소가 없을 경우 에러 발생
  - `list[::-1]` 과 같은 기능을 하는데, 이 쪽이 빠르다고 함
- `list.insert(index, x)` : list 리스트의 index에 x를 삽입함
- `del list[index]` : list 리스트의 index번 째 원소를 삭제함
- 리스트도 enumerate를 지원함
  - `for i, n in enumerate(list)` 하면 앞은 인덱스, 뒤는 값이 됨 



딕셔너리 관련

- defaultdict

  - 존재하지 않는 키를 조회할 경우 해당 키에 대한 딕셔너리 아이템을 "기본값을 기준으로 " 생성함
    - 일반 딕셔너리는 에러메세지를 반환
    
    - 기본값은 int 기준 0임
    
    - ```python
      counts = collections.defaultdict(int)
      for word in words:
          counts[word] += 1
      ```

- Counter

  - 아이템의 갯수를 계산해 딕셔너리로 리턴함

  - ```python
    a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
    b = collections.Counter(a)
    # b는 {5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1}
    ```

  - `b.most_common(2)`를 하면 b에서 가장 빈도가 높은 2개의 요소 (5, 3), (6, 2)를 담은 리스트를 반환함
  
- get()

  - key를 이용하여 value를 얻음
  - key가 존재하지 않는 경우 에러메시지를 반환하는게 아니라 None을 반환한다는 특징이 있음

- values()

  - 딕셔너리의 값들을 묶어서 반환
  - list() 안에 넣어주면 리스트 형태로 받을 수 있음



파이썬 기본 함수

- `max()`

  - key에 들어가는 함수를 활용하여 해당 함수를 처리한 결과 중 최댓값을 구할 수 있음
  - 예) `max([1, 0, -2, 3, -5], key=abs)` : 절댓값 기준으로 찾기 때문에 -5가 나옴
  - 예2) `max(counts, key=counts.get)` : 딕셔너리 counts 중 value가 가장 큰 것의 키를 구할 수 있음

- `zip()`

  - 2개 이상의 시퀀스를 짧은 길이를 기준으로 1대1 대응하는 튜플 시퀀스를 만들어줌

  - 예시

    - ```python
      a = [1, 2, 3, 4, 5]
      b = [2, 3, 4, 5]
      c = [3, 4, 5]
      
      # [(1, 2), (2, 3), (3, 4), (4, 5)]
      list(zip(a, b))
      
      # [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
      list(zip(a, b, c))
      ```

- Asterisk

  - Unpack을 해 주는 연산자
  - 예시
    - `print(*fruits)` 를 하여 리스트 fruits에 있는 원소들을 구분하여 한 번에 출력
    - `list(zip(*collections.Counter(nums).most_common(k)))` : 튜플이 담긴 리스트를 반환하는 most_common 함수의 결과값을 zip으로 묶으면 튜플 내부의 값끼리 묶는 것이 아니라 튜플이 통으로 나오기 때문에 원하는 결과를 얻을 수 없어 unpack을 해준 후에 묶음 



## **1. 그리디 알고리즘**

> 







## **2. 탐색**

> 

 

### 2.1. 순차 탐색



보초법



#### 투 포인터

> 정렬된 배열에서 두 개의 포인터를 이동시키며 원하는 값을 찾음



#### 슬라이딩 윈도우

> 고정 사이즈 윈도우를 이동시키며 탐색
>
> 정렬되지 않은 배열에서도 사용 가능



### 2.2. DFS

> 깊이 우선 탐색
>
> 백트래킹을 통해 뛰어난 효용을 보임



재귀로 구현한 DFS

```python
def recursive_dfs(v, visited):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            recursive_dfs(w, visited)
    return visited
```





반복으로 구현한 DFS

```python
def iterative_dfs(v):
    visited = []
    stack = [v]
    while stack:
        t = stack.pop()
        if t not in visited:
            visited.append(t)
            for w in graph[t]:
                stack.append(w)
    return visited
```



#### Backtracking

> 해결책에 대한 후보를 쌓아가다 가능성이 없다고 판단되는 즉시 후보를 포기(backtrack)
>
> 트리를 탐색하다가 불필요한 부분을 버리는 것을 가지치기(pruning)라 함





### 2.3. BFS

> 너비 우선 탐색: 출발점으로부터 가까운 순서대로 탐색
>
> 최단 경로를 구하는 문제에 주로 사용됨



큐를 이용하여 구현

```python
def iterative_bfs(v):
    visited = [v]
    queue = [v]
    while queue:
        # 파이썬으로 큐는 잘 사용하지 않으니 덱을 사용한다. 여기서는 큐 이용
        t = queue.pop(0)
        for w in graph[t]:
            if w not in visited:
	            visited.append(w)
    	        queue.append(w)
    return visited
```





### 2.4. 이진 탐색

> 정렬된 데이터에서 탐색 범위를 절반씩 좁혀가며 탐색
>
> O(logN)



재귀를 이용하여 구현

```python
def binary_search(arr, target):
    def search(left, right):
        if left > right:
            return -1
        
        mid = (left+right)//2
        if target < arr[mid]:
            return search(left. mid-1)
        elif target > arr[mid]:
            return search(mid+1, right)
        else:
            return mid
    
    return search(0, len(arr)-1)
```



반복을 이용하여 구현

```python
def binary_search(arr, target):
    n = len(arr)
    l, r = 0, n-1
    while l <= r:
        mid = (l + r) // 2
        if target < arr[mid]:
            r = mid-1
        elif target > arr[mid]:
            l = mid+1
        else:
            return mid
    return -1
```





파이썬에서는 그냥 모듈을 쓰자





## **3. 정렬**



### 3.1. O(N^2)

> 실무에서 쓸 일은 없지만...



#### 3.1.1. Bubble Sort

문제 해결 기본 아이디어랄 것도 없다. 하나씩 비교해서 크면 뒤로 넘긴다.

해결 방법

```python
for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
```



#### 3.1.2. Selection Sort

문제 해결 기본 아이디어

1. 배열 내 **가장 작은 원소를 찾고** 
2. 해당 원소를 **제일 앞에 있는 원소와 swap**한 후 다시 반복



해결 방법

```python
for i in range(len(arr)-1):
    # 배열 내에서 가장 작은 원소를 찾아서 인덱스 i에 저장
    minId = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[minId]:
            minId = j
    # 찾았으면 (for문이 끝났으면) 정렬되지 않은 수 중에 제일 앞의 수와 swap
    arr[minId], arr[i] = arr[i], arr[minId]
```



#### 3.1.3. Insertion Sort

> 이미 정렬된 배열에 대해서는 O(N)에 끝나는 정렬



문제 해결 기본 아이디어

1. 배열의 두 번째 원소부터 다음을 반복
2. 자신의 **앞에 있는 원소들과 하나씩 비교하여, 자신이 작으면 앞으로 이동**하고 그렇지 않으면 멈춤
   - 제일 작은 수는 맨 앞으로 이동하는 식으로 오름차순 정렬됨



해결 방법

```python
# 첫 번째 원소는 놔두고 두 번째 원소부터 시작
for i in range(1, len(arr)):
    # 현재 보고 있는 원소 arr[i]를 앞에 있는 수들과 비교
    for j in range(i, 0, -1):
        # 앞의 수가 더 작다면 swap하여 앞으로 이동, 아니면 stop
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
```



### 3.2. O(NlogN)



#### 3.2.1. Quick Sort

> 가장 많이 사용되는 정렬 알고리즘
>
> 평균적으로 O(NlogN)이지만 최악의 경우 O(N^2)



문제 해결 기본 아이디어

- 기준 데이터를 설정하고 **기준보다 큰 데이터와 작은 데이터의 위치를 바꿈**
  - 기준을 정하는 방식에 따라 Hoare Partition, Lumoto Partition이 존재
  - Hoare는 맨 앞을, Lumoto는 맨 뒤를 pivot으로 설정
- Hoare는 다음과 같이 정렬함

1. `i=1, j=len(n)-1`로 설정하여 각각 오른쪽과 왼쪽으로 이동시키면서 pivot과 비교
   - pivot보다 작은 데이터를 왼쪽에, 큰 데이터를 오른쪽에 위치시킴
2. i와 j가 교차되면 pivot과 j를 swap
3. 다음 pivot에 대해서도 반복



해결 방법

```python
def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을때까지
        while left <= end and arr[left] <= arr[pivot]: left += 1
        # 피벗보다 작은 데이터를 찾을때까지
        while right > start and arr[right] > arr[pivot]: right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        # 최소한 right 왼쪽으로는 전부 피벗보다 작음이 보장되기 때문
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)
```



#### 3.2.2. Merge Sort

> Stable sort로 최선과 최악 모두 O(nlogn)의 성능을 보임
>
> 분할 정복의 진수를 보여주는 알고리즘



문제 해결 기본 아이디어

1. 배열을 가장 작은 단위(1개씩)까지 쪼갠다
2. 작은 배열은 정렬한 후 2개씩 병합하면서 다시 정렬된 배열을 구성한다
3. 원래 배열의 크기가 될 때까지 반복하여 원래 배열을 정렬된 상태로 만든다



해결 방법

```python
def merge_sort(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    
    # 왼쪽과 오른쪽을 각각 정렬한 후 병합
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
```



### 3.3. 기타 정렬

> 상황에 따라 O(NlogN)보다 빨라질 수 있으므로 그 상황을 기억해뒀다 활용하자



#### 3.3.1. Count Sort

> O(N+K)이므로 데이터 중 최대값이 너무 크지만 않으면 대개의 경우 아주 빠름



[문제 해결 기본 아이디어]

데이터의 **모든 범위를 담을 수 있는 배열**을 만들고 거기에 데이터를 **한 번 씩만 채움**

배열을 선언 → 데이터를 순회하면서 해당 숫자와 같은 인덱스의 배열의 값을 1씩 추가한다 → 끝



[해결 방법]

```python
# 데이터의 최대 범위만큼의 길이를 갖는 배열 선언
count = [0]*n

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```



#### 3.3.2. Radix Sort



## **4. DP**



### 4.1. LIS(Longest Increasing Subsequence)

> 수열 nums 내 가장 긴 증가하는 부분 수열의 길이는 얼마인가?



[백준 11053번](https://www.acmicpc.net/problem/11053)

[나무위키](https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4)



**문제 해결 기본 아이디어**

1. 수열을 순차적으로 돌면서 
2. 현재 보고 있는 **nums[i]보다 작은 동시에 LIS의 마지막 원소인 수**를 찾음
   - 순차적으로 찾으면 O(N^2), 이진 탐색하면 O(NlogN)
   - 찾았다: 현재 보고 있는 수가 LIS의 마지막 원소가 됨, LIS의 길이 += 1
   - 못 찾았다
     - O(N^2): 업데이트 필요하지 않으므로 무시
     - O(NlogN): 업데이트 필요(이진 탐색 위해서 오름차순 정렬 해줘야)



**해결 방법**

- O(N^2)인 방법

  - ```python
    # nums[i]를 마지막 원소로 하는 '증가하는 순열'의 길이를 담는 배열
    LIS = [0]*n
    for i in range(n):
        # nums[i]보다 작은 수 중에, 증가하는 수열의 길이를 최대가 되게 하는 인덱스j를 찾음
        temp = 0
        for j in range(i):
            if nums[j] < nums[i] and LIS[j] > temp:
                temp = LIS[j]
        LIS[i] = temp + 1
    
    # LIS배열 내에서 최댓값을 출력하면 종료
    print(max(LIS))
    ```

- O(NlogN)인 방법

  - nums 내에 존재하는 증가하는 부분수열들을 마지막 원소의 크기에 따라 오름차순으로 정렬함

    - 먼저 **부분수열의 길이 별로, 해당 길이의 수열 중 가장 작은 마지막 원소를 저장하는 배열**을 작성
    - 부분수열들의 마지막 원소 중 nums[i] 바로 다음으로 큰 수를 찾음
    - 해당 원소를 nums[i]로 갱신해 줌: 해당 부분수열이 더 작은 수를 마지막 원소로 가져야 더 긴 증가하는 부분수열을 가질 수 있음 
    - 부분수열들의 마지막 원소의 크기가 오름차순으로 정렬됨 

  - ```python
    # 이진탐색을 하기 위한 배열 LIS
    # 첫 번째 인덱스는 부분순열의 길이, 두 번째 인덱스는 해당 부분순열의 마지막 원소
    LIS = [[1, nums[0]]]
    for i in range(1, n):
        # nums[i]가 LIS에서 몇 번 째 위치로 갈 수 있는지 탐색  
        index = binary(LIS, 0, len(LIS)-1, nums[i])
        if index > len(LIS)-1:
            LIS.append([LIS[-1][0]+1, nums[i]])
        else:
            LIS[index] = [LIS[index][0], nums[i]]
    
    # LIS배열 내에서 최댓값을 출력하면 종료
    print(LIS[-1][0])
    ```



### 4.2. LCS(Longest Common Subsequence)

> 두 수열의 부분수열들을 비교했을 때 공통의 부분수열이 되는 것 중에 가장 긴 것은?



[백준 9251번](https://www.acmicpc.net/problem/9251)



**문제 해결 기본 아이디어**

![LCS](https://wikimedia.org/api/rest_v1/media/math/render/svg/11898811d5c6af9b5b110a69e14feadcc459e663)



**해결 방법**





### 4.3. Palindrome

> 앞뒤가 똑같은 전화번호



[백준 10942번](https://www.acmicpc.net/problem/10942)



**문제 해결 기본 아이디어**

1. 팰린드롬을 이루려면, 해당 수열의 선두와 후미는 같은 수여야 한다
2. 선두와 후미를 제외한 내부의 수열이 팰린드롬을 이룬다면 해당 수열은 팰린드롬이다



**해결 방법**

1. s번째 수에서 e번째 수까지의 수열이 팰린드롬인지 알 수 있게 하는 N x N 배열을 작성 

2. 먼저 길이 1인 수열은 무조건 팰린드롬이므로,  반복문을 이용해`arr[i][i] = 1` 입력

3. 길이 2부터 n까지의 수열이 팰린드롬인지 판별하기 위해, 기본 아이디어를 이용

   ```python
   # 먼저 길이1 팰린드롬과 길이2 팰린드롬(연속한 두 수가 같다면)에 대해 dp에 True를 기록
   for i in range(1, n+1):
       dp[i][i] = 1
       if nums[i-1] == nums[i]:
           dp[i-1][i] = 1
   
   # 길이 3부터 n까지의 팰린드롬을 기록        
   for i in range(3, n+1):
       for j in range(1, n-i+2):
           # 시작과 끝이 같고 그 내부가 팰린드롬을 이룬다면 팰린드롬
           if nums[j] == nums[j+i-1] and dp[j+1][j+i-2]:
               dp[j][j+i-1] = 1
   ```



### 4.4. Traveling Sales Person

> 외판원 순회 문제



[백준 2098번](https://www.acmicpc.net/problem/2098)



**문제 해결 기본 아이디어**

1. 먼저 "순회"이므로 어느 지점에서 출발해도 결과는 같음: 0번 도시에서 출발한다 가정
2. 지금까지 방문한 도시의 목록으로 배열이 아니라 **비트마스킹**을 이용
3. 지금까지 방문한 목록으로부터, **앞으로 모든 도시를 순회하는 데 필요한 비용 중 최솟값**을 취해 나가면서 계산을 진행(동적 계획법)



**해결 방법**

1. n번 도시를 방문하고 있을 때 지금까지 방문한 모든 경우에 대해 앞으로 필요한 최소한의 비용을 담을 배열 DP를 `dp = [[ING]*(1<<n) for _ in range(n)]`과 같이 만든다

2. 나머지는 재귀적으로 구현하되 dp의 값이 None이 아니라면(이미 계산을 수행했다면) 리턴하여 중복 제거

   ```python
   # 현재 위치, 방문한 기록
   def travel(start, visit):
       # 모든 도시를 다 순회했다면
       if visit == check:
           # 마지막 도시에서 출발 도시로 돌아가는 길이 있다면 값을, 아니면 INF 리턴
           return cost[start][0] or INF
   
       # 이미 해당 출발점에 대해 계산이 이루어졌다면 바로 리턴: 중복 제거
       if dp[start][visit] is not None:
           return dp[start][visit]
   
       temp = INF
       for i in range(n):
           # i로 가는 길이 존재하고, 아직 방문하지 않았다면
           if cost[start][i] and visit & (1<<i) == 0:
               temp = min(temp, travel(i, visit|(1<<i))+cost[start][i])
       # 현재 위치와 현재까지 방문한 목록에 대응되는 최솟값을 갱신
       dp[start][visit] = temp
   
       return temp
   ```



### 4.5. Kadane's Algorithm

> 어떤 배열의 최대 부분합을 어떻게 구할 것인가?



문제 해결 기본 아이디어

1. 배열 arr에 대해 i번 인덱스까지의 최대 부분합을 dp[i]라고 하자
2. `dp[i] = max(dp[i-1], dp[i-1]+arr[i])`



해결 방법은 생략^^



## **5. 최단 경로**



### 5.1. Dijkstra

> 음의 가중치가 없는 그래프의 **한 정점에서 모든 정점까지의** 최단거리를 구하는 알고리즘



[나무위키](https://namu.wiki/w/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

[백준 1753번](https://www.acmicpc.net/problem/1753)



**문제 해결 기본 아이디어**

1. 출발점으로부터 각 노드 까지의 최단 거리를 담을 배열 D[V]를 선언
   - 값은 INF로 설정
2. 모든 노드를 방문할 때까지 다음을 반복함
   - 현재 노드로부터 갈 수 있는 임의의 노드에 대해 `D[A] + dist[A][B]`와 `D[B]`를 비교
   - 둘 중 더 작은 값으로 D[B]를 업데이트
   - 현재 노드의 모든 주변 노드에 대해 같은 작업을 실시
   - 현재 노드의 상태를 방문 완료로 바꾸고, 미방문 노드중 D[V]값이 가장 작은 곳을 방문해서 반복함



**해결 방법**

- O(V^2)

  - 다익스트라가 원래 고안한 방법

  - ```python
    visit[start] = 1
    distance[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    # 모든 노드를 방문하며 거리를 업데이트
    for i in range(v-1):
        # 미방문 노드 중 출발점과의 거리가 최단인 곳을 탐색: O(V^2)
        now = get_smallest_node()
        visit[now] = 1
        for edge in graph[now]:
            cost = distance[now] + edge[1]
            # 다익스트라의 핵심: 출발점-now + now-주변노드 vs 출발점-주변노드 거리 비교
            if cost < distance[edge[0]]:
    ```

- O((V+E)logV)

  - 우선순위 큐를 이용한 방법

  - E는 한 노드와 연결된 주변 노드의 수

  - 각 노드마다 출발점으로부터 현재까지 최단거리 계산에 VlogV, 이웃노드의 최단거리 갱신에 ElogV 필요

  - ```python
    # 각 노드의 최단거리를 "업데이트"하는 데 사용하는 우선순위큐
    q = []
    heapq.heappush(q, (0, start))
    # 출발점으로부터의 각 노드의 최단거리를 저장하는 배열: 최종 결과
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 우선순위 큐는 거리가 짧은 것부터 먼저 처리함
        # 같은 노드에 대해 거리가 더 짧은 경로를 처리했다면 다음부터는 처리할 필요 없음
        # dist가 갖고 있는 정보(큐에 저장된 거리)와 distance(처리된 거리)를 비교
        if distance[now] < dist:
            continue
        # now의 주변 노드들을 탐색
        for edge in graph[now]:
            cost = dist + edge[1]
            if cost < distance[edge[0]]:
                distance[edge[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    ```



**수학적 증명**

귀납법으로 증명 가능 [네이버 블로그](https://m.blog.naver.com/ao9364/221986534307)

*그래프 내 최단 경로가 모두 다익스트라 알고리즘에 의거하지는 않는다*  는 가정을 세우고 이를 반박해보자.

- 임의의 꼭짓점 u에서부터 v까지 다익스트라 알고리즘에 의한 최단경로를 상정하고, 그 위에 노드 w가 있음

- 이 때 w와 u의 최단경로가 다익스트라 알고리즘에 따른 최단거리를 갖지 않는다고 가정하면
- u-w와 w-v의 거리의 합이 u-v의 거리의 합보다 짧아져야 함
  - u-v는 다익스트라 알고리즘에 의한 최단거리를 갖기 때문에, 이것은 u-w거리 + w-v거리와 같아야 함
- 그럼 u-v사이에 최단경로보다 더 짧은 경로가 존재해야 하므로 모순
  - 따라서 u-w 사이에도 다익스트라 알고리즘에 따른 최단경로보다 더 짧은 경로는 존재하지 않음
  - 이를 그래프 내 모든 노드로 확장할 수 있음
  - 모든 노드는 다익스트라 알고리즘에 의해 최단경로를 구할 수 있음  



### 5.2. Floyd-Warshall

> 그래프의 모든 노드 간의 최단 거리를 구하는 알고리즘
>
> 음의 가중치를 가지는 그래프에서도 사용 가능하다



[백준 11404번](https://www.acmicpc.net/problem/11404)

[2021 카카오 신입공채 1차 코딩테스트 4번](https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/)



**문제 해결 기본 아이디어**

1. 기본적으로 다익스트라와 같은 원리: 출발점 - 노드 뿐 아니라 모든 노드에 대해서 확장
2. i-j 거리와 i에서 임의의 노드 k + k-j 거리를 비교해 더 짧은 쪽으로 i-j 거리를 업데이트
   - 이걸 모든 노드 k에 대해서 반복하여 i-j의 최단거리를 얻는다
3. 같은 것을 모든 노드에 대해 실행한다



**해결 방법**

- 반복문 3개를 중첩하되, **가운데 노드 k가 제일 위에 와야 함**

  - 이건 [위키백과](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)에 잘 설명되어 있는데, 요약하자면 다음과 같음
  - i에서 j로 가는데, 1~k번 사이의 노드만 경유할 수 있다고 할 때 최단거리를 `path(i, j, k)`라고 하자
  - 위 상황에서 i에서 j로 가는 **모든 경로는 k를 경유하는가 or 경유하지 않는가** 로 분리됨(DP)
  - 따라서 `path(i, j, k)`는 `min(k를 경유하는 경로, k를 안 경유하는 경로)`가 됨 
    - k를 안 경유하는 경로 중 최단거리는 `path(i, j, k-1)`임
    - k를 경유하는 경로 중 최단거리는 `path(i, k, k-1) + path(k, j, k-1)`임
  - 그러므로 k=1에서 모든 i, j에 대해 최단거리를 구하고, k=N이 될 때까지 반복하면 모든 쌍의 최단경로를 찾을 수 있음

- ```python
  graph = [[INF]*(V+1) for _ in range(V+1)]
  
  # 자기 자신으로 가는 거리는 0으로 초기화
  for a in range(1, V+1):
      graph[a][a] = 0
  
  # 노드 a에서 b로 가는 거리 c를 입력받아 그래프 작성
  for _ in range(E):
      a, b, c = map(int, input().split())
      graph[a][b] = c
  
  # 점화식에 따라 각 노드 k에 대해 a에서 b로 가는 최단거리 갱신
  # a-b로 직접가는 것보다 a-k-b로 가는 거리가 짧으면 갱신
  for k in range(1, V+1):
      for a in range(1, V+1):
          for b in range(1, V+1):
              graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
  ```



## **6. 그래프 이론**



### 6.1. Disjoint Sets

> 공통 원소가 없는 두 집합



두 트리가 서로소 집합인지 확인하려면 **UNION**연산을 통해 root가 다른지 확인해본다

```python
parent = [0] * V

# 먼저 모든 노드에 대해 자기 자신을 부모로 갖도록 설정함
for i in range(V):
    parent[x] = x

# 재귀적으로 자신의 root를 찾는 함수
def find_parent(x):
    if parent[x] != x:
        # 부모 노드를 root로 갱신하여 root에 빠르게 접근할 수 있도록 함(경로 압축)
        parent[x] = find_parent(parent[x])
    return parent[x]

# 노드 x와 노드 y의 root를 같도록 함: UNION
# 여기선 번호가 더 작은 노드를 부모로 가게 합침
def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
	    parent[y] = x
    else:
        parent[x] = y
```

root별로 구분하여 서로소 집합을 나눌 수 있음



**사이클 판별하기**

1. 각 간선을 확인하며 간선에 연결된 두 노드의 root를 확인
   - root가 다르다면 union을 수행
   - **root가 같다면 사이클이 존재하는 것**
2. 모든 간선에 대해 1을 반복



### 6.2. Spanning Tree

> 하나의 그래프가 있을 때, **모든 노드를 포함하면서 사이클이 존재하지 않는** 부분 그래프

![spanning tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Minimum_spanning_tree.svg/1200px-Minimum_spanning_tree.svg.png)

- 스패닝(신장) 트리는 **DFS/BFS를 이용해 선형 시간에서 찾을 수 있음**
- 병렬 및 분산 컴퓨팅에서 중요하다고 함
  - 상세 내용은 차후에 추가
- 최소한의 비용으로 이러한 신장 트리를 만들 수 있는 알고리즘을 **최소 신장 트리 알고리즘**이라 함
  - Boruvka's algorithm	  O(*m* log *n*)
  - Prim's algorithm            O(*m* log *n*) or O(*m* + *n* log *n*)
  - Kruskal's algorithm       O(*m* log *n*)



#### 6.2.1. Prim's Algorithm



#### 6.2.2. Kruskal's Algorithm



**문제 해결 기본 아이디어**

1. 모든 간선에 대해 비용의 오름차순으로 정렬
2. 간선을 비용순서대로 추가하는데, 사이클을 발생시킨다면 추가하지 않음
   - 비용이 적은 순서대로 사이클 없이 추가하기 때문에 말 그대로 최소 비용 신장 트리가 됨



**해결 방법**

- 사이클을 발생시키는지 UNION을 이용하여 판별하면서 구현

  - **집합 자료구조를 이용**해서 판별하면 훨씬 빠르게 동작함

- ```python
  cnt = 0
  
  for i in range(E):
      px = find_root(edge[i][0])
      py = find_root(edge[i][1])
  
      # cycle check
      if px != py:
          cnt += 1
          union(px, py)
      
      # MST의 간선의 수는 노드의 개수 -1 이다
      if cnt == V-1:
          break
  ```



### 6.3. Topology Sort

> 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
>
> 선수과목을 고려한 학습 순서 설정을 예로 들 수 있음



[백준 2252번](https://www.acmicpc.net/problem/2252)



**문제 해결 기본 아이디어**

1. **진입차수**가 0인 노드를 큐에 넣는다
   - 진입차수: 특정한 노드로 **들어오는** 간선의 개수
   - 진입차수가 0인 과목은 선수과목이 없는 1학년 과목이라 할 수 있음
2. 큐가 빌 때까지 다음을 반복한다
   - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 제거한다
   - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
   - 주의) 사이클이 존재한다면 **모든 노드를 방문하기 전에 큐가 빔**
     - 사이클 내 노드들은 진입차수가 0이 되지 않기 때문



**해결 방법**

모든 노드와 간선들을 한 번씩 확인하므로 시간 복잡도는 O(V+E)

```python
# 진입차수: 해당 노드로 들어오는 간선의 갯수
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, v+1):
    # 진입차수가 0인 노드를 큐에 넣는다
    if indegree[i] == 0:
        q.append(i)

while q:
    # 현재 방문중인 노드 now
    now = q.popleft()
    for node in graph[now]:
        # now에서 출발하는 간선을 제거: 도착 노드들의 진입차수 -=1
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(now)
```



## **7. 문자열**

파이썬의 문자열은 기본적으로 불변인 자료구조임에 유념하자

기본적으로 **슬라이싱이 가장 빠르기 때문에** 다른 연산보다 이를 우선으로 할 것



### KMP 알고리즘

> 어떤 문자열 안에 다른 문자열이 들어있는지를 O(n+m)으로 찾아내는 알고리즘
>
> 반복되는 부분을 건너뛰면서 찾는다



[백준 1786번](https://www.acmicpc.net/problem/1786)



**문제 해결 기본 아이디어**

1. 순차적으로 두 문자열 T, P를 비교하다 불일치가 발생하면 "**일치했던 부분을 건너뛰고**" 다시 비교 
2. 단, 일치했던 부분을 **전부 건너뛰지는 않음**
   - 일치했던 부분 내에 반복되는 부분이 존재하면 거기서부터 시작함
   - 반복되는 부분을 찾기 위해 비교할 문자열인 P의 각 위치마다 **실패 함수** 값을 설정
   - 실패 함수란?
     - 불일치가 발생했을 때 얼마만큼 건너뛸지 나타내는 값
     - P의 부분 문자열에 대해 해당 문자열 내에서 **prefix와 suffix가 일치하는 최대 길이**
     - 이걸 LPS(Longest proper Prefix which is Suffix)라고 함



**해결 방법**

- 실패함수 fail[] 이 있다고 했을 때, KMP는 다음과 같이 구현 가능

- ```python
  # T와 P를 비교
  j = 0
  # T와 P가 일치하는 지점의 인덱스를 저장
  result = []
  for i in range(n):
      # 불일치가 발생하면 fail값을 "따라감"
      while j > 0 and T[i] != P[j]:
          j = fail[j-1]
      if T[i] == P[j]:
          # 문자열 매칭 성공
          if j == m-1:
              result.append(i-m+2)
              # 계속 탐색: fail값을 따라감
              j = fail[j]
          else:
              j += 1
  ```

  - 실패 함수 값을 따라간다는 것은 불일치가 발생했을 때 P를 얼마나 "밀어주는가"를 뜻함
    - 실패함수 값이 2라면 맨 앞 2글자==맨 뒤 2글자이므로 P의 3번째 글자부터 비교를 시작
    - `j=2`가 됨: 여기서 2는 불일치가 발생한 지점 직전의 실패함수 값이므로 `j=fail[j-1]`이 된다
  - if가 아니라 while문인 이유는 실패함수의 값이 클 때 "밀어준" 직후에 바로 불일치가 발생할 수 있기 때문

- **실패함수는 P와 P를 비교하는 KMP로 구현** 가능

- ```python
  fail = [0]*(m)
  j = 0
  # i = 0일 때는 실패함수가 0임이 자명하므로 pass
  for i in range(1, m):
      while j > 0 and P[i] != P[j]:
          j = fail[j-1]
      # i번째 인덱스까지의 문자열에서 현재 j가 위치한 자리의 길이(j+1)가 실패함수의 값이 됨    
      if P[i] == P[j]:
          # j를 오른쪽으로 한 칸 이동
          j += 1
          fail[i] = j
  ```

  