#deque
#데이터의 양 끝 모두 삽입 삭제가 가능해요
#스택, 큐 모두 덱으로 만들 수 있음
#파이썬엔 덱 모듈이 있어요

#오른쪽 삽입삭제 : append(), pop()
#왼쪽 삽입삭제 : appendleft(), popleft()

#front / rear

# 큐는 값의 삽입 방향과 삭제 방향이 달라요
# 스택은 값의 삽입 방향과 삭제 방향이 왼쪽이에요


#iterable 객체 : 반복 가능한 형태의 데이터 자료 ex) 리스트 튜플 덱
#extend(iterable) : 덱의 오른쪽에 배열 추가  extendleft(iterable) 여러개의 리스트나 덱을 통째로 추가해요




#deque 연습

from collections import deque

deq = deque([4, 5, 6])

deq.append(7)
deq.appendleft(3)
print(deq)

deq.pop()
deq.popleft()
print(deq)


li = [1,2,3]
deq.extend(li)
print(deq)
deq.extendleft(li)
print(deq)


# **왼쪽에 추가 될 때는 3, 2, 1 로 인설트돼요

deq = deque([4, 5, 6])

deq.insert(2, 0)
print(deq)
deq.remove(0)
print(deq)


deq = deque([4, 5, 6, 4])

print(deq.count(4))
# 4가 여러개 있는 경우 맨 앞에 있는 인덱스의 번호가 출력돼요
print(deq.index(4))


deq = deque([4, 5, 6])
deq.reverse()
print(deq)

deq = deque([4, 5, 6])
print("길이:", len(deq))
print("합:", sum(deq))
print("최대:", max(deq))
print("최소:", min(deq))


deq.clear()
print(deq)



