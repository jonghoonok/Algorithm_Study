# Algorithm

기초 알고리즘부터 심화까지 이론 정리 및 문제 풀이를 업로드하는 저장소



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





## **1. 그리디 알고리즘**

> 







## **2. 탐색**

> 

 

### 2.1. DFS



### 2.2. BFS



### 2.3. 이진 탐색





## **3. 정렬**





## **4. DP**



### 4.1. LIS(Longest Increasing Subsequence)

> 수열 nums 내 가장 긴 증가하는 부분 수열의 길이는 얼마인가?



[백준 11053번](https://www.acmicpc.net/problem/11053)

[나무위키](https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4)



문제 해결 기본 아이디어

1. 수열을 순차적으로 돌면서 
2. 현재 보고 있는 **nums[i]보다 작은 동시에 LIS의 마지막 원소인 수**를 찾음
   - 순차적으로 찾으면 O(N^2), 이진 탐색하면 O(NlogN)
   - 찾았다: 현재 보고 있는 수가 LIS의 마지막 원소가 됨, LIS의 길이 += 1
   - 못 찾았다
     - O(N^2): 업데이트 필요하지 않으므로 무시
     - O(NlogN): 업데이트 필요(이진 탐색 위해서 오름차순 정렬 해줘야)



해결 방법

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



문제 해결 기본 아이디어



해결 방법





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



