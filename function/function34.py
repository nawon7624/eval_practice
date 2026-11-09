# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 커트라인(60), 2개면 둘째 값이 커트라인입니다. (정수)
parts = input().split()

# 합격 여부를 판정하는 함수 정의
def check_pass(score, pass_line=60):
    if score >= pass_line:
        return "합격"
    else:
        return "불합격"
# 함수를 호출해 결과를 출력
if len(parts) == 1:
    score = int(parts[0])
    print(check_pass(score))
else:
    score = int(parts[0])
    pass_line = int(parts[1])
    print(check_pass(score, pass_line))