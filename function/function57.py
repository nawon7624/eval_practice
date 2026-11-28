# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 평균을 반환하는 함수 정의
def average_args(*nums):
    return sum(nums) // len(nums)

# ↓ 호출부 (수정하지 마세요)
print(average_args(*nums))
