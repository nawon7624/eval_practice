# 입력을 정수 리스트로 만듭니다. 예: "3 5" → coords=[3, 5]
coords = [int(x) for x in input().split()]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def make_point(x, y):
    return "(" + str(x) + ", " + str(y) + ")"

# coords를 풀어서 함수에 전달하고 결과 출력
print(make_point(*coords))
