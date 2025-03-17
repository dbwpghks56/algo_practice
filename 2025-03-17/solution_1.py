import sys

n = int(sys.stdin.readline())

st = []

for _ in range(n):
    lst = list(sys.stdin.readline().split())
    if lst[0] == "push":
        st.append(lst[1])
    elif lst[0] == "pop":
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop(-1))
    elif lst[0] == "size":
        print(len(st))
    elif lst[0] == "empty":
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif lst[0] == "top":
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
