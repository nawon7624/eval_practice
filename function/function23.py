# 한 줄을 공백으로 나눕니다. 예: "철수" → ["철수"](기본값 사용) / "철수 반가워" → ["철수","반가워"](override)
parts = input().split()

# 기본 인사말을 반환하는 함수를 정의
def greet(name, greeting="안녕하세요"):
    return f"{greeting}, {name}님!"
# 함수를 호출해 결과를 출력
if len(parts) == 1:
    print(greet(parts[0]))
else:
    print(greet(parts[0], parts[1]))