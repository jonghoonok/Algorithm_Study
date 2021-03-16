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



## **5. 최단 경로**



## **6. 그래프 이론**



