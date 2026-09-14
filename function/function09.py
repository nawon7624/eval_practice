# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "85" 이면 score == 85
score = int(input())

# 점수 검증하는 함수 정의
def evaluate(score):
    if score < 0 or score > 100:
        return "유효하지 않음"
    elif 60 <= score <= 100:
        return "합격"
    else:
        return "불합격"
# 함수를 호출해 결과 출력
print(evaluate(score))