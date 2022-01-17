import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = [sys.stdin.readline().strip() for i in range(k)]
l = int(sys.stdin.readline())
c = deque()
r = deque()
a = 0


for j in range(l):
    text = sys.stdin.readline().strip()
    if text.split()[1] == "L":
        c = int(text.split()[0])
    elif text.split()[1] == "D":
        c = int(text.split()[0])





