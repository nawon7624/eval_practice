# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 지수(2), 2개면 둘째 값이 지수입니다. (값은 정수)
parts = input().split()

# 거듭제곱을 반환하는 함수 정의
def power(base, exp=2):
    return base ** exp
# 함수를 호출해 결과를 출력
if len(parts) == 1:
    print(power(int(parts[0])))
else:
    print(power(int(parts[0]), int(parts[1])))
