def count_possible_seats(N, M, K, seats):
    count = 0  # 가능한 자리 개수

    for row in seats:
        available = 0  # 현재 윈도우 내 빈 좌석 개수

        for right in range(M):  # 오른쪽 포인터 이동
            if row[right] == '0':
                available += 1  # 빈 좌석 증가
            else:
                available = 0  # 1을 만나면 초기화

            # K개의 연속된 좌석이 확보되면 카운트
            if available >= K:
                count += 1

    return count


# 입력 처리
N, M, K = map(int, input().split())
seats = [input().strip() for _ in range(N)]

# 정답 출력
print(count_possible_seats(N, M, K, seats))
