# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "3 -1 4" → nums=[3, -1, 4]
nums = [int(x) for x in input().split()]

# 음수를 만나면 종료하는 함수 정의
def first_negative(nums):
    for i in nums:
        if i < 0:
            return i
    return "없음"
# 함수의 반환값을 출력음
print(first_negative(nums))