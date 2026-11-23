# key=value 토큰을 dict 로 파싱합니다. 예: "b=2 a=1" → opts={"b":"2","a":"1"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def collect(**kwargs):
    return ",".join(sorted(kwargs))
# opts를 풀어 함수에 전달 후 결과 출력
print(collect(**opts))
