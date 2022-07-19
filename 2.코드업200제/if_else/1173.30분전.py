import sys

t, m = map(int, sys.stdin.readline().rstrip().split())
n_m = m-30

if n_m < 0:
    if t > 0:
        t -= 1
    else:
        t = 23
    n_m += 60
    print(t, n_m)
else:
    print(t, n_m)