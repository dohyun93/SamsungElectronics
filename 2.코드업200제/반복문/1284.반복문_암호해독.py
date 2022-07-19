# 1. n까지 소수들을 모두 리스트에 담는다.
# 2. 2부터 1의 소수 리스트에서 n의 절반보다 작은 수까지 n을 나눌 수 있는 소수가 리스트에 있는지 찾는다.
# 3. 있다면 오름차순 출력하고 없으면 "wrong number" 출력한다.

a = int(input())
b = []

for i in range(2, a):
    if a % i == 0:
        b.append(i)

if len(b) == 2:
    if 4 in b:
        print("wrong number")
    else:
        print(*b)
else:
    print("wrong number")