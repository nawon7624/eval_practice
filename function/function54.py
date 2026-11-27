# 위치 토큰: 첫째=기본가, 나머지=추가요금. "discount=값" 은 키워드 전용 할인액.
# 예: "1000 100 200 discount=50" → price=1000, fees=[100,200], discount=50
raw = input().split()
pos = [t for t in raw if "=" not in t]
price = int(pos[0])
fees = [int(x) for x in pos[1:]]
discount = 0
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "discount":
            discount = int(v)
# 결제 합산을 계산해 반환하는 함수 정의
def pay(price, *fees, discount=0):
    total = 0
    for f in fees:
        total += f
    return price + total - discount
# ↓ 호출부 (수정하지 마세요) — discount 는 키워드 전용이라 이름으로 전달
print(pay(price, *fees, discount=discount))