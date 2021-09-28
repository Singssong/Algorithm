"""
N(> 0)개의 정수들의 배열이 주어져 있다. 
배열 요소들은 음수, 양수 혹은 0 이다. 
이 배열의 요소들을 모든 음수(들)이 
먼저 나오고 다음으로 0(들)이 나오고 
마지막으로 양수(들)이 나오도록 재정렬하는
O(N) 알고리즘을 작성하라.

아아디어 :
    1. pivot 을 0으로 설정
    2. pivot을 기준으로 음수와 0, 양수를 분리
    3. 분리된 양수를 제외한 음수와 0이 섞여있는 부분집합에서
    음수는 좌측, 0은 우측으로 분리
"""


def partition(A, low, high):
    i = low 
    j = high
    pivot = 0
    temp = 0 # 자리 스위칭을 위한 temp

    while(i<=j): # [음수+0 / 양수]로 분리
        if (A[i] <= pivot):
            i = i + 1
        elif (A[j] > pivot):
            j = j - 1
        else:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i = i + 1
            j = j - 1
    
    j = i - 1 # 양수로 분리된 부분배열 전까지
    i = low

    while(i<j): #음수와 0이 포함된 부분배열을 음수는 좌측, 0은 우측으로 분리
        if (A[i] < pivot):
            i = i + 1
        elif (A[j] == pivot):
            j = j - 1
        else:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i = i + 1
            j = j - 1





A = [2, -1, -1, -1, -1, 0, 0, 2]

#최초호출
partition(A, 0, 7)

#output
print(A)