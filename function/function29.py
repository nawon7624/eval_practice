# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "width=4 height=5" → opts={"width":4,"height":5}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 넓이를 계산하여 반환하는 함수 정의
def rectangle_kw(width, height):
    return width * height
# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(rectangle_kw(**opts))
