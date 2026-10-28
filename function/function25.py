# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 할인율(10), 2개면 둘째 값이 할인율(%)입니다. (정수)
parts = input().split()

# 할인 적용 가격을 반환하는 함수 정의
def discount_price(price, rate=10):
    return price - price * rate // 100
# 함수를 호출해 결과 출력
if len(parts) == 1:
    print(discount_price(int(parts[0])))
elif len(parts) == 2:
    print(discount_price(int(parts[0]), int(parts[1])))
    