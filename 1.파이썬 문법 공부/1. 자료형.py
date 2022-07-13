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

###############################
# 3. 문자열, 튜플, 사전, 집합 자료형
###############################
#### 1. 문자열 ####
# " 나 ' 를 문자열 내 포함할 수 있다.
# "를 포함하고 싶으면 ''안에 문자열을 넣고 그 반대도 가능하다.
# 만약 상관없이 하고싶다면 \ 문자를 사용한다.
myString = "hello\"Dohyun\'"
print(myString)

# 문자열에 정수를 곱하면 동일문자열을 해당 정수만큼 이어붙인것이 된다.
myString = "abc"
print(myString * 3)

# 문자열끼리 + 연산은 문자열을 합쳐준다.
myString = "abc" + " Def"
print(myString)

#### 2. 튜플 #####
# 리스트는 [] 로 원소들을 담았다.
# 튜플은 () 로 원소들을 담는다.
# 튜플로 한 번 선언된 값은 변할 수 없다.

# (중요 Tip!)
# 튜플은 주로 바뀌지 않는 값들을 다룰 때 사용되는데, 우선순위 큐를 이용한 최단거리 구하기(다익스트라 알고리즘)에서
# (비용, 노드) 같이 서로다른 성격의 데이터를 묶어 저장할 때 사용한다.

myTuple = (1, 2, 3)
print(myTuple)
# myTuple[2] = 1 -> TypeError: 'tuple' object does not support item assignment

#### 3. 사전 ####
# key - value 쌍에 대한 데이터를 다루는 자료형이다.
# 리스트, 튜플은 원소의 순서가 있는, 즉 순번으로 인덱싱이 가능한 자료형이나, 사전은 그렇지 않다.
# 사전은 키에 대한 밸류를 해시테이블을 이용해 저장하는 자료형이기 때문에, 인덱스로 원소의 순번이 아닌 key를 사용한다.
# 검색과 수정이 O(1) 시간복잡도로 이뤄진다.

data = dict()
# list는 list()
data["myAge"] = 30
data["myHeight"] = 187
print(data)

# 사전 자료형은 메모리공간의 낭비를 막을 수 있다.
# 가령 1000만개의 데이터 중 100개가 체크되어야 한다고 했을 때, 리스트는 1000만개의 원소를 갖고 그 중 100개만 체크를 하여야 하지만,
# 사전 자료형은 100개만 키-밸류 데이터를 갖고있으면 되어 메모리상 이점이 있다. 실제로 코테에서도 잘 쓰이는 자료형이다.

# (중요 Tip!)
# list, tuple, dict 에서는 'in'키워드를 사용할 수 있다.
if 'myAge' in data:
    print("\'myAge\'를 키로 갖는 밸류가 존재합니다.")

# 또한 key, value에 대해 리스트로 뽑을 수 도 있다.
data_keys = data.keys()
data_values = data.values()

print(data_keys)
print(data_values)

for key in data_keys:
    print(key, " : ", data[key])

#### 4. 집합 ####
# 집합은 중복을 허용하지 않으며, 순서가 없다.
# 사전 자료형에서 키-밸류에 대한 데이터의 인덱스가 없듯 집합은 밸류의 값만 존재하는 자료형이다.
# 특정 원소가 존재하는지 확인할 때 사전자료형처럼 O(1)이 소요된다.

mySet = set()
mySet = set([1, 2, 3])
# mySet = {1, 2, 3}

# mySet.add(1) -> 원소 추가
print(mySet)

# 합집합
setA = set([1, 2, 3])
setB = set([2, 3, 4])
setA_Plus_B = setA | setB # 합집합은 |를 사용한다.
print(setA_Plus_B)

# 교집합
setA_And_B = setA & setB # 교집합은 &를 사용한다.
print(setA_And_B)

# 차집합
setA_Minus_B = setA - setB
print(setA_Minus_B)

# (중요 Tip!) - 집합 자료형의 주요 함수
# add, update, remove
setA.add(7) # 원소 1개 추가. O(1)
print(setA)

setA.update([5, 6]) # 여러개 원소 추가
print(setA)

setA.remove(5) # 원소 1개 제거. O(1)
print(setA)