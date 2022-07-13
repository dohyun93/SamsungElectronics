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

#### [3] 수 자료형의 연산 ####
a = 8
b = 3
print(a/b) # 실수형으로 나타낸다.
print(a//b)# 몫을 구한다.
print(a%b) # 나머지를 구한다.
print(a**b)# 거듭제곱을 구한다.

###############################
# 2. 리스트 자료형
###############################
# * append(), remove() 등의 메서드를 지원한다.
# * 여러개의 데이터를 연속적으로 담아 처리하기 위해 사용한다.
# * C++ STL의 vector와 유사하다.

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mylist)
print(mylist[3])
mylist = list() # mylist = [] 와 동일하게 빈 리스트 생성할 수 있다.
print(mylist)

#### [1] 리스트 활용 ####
n = 10
mylist = [1] * n
print(mylist)
# 이런 코드는 주로 크기가 n인 1차원 리스트를 초기화 할 때 사용한다.

#### [2] 리스트 활용 - 리스트 인덱싱과 슬라이싱 ####
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[-1])
print(a[3])
print(a[3:9])

#### [3] 리스트 활용 - 리스트 컴프리헨션 ####
# 리스트 컴프리헨션은 리스트를 초기화 하는 방법 중 하나다.
array = [i for i in range(1, 20)]
print(array)
array = [i for i in range(1, 20) if i % 2 == 0]
print(array)

# 이러한 리스트 컴프리헨션은 2차원 N x M 리스트를 초기화 하는데 유용하게 사용할 수 있다.
# [[0] * c] * r 과 같은 형태로 하면 동일한 리스트 객체에 대해 r개의 원소가 생기므로, 한 리스트의 수정이 다른 리스트들의 수정을 야기한다.
r = 3
c = 4
myMap = [[1] * c for _ in range(r)]
print(myMap)

#### [3] 리스트 활용 - 리스트 관련 메서드 ####
# 3-1. list.append(val) : O(1)
# -> list에 원소 하나를 삽입한다.
a = []
a.append(1)
print(a)

# 3-2. list.sort(), list.sort(reverse=True) : O(NlogN)
# -> 리스트 원소들을 정렬한다 (오름/내림차순)
a = [1, 3, 2, 8, 7, 4]
print(a)
a.sort() # 오름차순
print(a)
a.sort(reverse=True) # 내림차순
print(a)

# 3-3. list.reverse() : O(N)
# -> 리스트 원소들을 역순으로 배치한다.
a = [1, 2, 3, 4]
a.reverse()
print(a)

# 3-4. list.insert(idx, val) : O(N)
# -> list의 idx에 val을 삽입한다.
a = [1, 2, 3, 4, 5, 6, 7]
a.insert(3, 100) # idx 3위치에 100 삽입. -> [1, 2, 3, 100, 4, 5, 6, 7]
print(a)

# 3-5. list.count(val) : O(N)
# -> list의 val개수를 센다.
a = [1, 2, 3, 3, 3, 5]
print(a.count(3))

# 3-6. list.remove(val) : O(N)
# -> list에서 val을 제거하나, 여러개면 하나만 제거한다.
a = [1, 2, 3, 7, 3, 5]
a.remove(3)
print(a)

# append는 O(1), sort는 O(NlogN)이며 나머지는 O(N)이다.
# N개의 원소를 갖는 리스트에서 복수개가 존재하는 특정 값을 제거한다고 했을 때,
# O(N)의 remove()를 N개 원소에 대해 적용하면 O(N^2) 시간복잡도를 갖는 알고리즘이다.
# 한편 제거할 대상을 별도 리스트에 담아두고, N개 원소의 리스트중 제거대상 리스트에 없는 원소만 결과에 포함시키면 O(N)으로 가능하다.

remove_list = [1, 3]
my_list = [1, 2, 3, 4, 5, 6, 1, 1, 3, 3, 8, 9, 10, 11, 13]

result = [i for i in my_list if i not in remove_list]
print(result)