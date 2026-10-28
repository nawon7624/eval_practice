# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 여러 수의 합을 구해 반환하는 함수 정의
def total(*nums):
    total = 0
    for i in nums:
        total += i
    return total
# ↓ 호출부 (수정하지 마세요) — 리스트를 * 로 풀어 total 에 전달
print(total(*nums))
