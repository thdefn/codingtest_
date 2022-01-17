import sys

# 오름차순 -> 작은것부터 큰 것
# 스택은 후입선출
# 4,3,6,8,7,5,2,1

num = int(sys.stdin.readline().strip())
data = [sys.stdin.readline().strip() for i in range(num)]
a = 0

# a 라는 숫자를 비교해서 작으면 스택에 넣음
for i in range(num):
    a = int(sys.stdin.readline().strip())

