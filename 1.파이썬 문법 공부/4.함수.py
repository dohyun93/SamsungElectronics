###############################
# 4. 함수
###############################

# 함수는 프로그래밍에 있어 굉장히 중요하다.
# 똑같은 코드를 작성하지 않고 재사용할 수 있는 일련의 기능을 응집시키고 재활용할 수 있게 해주는 기능이다.

# 예를 들어 덧셈을 하는 함수를 만들어보자.

def AddTwoIntegers(a, b):
    print("a + b = ", a+b)

AddTwoIntegers(10, 30)

# 2. global 키워드
# global 키워드로 함수내에서 지역변수가 아닌 함수 밖의 변수를 직접 참조하여 값을 변경할 수 있다.

myInteger = 30

def IncrementGlobalVariable():
    global myInteger # 함수스코프 내 변수가 아닌 함수 외부의 변수를 global 키워드로 직접 접근한다.
    myInteger += 1   # 증가

for i in range(10):  # 10번 호출하여 10번 글로벌 변수의 수를 증가시킨다.
    IncrementGlobalVariable()

print(myInteger)

# 3. 람다 표현식
# 함수를 매우 간단하게 작성할 수 있다.
# 특정한 기능을 수행하는 함수를 '한 줄'에 작성할 수 있다는 점이 특징이다.
# 정렬 라이브러리를 사용할 때 '정렬 기준(Key)'을 설정할 때도 자주 사용되니 매우 중요하다!

def add(a, b):
    return a+b

# 일반적인 add()메서드 사용
print("일반적인 add 메서드 사용 - add(3, 4)")
print(add(3, 4))

# 람다 표현식으로 구현한 add()메서드
print("람다 표현식으로 동일기능 함수 구현 - (lambda a, b:a+b)(3, 4)")
print((lambda a, b: a+b)(3, 4))
