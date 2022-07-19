import sys
max = -1e9
a, b = map(int, sys.stdin.readline().rstrip().split())

def pow(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

sum = a+b
if sum > max:
    max = sum

minus_a = a-b
if minus_a > max:
    max = minus_a

minus_b = b-a
if minus_b > max:
    max = minus_b

mul = a*b
if mul > max:
    max = mul

div_a = a/b
if div_a > max:
    max = div_a

div_b = b/a
if div_b > max:
    max = div_b

a_b = pow(a, b)
if a_b > max:
    max = a_b

b_a = pow(b, a)
if b_a > max:
    max = b_a

max = round(max, 7)
print(f"{max:.6f}")