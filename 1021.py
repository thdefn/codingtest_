import sys
from collections import deque


def moveLeft(index):
    for i in range(index):
        a = deq.popleft()
        deq.append(a)

def moveRight(index):
    for i in range(index):
        a = deq.pop()
        deq.appendleft(a)

deq = deque()
text = sys.stdin.readline()
num = int(text.split()[0])
m = int(text.split()[1])
deq.extend(range(1,num-1))
##print(deq.popleft())

text = sys.stdin.readline().strip()


sum = 0
for i in range(m):
    index = int(text.split()[i])
    if index == deq[0]:
        sum = sum
    elif index == deq[-1]:
        sum = sum
    elif num / 2 >= deq.index(index):
        for i in range(index):
            a = deq.popleft()
            deq.append(a)
        sum = sum + index
    elif num / 2 < deq.index(index) :
        for i in range(index):
            a = deq.pop()
            deq.appendleft(a)
        sum = sum + index

print(sum)


