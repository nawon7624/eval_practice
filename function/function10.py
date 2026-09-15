# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 커트라인(60), 2개면 둘째 값이 커트라인입니다. (정수)
parts = input().split()

# TODO: pass_line 에 기본값 60 을 가진 함수를 직접 정의(def)하고,
#   토큰 개수에 따라 정수로 변환해 인자를 생략/전달한 뒤 결과를 print 하세요.

# 합격 여부를 판정하는 함수 정의
def check_pass(score, pass_line=60):
    if score >= pass_line:
        return "합격"
    else:
        return "불합격"
# 함수를 호출해 결과를 출력
print(check_pass(score, pass_line))