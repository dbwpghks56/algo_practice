import sys

sys.stdin = open('/Users/yujehwan/Desktop/algorithm/2025-03-26/input_1120.txt')
a, b = sys.stdin.readline().split()

min_diff = 51

for i in range(len(b) - len(a) + 1):
    diff = 0
    sub_b = b[i:i+len(a)]
    for x, y in zip(a, sub_b):
        if x != y:
            diff += 1
    min_diff = min(min_diff, diff)

# 결과 출력
print(min_diff)
