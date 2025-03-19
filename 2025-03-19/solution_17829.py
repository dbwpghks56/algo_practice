import sys

n = int(sys.stdin.readline())
first = [[] * n  for _ in range(n)]

for i in range(n):
    first[i] = list(map(int, input().split()))

while(1):
    fourxfour = [];
    for i in range(0, len(first[0])-1, 2):
        for j in range(1, len(first[0]), 2):
            fourxfour.append(first[i][j-1:j+1] + first[i+1][j-1:j+1])

    for i in range(len(fourxfour)):
        fourxfour[i].sort()

    second = []
    for i in range(len(fourxfour)):
        second.append(fourxfour[i][-2])

    second = [second[i:i+(len(first)//2)] for i in range(0, len(second), len(first)//2)]
    first = second

    if(len(first) == 1):
        print(first[0][0])
        break
