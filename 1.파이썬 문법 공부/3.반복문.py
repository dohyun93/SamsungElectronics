###############################
# 3. 반복문
###############################

# 반복문은 리스트, 튜플, 딕셔너리, 문자열, 집합에서 사용 가능하다.
myDict = dict()
myDict["나이"] = 30
myDict["연봉"] = 7200
myDict[30] = 20

print(myDict[30])
for i in myDict:
    print(i, myDict[i])

myString = "abcdefg"
for i in myString:
    print(i)

mySet = {3, 7}
mySet.add(3)
mySet.add(7)
for i in mySet:
    print(i)

# 구구단 - i, j변수 활용하기.
for i in range(1, 10):
    print(i, "단 계산!")
    for j in range(1, 10):
        print(i, " * ", j, " = ", i*j)
    print()