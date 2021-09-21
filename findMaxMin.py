# 분할정복 알고리즘을 이용한 최댓값과 최솟값 찾기(재귀)

def findMaxMin(A, i, j):
    # input : 배열 A[i..j]
    # output : min(최솟값), max(최댓값)
    if (i == j): # 배열 요소가 한개 이면,
        min, max = A[i], A[i]
    elif (i == j-1): # 배열 요소가 두개면,
        if (A[i] < A[j]):
            min = A[i]
            max = A[j]
        else:
            min = A[j]
            max = A[i]
    else: # 배열 요소가 세개 이상인 경우
        mid = int((i+j) / 2)
        min1, min2, max1, max2 = 0, 0, 0, 0
        
        min1, max1 =findMaxMin(A, i, mid)
        min2, max2 =findMaxMin(A, mid+1, j)
        if(min1 < min2):
            min = min1
        else:
            max = min2
        
        if(max1 < max2):
            max = max2
        else:
            max = max1
    
    return min, max

A=[24,25,26,27,28,29,30,31]  
min, max = findMaxMin(A,0,7)
print(min, max)
