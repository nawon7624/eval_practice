# key=value 토큰을 dict 로 파싱합니다. 예: "width=4 height=5" → opts={"width":"4","height":"5"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def box(width, height):
    return width + "x" + height
# opts을 풀어서 함수로 전달해 결과 출력
print(box(**opts))