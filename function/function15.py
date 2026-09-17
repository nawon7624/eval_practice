# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 2회, 2개면 둘째 값(정수)이 반복 횟수입니다.
parts = input().split()

# 문자열을 반복해 반환하는 함수 정의
def repeat_text(text, times=2):
    return text * times
# 함수를 호출해 결과를 출력
if len(parts) == 1:
    print(repeat_text(parts[0]))
else:
    print(repeat_text(parts[0], int(parts[1])))