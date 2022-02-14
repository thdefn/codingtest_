import sys


def qs(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    pnum = ord(pivot)
    left, right = [], []

    for i in range(1, len(array)):
        anum = ord(array[i])
        if anum <= pnum:
            left.append(array[i])
        elif anum > pnum:
            right.append(array[i])

    return qs(left) + [pivot] + qs(right)


data = list(sys.stdin.readline().strip('\n'))
num = []
for i in range(len(data)):
    num.append(ord(data[i]))

numsort = sorted(num)

idx = -1
for i in range(len(numsort)):
    if numsort[i] == idx:
        k = data.index(chr(numsort[i]), k+1)
    else:
        k = data.index(chr(numsort[i]))
    idx = numsort[i]
    print(data[k:])


text_s = sys.stdin.readline().strip()
list_s = []

for i in range(len(text_s)):
    list_s.append(text_s[i:])

list_s.sort()





