def solution(example:list, target:int) -> bool:
    example.sort()
    left:int = 0
    right:int = len(example) - 1

    while(example[left] + example[right]) != target:

        if(example[left] + example[right] < target):
            left += 1

        else:
            right -= 1

        if(left == right or left > right):
            return False

    return True

print(solution([2,1,5,7], 4))
