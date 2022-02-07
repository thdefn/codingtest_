import sys
from collections import deque
num = int(sys.stdin.readline())
nums = []
for i in range(num):
    [x, y] = map(int, sys.stdin.readline().split())
    nums.append([x, y])

nums = sorted(nums)

for i in range(num):
    print(nums[i][0], nums[i][1])


'''
number = int(sys.stdin.readline())
list_XY = []

for i in range(number):
    list_XY.append(list(map(int, sys.stdin.readline().split())))
    
list_XY.sort()

for x, y in list_XY:
    print(x, y)

'''