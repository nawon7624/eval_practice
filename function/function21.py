# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 증가폭(1), 2개면 둘째 값이 증가폭입니다. (정수)
parts = input().split()

# step만큼 값 증가하는 함수 정의
def increment(n, step=1):
    return n + step
# 함수를 호출해 결과를 출력
if len(parts) == 1:
    print(increment(int(parts[0])))
elif len(parts) == 2:
    print(increment(int(parts[0]), int(parts[1])))