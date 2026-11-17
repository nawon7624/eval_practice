# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "name=철수 age=20" → opts={"name":"철수","age":"20"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 회원 등록옵션 반환하는 함수 정의
def register(name, **options):
    result = []
    for opt in sorted(options):
        result.append(f"{opt}={options[opt]}")
    return f"{name}: " + ",".join(result)
# ↓ 호출부 (수정하지 마세요) — name 은 name 매개변수로, 나머지는 **options 로 모임
print(register(**opts))
