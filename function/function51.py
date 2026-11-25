# 앞 두 토큰=단어 리스트 pair, 나머지 key=value=옵션 dict opts.
# 예: "hello world sep=_ end=?" → pair=["hello","world"], opts={"sep":"_","end":"?"}
tokens = input().split()
pair = tokens[:2]
opts = {}
for token in tokens[2:]:
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def make(a, b, sep="-", end="!"):
    return a + sep + b + end

# # *와 **를 함께 사용하여 리스트와 딕셔너리의 값을 풀어서 함수에 전달 후 결과 출력
print(make(*pair, **opts))