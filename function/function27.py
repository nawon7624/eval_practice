# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]
# 인자의 개수를 세는 함수 정의
def count_args(*args):
    return len(args)
# ↓ 호출부 (수정하지 마세요)
print(count_args(*nums))
