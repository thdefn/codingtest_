import sys
from collections import deque


"""
deq = deque()

num = int(sys.stdin.readline())

for i in range(num):
    text = sys.stdin.readline().strip()
    if text.split()[0] == "push_front":
        deq.appendleft(text.split()[1])
    elif text.split()[0] == "push_back":
        deq.append(text.split()[1])
    elif text.split()[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif text.split()[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif text.split()[0] == "size":
        print(len(deq))
    elif text.split()[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif text.split()[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif text.split()[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[len(deq)-1])
"""

number = int(sys.stdin.readline())
deq = deque()

for i in range(number):
    text = sys.stdin.readline().strip()
    if text.split()[0] == "push_front":
        deq.appendleft(text.split()[1])
    elif text.split()[0] == "push_back":
        deq.append(text.split()[1])
    elif text.split()[0] == "pop_front":
        print(deq.popleft() if deq else -1)
    elif text.split()[0] == "pop_back":
        print(deq.pop() if deq else -1)
    elif text.split()[0] == "size":
        print(len(deq))
    elif text.split()[0] == "empty":
        print(0 if deq else 1)
    elif text.split()[0] == "front":
        print(deq[0] if deq else -1)
    elif text.split()[0] == "back":
        print(deq[-1] if deq else -1)
