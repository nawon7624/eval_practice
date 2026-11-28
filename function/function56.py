# 입력을 단어 리스트로 만듭니다. 예: "a b c" → words=["a", "b", "c"]
words = input().split()

# 단어를 이어붙인 문자열을 반환하는 함수 정의
def concat_words(*words):
    return "-".join(words)

# ↓ 호출부 (수정하지 마세요)
print(concat_words(*words))