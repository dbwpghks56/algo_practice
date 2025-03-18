def solution(absolutes, signs):
    answer = 0;

    for idx, val in enumerate(absolutes):
        if signs[idx] == True:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]

    return answer
