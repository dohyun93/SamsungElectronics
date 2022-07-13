###############################
# 1. 수 자료형 -> 정수형, 실수형, 연산
###############################

#### [1] 정수형 ####
# 정수형
myint = 30
print(myint)

#### [2] 실수형 ####
# 실수형 - 일반적인 표기
myfloat = 157.3
print(myfloat)

myfloat2 = 3. # 소수부가 0일때 소수부를 생략.
myfloat3 = -.7# 정수부가 0일때 정수부를 생략.

print(myfloat2)
print(myfloat3)

# 실수형 - 지수 표기법
myE1 = 1.2e9 # 0이 9개. 유효숫자e지수부 이기 때문에, 유효숫자 x 10^(지수부)로 생각하면 쉽다.
print(myE1)

# 실수형 - round()
# round(실수, 반올림하려는 위치-1)
# e.g., 셋째자리에서 반올림한다면 round(실수, 3-1) => round(실수, 2)가 된다.

testRound = round(12.345, 2) # 셋째자리에서 반올림.
print(testRound)

testround2 = round(12.345)    # 디폴트로 첫째자리에서 반올림하므로 12
testround3 = round(12.345, 0) # 첫째자리에서 반올림하지만 결과는 12.0
print(testround2)
print(testround3)

#### [2] 실수형 ####