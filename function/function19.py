# 한 줄을 공백으로 나눕니다. 토큰이 2개면 기본 구분자("-"), 3개면 셋째 값이 구분자입니다.
parts = input().split()

# 두 단어를 구분자로 잇는 함수 정의
def join_two(a, b, sep="-"):
    return a + sep + b
# 함수를 호출해 결과를 출력
if len(parts) == 2:
    print(join_two(parts[0], parts[1]))
elif len(parts) == 3:
    print(join_two(parts[0], parts[1], parts[2]))