# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 할인(0), 2개면 둘째 값이 할인액입니다. (값은 정수)
parts = input().split()

# 최종 결제 금액을 반환하는 함수 정의
def final_price(price, discount=0):
    return price - discount
# 함수를 호출해 결과를 출력
if len(parts) == 1:
    print(final_price(int(parts[0])))
else:
    print(final_price(int(parts[0]), int(parts[1])))
