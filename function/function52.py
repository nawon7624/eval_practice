# 첫 토큰=대표 메뉴, 나머지=사이드. 예: "비빔밥 김치 단무지" → name="비빔밥", sides=["김치","단무지"]
raw = input().split()
name = raw[0]
sides = raw[1:]

# 대표 메뉴와 사이드 메뉴를 반환하는 함수 정의
def menu(name, *sides):
    if sides:
        return f"{name} ({','.join(sides)})"
    else:
        return name

# ↓ 호출부 (수정하지 마세요)
print(menu(name, *sides))