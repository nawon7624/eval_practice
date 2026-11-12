# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "b=2 a=1" → opts={"b":"2","a":"1"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 키워드 인자를 문자열로 합쳐 반환하는 함수 정의
def merge_to_string(**kwargs):
    result = []
    for key in sorted(kwargs):
        result.append(f"{key}={kwargs[key]}")
    return ",".join(result)
# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(merge_to_string(**opts))
