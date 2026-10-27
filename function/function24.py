# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4 5" → nums=[1, 2, 3, 4, 5]
nums = [int(x) for x in input().split()]

# 최댓값, 최솟값을 뺀 나머지의 합을 반환하는 함수 정의
def trimmed_sum(*nums):
    total = 0
    for i in nums:
        total += i
    return total - max(nums) - min(nums)
# ↓ 호출부 (수정하지 마세요)
print(trimmed_sum(*nums))
