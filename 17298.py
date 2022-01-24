import sys

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