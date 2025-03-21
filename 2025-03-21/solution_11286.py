import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
ildan = []
juldae = []

for _ in range(n):
    m = int(sys.stdin.readline())

    if m != 0 :
        heappush(ildan, (abs(m), m))

    else:
        if len(ildan) == 0:
            print(0)
        else:
            print(heappop(ildan)[1])




# else:
#     if len(ildan) == 0:
#         print(0)
#     else:
#         confirm = min(juldae)
#         juldae.remove(confirm)

#         if -confirm in ildan:
#             ildan.remove(-confirm)
#             print(-confirm)

#         elif confirm in ildan:
#             ildan.remove(confirm)
#             print(confirm)
