# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "-7" 이면 n == -7
n = int(input())
# 절대값을 반환하는 함수를 정의한다.
def my_abs(n):
# 반환값을 출력한다.    
    if n < 0:
        return -n
    return n
# 함수를 호출한다.
print(my_abs(n))