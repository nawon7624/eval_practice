# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 최소, 최대, 합 언패킹해 반환하는 함수 정의
def stats(nums):
    return min(nums), max(nums), sum(nums)
# 함수를 호출해 결과를 출력
print(*stats(nums))