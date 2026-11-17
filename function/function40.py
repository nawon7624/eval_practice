# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "base=1000 ship=500" → opts={"base":1000,"ship":500}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 청구서 합계를 구해 반환하는 함수 정의
def invoice(base, **fees):
    total = base
    for value in fees.values():
        total += value
    return total
# ↓ 호출부 (수정하지 마세요) — base 는 base 매개변수로, 나머지는 **fees 로 모임
print(invoice(**opts))