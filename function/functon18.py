# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 수량(1), 2개면 둘째 값이 수량입니다. (정수)
parts = input().split()

# 총액을 계산하는 함수 정의
def total_price(unit_price, count=1):
    return unit_price * count
# 함수 호출해 결과 출력
if len(parts) == 1:
    print(total_price(int(parts[0])))
else:
    print(total_price(int(parts[0]), int(parts[1])))