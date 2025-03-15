def solution(friends, gifts):
    n = len(friends)
    friend_idx = {name: i for i, name in enumerate(friends)}  # 친구 이름을 인덱스로 변환
    gift_history = [[0] * n for _ in range(n)]  # 선물 주고받은 기록 (2D 리스트)
    gift_score = [0] * n  # 선물 지수 (준 개수 - 받은 개수)
    received_gifts = [0] * n  # 다음 달 받을 선물 개수

    # 선물 기록 저장
    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx, receiver_idx = friend_idx[giver], friend_idx[receiver]

        gift_history[giver_idx][receiver_idx] += 1  # 선물 기록
        gift_score[giver_idx] += 1  # 준 선물 개수 증가
        gift_score[receiver_idx] -= 1  # 받은 선물 개수 증가

    # 다음 달 선물 계산
    for i in range(n):
        for j in range(n):
            if i == j:
                continue  # 자기 자신에게 주는 경우는 없음

            if gift_history[i][j] > gift_history[j][i]:
                # i가 j에게 더 많이 줬다면 j가 i에게 선물 하나 줌
                received_gifts[i] += 1
            elif gift_history[i][j] == gift_history[j][i]:
                # 주고받은 개수가 같다면 선물 지수 비교
                if gift_score[i] > gift_score[j]:
                    received_gifts[i] += 1

    return max(received_gifts)  # 가장 많이 받은 친구의 선물 개수 반환

# 테스트 실행
print(solution(
    ["joy", "brad", "alessandro", "conan", "david"],
    ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
))
