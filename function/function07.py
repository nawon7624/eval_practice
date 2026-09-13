# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 첫 짝수 찾는 함수 정의
def first_even(nums):
    for i in nums:
        if i % 2 == 0:
            return i
# 함수 호출하여 결과 출력
print(first_even(nums))