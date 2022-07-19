# https://codeup.kr/problem.php?id=1218
#
# 문제 설명
# 삼각형의 3변의 길이 a, b, c가 입력으로 주어진다.
#
# 여기서 입력되는 변의 관계는 a ≤ b ≤ c 이다.
#
# 그 삼각형이 무슨 삼각형인지 출력하시오.

# 조건에 따라 삼각형을 출력한다.
#
# 조건)
#
# 세 변의 길이가 같은 경우 : 정삼각형
# 두 변의 길이가 같은 경우 : 이등변삼각형
# a2 + b2 = c2일 경우(피타고라스 정리) : 직각삼각형
# 위의 조건에 맞지 않는 일반 삼각형일 경우 : 삼각형
# 삼각형이 아닐 경우 : 삼각형아님
# 을 출력한다.

import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
if a == b and b == c:
    print("정삼각형")
elif (a == b and a + b > c) or (b == c and b + c > a):
    print("이등변삼각형")
elif a**2 + b**2 == c**2:
    print("직각삼각형")
elif ((a+b) <= c):
    print("삼각형아님")
else:
    print("삼각형")
