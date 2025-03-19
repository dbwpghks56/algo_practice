def count_possible_seats(N, M, K, seats):
    count = 0  # 가능한 자리 개수

    for row in seats:
        # 초기 윈도우 설정
        zero_count = sum(1 for i in range(K) if row[i] == '0')

        # K개의 연속된 0이 있으면 카운트 증가
        if zero_count == K:
            count += 1

        # 윈도우를 이동하면서 갱신
        for right in range(K, M):
            left = right - K  # 윈도우에서 벗어나는 인덱스

            # 오른쪽에 추가된 값 확인
            if row[right] == '0':
                zero_count += 1
            if row[left] == '0':  # 왼쪽에서 사라지는 값 확인
                zero_count -= 1

            # 현재 윈도우가 K개의 연속된 0을 포함하면 카운트 증가
            if zero_count == K:
                count += 1

    return count


# 입력 처리
N, M, K = map(int, input().split())
seats = [input().strip() for _ in range(N)]

# 정답 출력
print(count_possible_seats(N, M, K, seats))
