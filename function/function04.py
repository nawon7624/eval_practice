# input() 으로 문자열 한 줄을 읽습니다. 예: 입력이 "hello" 이면 s == "hello"
s = input()

# 모음의 개수를 반환하는 함수 정의
def count_vowels(s):
    total = 0
    for ch in s:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            total += 1
    return total
# 함수를 호출해 결과를 출력
print(count_vowels(s))