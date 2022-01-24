#선형탐색
#앞에서부터 하나씩 하니씩 비교를 해요, 원하는 데이터를 찾았을때 인덱스값을 반환하고 탐색 종료
#끝까지 찾는 데이터가 없으면 탐색 실패

def sequentialSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

li = [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]

print(sequentialSearch(li, 6))
print(sequentialSearch(li, 2))
print(sequentialSearch(li, 11))

#이진탐색
#데이터가 정렬되어 있을 때 사용할 수 있는 검색 방법
#중간요소와 찾는 값의 크기를 비교하며 탐색 범위를 반으로 줄여나가요
#데이터가 클 때에도 효율적인 검색이 가능해요
#중간요소와 찾는값의 크기를 비교해서 찾는값의 크기가 작으면 end의 위치를 한 인덱스 앞으로 옮겨줘요


def binarySearch(array, target):
    start = 0
    end = len(array) -1

    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid+1
        else :
            end = mid-1
    return -1

li = [1,3,4,6,7,9,11,13,14,15,17]
print(binarySearch(li, 6))
print(binarySearch(li, 15))
print(binarySearch(li, 20))

