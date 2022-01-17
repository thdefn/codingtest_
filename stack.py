# stack 만들기
# size(), isEmpty(), push(), pop(), top()


from collections import deque

def size():
    print(len(stack))


def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False


def push(n):
    stack.append(n)


# 원래의 코드는 스택이 비어있는 경우 에러가 나요 -> 덱을 사용해봐요
def pop():
    if isEmpty():
        return
    n = stack[len(stack) - 1]
    stack.pop()
    return n


def top():
    if isEmpty():
        return
    return stack[len(stack) - 1]


#stack = []

stack = deque()
print(stack)
pop()
top()