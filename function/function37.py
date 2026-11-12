# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "a=hi b=hello" → opts={"a":"hi","b":"hello"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 가장 긴 값을 반환하는 함수 정의
def longest_value(**kwargs):
    longest = ""
    for v in kwargs.values():
        if len(v) > len(longest):
            longest = v
    return longest
# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(longest_value(**opts))