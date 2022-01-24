import sys
'''
res = []
num = int(sys.stdin.readline())
data = sys.stdin.readline().strip().split()
res = [-1]*num

for i in range(num):
    a = data[i]
    ex = num-i-1
    if ex > 0:
        for j in range(ex):
            if a<data[j+i+1]:
                res[i] = data[j+i+1]
                break
            else:
                continue

result = ' '.join(str(s) for s in res)
print(result)
'''

number = int(sys.stdin.readline())
list_A = list(map(int, sys.stdin.readline().split()))

nge = [-1]*number


for i in range(number):
    for j in range(i+1,number):
        if list_A[i] < list_A[j]:
            nge[i] = list_A[j]
            break

## 이걸로 하면 리스트를 출력할 수 있음
print(*nge)


number = int(sys.stdin.readline())
list_A = list(map(int, sys.stdin.readline().split()))

nge = [-1]*number
index=[]

for i in range(number):
    while index and list_A[index[-1]] < list_A[i]:
        nge[index[-1]] = list_A[i]
        index.pop()
    index.append(i)


print(*nge)