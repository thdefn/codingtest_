import sys

## 내장함수로는 안되는 문제임
num = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(num)]

nums.sort()
print('\n'.join(map(str, nums)), end='')