# key=value 토큰을 dict 로 파싱합니다. 예: "name=철수 age=20" → opts={"name":"철수","age":"20"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 키워드 인자로 프로필을 반환하는 함수 정의
def make_profile(name, age):
    return f"{name}({age})"
# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(make_profile(**opts))
