# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 가변인자 중 최솟값을 반환하는 함수정의
def min_all(*nums):
    minus = nums[0]
    for i in nums:
        if i < minus:
            minus = i
    return minus
# ↓ 호출부 (수정하지 마세요)
print(min_all(*nums))
