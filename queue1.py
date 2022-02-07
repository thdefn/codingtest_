import queue1
from collections import deque

def size():
    print(len(que))


def isEmpty():
    if len(que) == 0:
        return True
    else :
        return False

# 큐는 삽입 삭제 방향이 다른데 저는 오른쪽에서 들어오고 왼쪽에서 나가도록 해볼게요
def enqueue(n):
    que.append(n)


def dequeue():
    if isEmpty():
        return
    n = que[0]
    que.popleft()
    return n


def front():
    if isEmpty():
        return
    return que[0]


que = deque()

#que = queue.Queue()

enqueue(7)
enqueue(5)
enqueue(3)
enqueue(2)
dequeue()
dequeue()
enqueue(4)

print(que)