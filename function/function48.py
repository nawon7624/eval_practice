# 입력을 정수 리스트로 만듭니다. 예: "2 10" → nums=[2, 10]
nums = [int(x) for x in input().split()]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def power(base, exp):
    return base ** exp
# nums를 풀어 함수에 전달 후 결과 출력
print(power(*nums))