# 정렬은 데이터를 순서대로 정리하는 것, 오름차순 내림차순
# sorted list.sort() 메소드가 있지만 특정 조건에 한해  직접 정렬해야하는 경우도 있음
# 선택, 버블, 삽입, 퀵, 계수 정렬

# sorted, sort

li1=[3,1,4,9,8,6,7,4,10,2]
li2=sorted(li1)
li3=sorted(li1,reverse=True)
print(li1)
print(li2)
print(li3)

li1.sort()
print(li1)

li1.sort(reverse=True)
print(li1)


# 선택정렬 : 매번 가장 작은값을 선택하고 그 값을 맨 첫번째 위치한 값과 위치 교환하는 정렬
# 데이터 크기가 n개일때 위 과정을 n-1 번 반복하면 정렬 완료 -> 속도가 느림


def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        ## 최솟값의 위치를 판단해요
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i],array[min_idx] = array[min_idx],array[i]
        #print(array)
    return array

li=[3,1,4,9,8,6,7,4,10,2]
print(selectionSort(li))


# 버블 정렬
# 붙어있는 두 데이터를 비교해서 교환해요
# n번째와 n+1 번째 값을 비교하여 더 큰 값을 뒤로보내요
# 비교횟수가 많아 데이터가 많을 수록 속도가 느려지고 비효율적
# 벗 데이터가 거의 정렬되어있다면 훨씬 빠른 속도


def buubleSort(array):
    for i in range(len(array)-1):
        #하나씩 정렬을 완료할때마다 그 숫자만큼은 반복이 되지 않게끔
        for j in range(len(array)-1-i):
            if array[j]>array[j+i]:
                array[j],array[j+1]=array[j+1],array[j]
            print(array)
    return array

print(buubleSort(li))