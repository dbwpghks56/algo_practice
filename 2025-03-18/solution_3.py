def solution(nums):
    answerList = []

    for i in nums:
        if answerList.count(i) == 0:
            if len(answerList) < len(nums) /2:
                answerList.append(i)

    return len(answerList)


print(solution([3,1,2,3]))
