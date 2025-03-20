import sys

n = int(sys.stdin.readline())
first = list(map(int, sys.stdin.readline().split()))

first.sort()

left = 0
right = n - 1
answer = [first[left], first[right]]
result = abs(first[left] + first[right])

while left < right:
    total = first[left] + first[right]

    if abs(total) < result:
        result = abs(total)
        answer = [first[left], first[right]]

    if total < 0:
        left += 1
    else:
        right -= 1

print(min(answer), max(answer))




# result = abs(first[left] + first[right])
# answer[0] = first[left]
# answer[1] = first[right]

# while left < flag:
#     if result > abs(first[left] + first[right]):
#         result = abs(first[left] + first[right])
#         answer[0] = first[left]
#         answer[1] = first[right]


#     right -= 1

#     if left == right:
#         right = flag
#         left += 1


# print(answer[0], answer[1])
