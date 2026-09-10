# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 합과 평균을 언패킹해 반환하는 함수 정의
def sum_avg(nums):
    total = 0
    avg = 0
    for i in nums:
        total += i
        avg += 1
    return total, total // avg
# 함수 호출해 결과 출력
print(*sum_avg(nums))