# 한 줄을 공백으로 나눕니다. 첫 토큰=n, 둘째 토큰(있으면)=start. 토큰 1개면 start 는 기본값 1. (정수)
parts = input().split()

# 구간 합을 구하는 함수 정의
def range_sum(n, start=1):
    total = 0
    for i in range(start, n+1):
        total += i
    return total 
# 함수를 호출해 결과를 출력
if len(parts) == 1:
    n = int(parts[0])
    print(range_sum(n))
elif len(parts) == 2:
    n = int(parts[0])
    start = int(parts[1])
    print(range_sum(n, start))
    