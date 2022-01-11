import sys

que = []

num = int(sys.stdin.readline())

for i in range(num):
    text = sys.stdin.readline().strip()

    if text.split()[0] == "push":
        que.append(text.split()[1])
    elif text == "front":
        print(que[0] if que else -1)
    elif text == "back":
        print(que[-1] if que else -1)
    elif text == "size":
        print(len(que))
    elif text == "empty":
        print(0 if que else 1)
    elif text == "pop":
        if que:
            print(que[0])
            que.pop(0)
        else:
            print(-1)
