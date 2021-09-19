"""
이진 탐색 알고리즘
BinarySearch_1 : 재귀를 이용한 이진 탐색 알고리즘
BinarySearch_2 : 반복을 이용한 이진 탐색 알고리즘
"""

def BinarySearch_1(start,end,arr,x):
    arr.sort()
    mid = (start + end) // 2
    while(start <= end):
        if arr[mid] == x:
            print('해당 값은 배열내에 존재합니다')
            break
        elif arr[mid] < x:
            return BinarySearch_1(mid+1,end,arr,x)
        else:
            return BinarySearch_1(start,mid-1,arr,x)


def BinarySearch_2(arr,x):
    arr.sort()
    start = 0
    end = len(arr)-1
    
    while(start <= end):
        mid = (start + end) // 2
        if arr[mid] == x:
            print('해당 값은 배열내에 존재합니다')
            break
        elif arr[mid] < x:
            start = mid + 1
        else:
             end = mid - 1
    