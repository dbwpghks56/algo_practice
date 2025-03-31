import sys

sys.stdin = open('/Users/yujehwan/Desktop/algorithm/2025-03-31/input_2579.txt')

n = int(sys.stdin.readline())
stair = {}
dp = {}

for i in range(n):
    m = int(sys.stdin.readline())
    stair[i] = m

if n > 2:
    dp[0] = stair[0]
    dp[1] = max(stair[0] + stair[1], stair[1])
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

    for i in range(3, n, 1):
        dp[i] = max(dp[i-2] + stair[i], stair[i-1] + stair[i] + dp[i-3])

    print(dp[n-1])
elif n == 1:
    print(stair[n-1])

elif n == 2:
    print(max(stair[1], stair[0] + stair[1]))
