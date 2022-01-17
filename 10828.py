import sys


def push(n):
    stack.append(n)


def pop():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[-1])
        stack.pop()


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print("1")
    else:
        print("0")


def top():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[-1])


stack = []

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

for i in range(n):
    if data[i].split()[0] == "push":
        push(int(data[i].split()[1]))
    elif data[i].split()[0] == "pop":
        pop()
    elif data[i].split()[0] == "empty":
        empty()
    elif data[i].split()[0] == "top":
        top()
    elif data[i].split()[0] == "size":
        size()
