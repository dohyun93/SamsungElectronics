# https://www.acmicpc.net/problem/10430

# 문제
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
#
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
#
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
#
# 출력
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())
A = (a+b)%c
B = ((a%c) + (b%c)) % c
C = (a*b)%c
D = ((a%c) * (b%c)) % c

print(A)
print(B)
print(C)
print(D)