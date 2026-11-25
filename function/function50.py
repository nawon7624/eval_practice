# 첫 토큰=제목, 나머지=정수 점수들. 예: "합계 1 2 3" → title="합계", values=[1, 2, 3]
parts = input().split()
title = parts[0]
values = [int(x) for x in parts[1:]]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def summary(title, *nums):
    s = 0
    for n in nums:
        s += n
    return title + ": " + str(s)

# values를 *로 풀어 함수에 전달 후 결과 출력
print(summary(title, *values))