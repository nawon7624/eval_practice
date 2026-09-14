# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "-5" 이면 n == -5
n = int(input())

# 절대값과 부호 문자열을 언패킹해 반환하는 함수 정의
def abs_sign(n):
    if n > 0:
        result = "양수"
    elif n < 0:
        result = "음수"
    else:
        result = 0
    return abs(n), result
# 함수를 호출해 결과 출력
print(*abs_sign(n))