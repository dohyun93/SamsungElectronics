###############################
# 2. 조건문
###############################

# 사실 특별한 코드는 없다.
# 아래처럼 조건문으로 변수 값 대입도 가능하다.
myAge = 30
myAnswer = "success" if myAge >= 30 else "fail"

print(myAnswer)

# 또한 1. 자료형.Py에서 다루긴 했지만 리스트 컴프리헨션으로 아래처럼 특정 조건의 원소들을 제외하도록 코딩도 가능하다.
excludeList = [2, 4, 7, 8, 9]
myList = [i for i in range(10)]

print(myList)

resultList = [i for i in myList if i not in excludeList]

print(resultList)