import sys
from collections import deque


data = list(map(int, sys.stdin.readline().split()))
que = deque(range(1, data[0]+1))
res=[]
while len(res)!=data[0]:
    for i in range(data[1]):
        num = que.popleft()
        if i != data[1]-1:
            que.append(num)
        else:
            res.append(num)


print("<", end="")
for i in range(len(res)-1):
    print("%d, "%res[i], end='')
print(res[-1], end="")
print(">")


'''
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
que = deque([i for i in range(1, n+1)])
result = []

while que:
    for i in range(k-1):
        que.append(que.popleft())
    result.append(que.popleft())
    
print('<', end='')
print(', '.join(map(str,result)),end='')
print('>')

'''
