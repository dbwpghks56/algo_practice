import sys

sys.stdin = open('/Users/yujehwan/Desktop/algorithm/2025-03-29/input_25206.txt')

total = {'A+': 4.5, 'A0': 4.0, 'B+' : 3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

sum = 0
sumhak = 0
countP = 0

for _ in range(20):
    c, a, b = sys.stdin.readline().split()
    if b == 'P':
        countP += 1
    else:
        aa = float(a)
        sumhak += aa
        sum += aa * total[b]

if 'P' not in total:
    print('df')

print(sum / (sumhak))
