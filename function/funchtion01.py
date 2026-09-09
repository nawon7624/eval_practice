# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "5" 이면 n == 5
n = int(input())

# 팩토리얼을 반환하는 함수 정의
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# 함수를 호출해 결과를 출력
print(factorial(n))