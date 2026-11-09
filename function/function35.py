# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 최댓값을 찾는 함수 정의
def max_all(*nums):
    return max(nums)
# ↓ 호출부 (수정하지 마세요)
print(max_all(*nums))
