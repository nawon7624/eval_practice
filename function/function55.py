# 첫 토큰=기준값(threshold), 나머지=검사할 정수들. 예: "5 3 6 1 8" → threshold=5, nums=[3, 6, 1, 8]
parts = input().split()
threshold = int(parts[0])
nums = [int(x) for x in parts[1:]]

# 기준 초과 개수를 구하는 함수 정의
def count_above(threshold, *nums):
    count = 0
    for i in nums:
        if i > threshold:
            count += 1
    return count
# ↓ 호출부 (수정하지 마세요) — threshold 는 위치 인자, 나머지는 * 로 풀어 전달
print(count_above(threshold, *nums))