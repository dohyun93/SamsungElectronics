###############################
# 6. 주요 라이브러리
###############################
# 파이썬은 C++ STL 처럼 표준라이브러리를 이용해서 코딩테스트를 풀 수 있다.
# 아래 연습들로 주요 표준 라이브러리들을 연습해보자.

from itertools import permutations, combinations, combinations_with_replacement, product
import heapq
from bisect import bisect_left, bisect_right
from collections import deque, Counter
import math

# 1. print, input
# 2. itertools - 순열과 조합과 같은 반복되는 형태의 데이터를처리하는 기능을 푸는데 도와주는 라이브러리.
# 3. heapq - 우선순위 큐 기능을 구현하기 위해 사용한다.
# 4. bisect - 이진탐색을 제공하는 라이브러리다.
# 5. collections - 덱(deque), 카운터(counter) 등의 유용한 자료구조를 포함하는 라이브러리다.
# 6. math - 필수적인 수학 기능을 제공한다. e.g., 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수를 포함한다.

############### 1. 내장함수 ##################
# print(), input() 는 이미 다뤘으므로 생략한다.
# sum() - iterable 객체(리스트 같은)를 인자로 받아 그들의 원소 합을 반환한다.
List = [1, 2, 3, 4, 5]
myListSum = sum(List)
print(myListSum)

# min() - 여러개의 인자가 들어오거나, 리스트를 넣을 때 가장 작은 값 또는 원소를 반환한다.
print(min(List))

# max() - 여러개의 인자가 들어오거나, 리스트를 넣을 때 가장 큰 값 또는 원소를 반환한다.
print(max(List))

# eval() - 문자열 형태로 수식이 들어오면 그 수식을 계산해 반환한다.
myEquation = "(3+4)*(1-2)"
print(eval(myEquation)) # 수식을 계산해서 반환한다.

# sorted() - iterable 객체를 받아서 정렬된 결과를 반환한다.
mySortedListUp = sorted(List)
mySortedListDown = sorted(List, reverse=True)

print(mySortedListUp)
print(mySortedListDown)

# 응용 #
# 2개의 원소로 이뤄진 튜플들로 구성된 리스트들을 내 목적에 맞게 정렬시켜보자.
myList = [("권도현", 30), ("박현숙", 58), ("권오일", 58), ("권태란", 28)]
# 나이 내림차순으로 정렬한다.
sortedFamily = sorted(myList, key=lambda x: x[1], reverse=True)
print(myList)
print(sortedFamily)

############### 2. itertools ##################
# 순열과 조합을 구현하는 라이브러리들이 존재한다.
# 순열: permutations, 조합: combinations 가 존재한다.

# (1) permutations
# n개의 원소를 갖는 iterable 객체를 인자로 받아서 r개의 데이터를 뽑는 순열을 만들어준다.
# 순열이므로 같은 원소들로 이뤄지더라도 순서를 따진다.
data = ['A', 'B', 'C', 'D']
permutations_data = list(permutations(data, 2))
print(len(permutations_data), permutations_data)

# (2) combinations
# n개의 원소를 갖는 iterable 객체를 인자로 받아서 r개의 데이터를 뽑는 조합을 만들어준다.
combinations_data = list(combinations(data, 2))
print(len(combinations_data), combinations_data)

# (3) product
# n개의 원소를 갖는 iterable 객체를 인자로 받아서 r개의 데이터를 뽑는 순열을 만들어준다. 다만! 중복하여 뽑는다.
product_data = list(product(data, repeat=2))
print(len(product_data), product_data)

# (4) combinations_with_replacement
# n개의 원소를 갖는 iterable 객체를 인자로 받아서 r개의 데이터를 뽑는 조합을 만들어준다. 다만! 중복하여 뽑는다.
combinations_with_replacement_data = list(combinations_with_replacement(data, 2))
print(len(combinations_with_replacement_data), combinations_with_replacement_data)

############### 3. heapq ##################
# 우선순위 큐 알고리즘 구현에 사용.
# 다익스트라 최단경로 알고리즘을 포함해 다양한 알고리즘이 이 우선순위 큐 기반인데, 이를 구현하고자 할 때 사용된다.
# 파이썬의 힙은 '최소 힙'으로 구성되어 있으므로 단순히 원소를 힙에넣었다가 빼는것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
# 최소 힙은 최상단 원소가 가장 작은 원소이다.

# 힙 원소 삽입: heapq.heappush()
# 힙 원소 꺼냄: heapq.heappop()

# 힙 정렬을 heapq로 구현하는 예제로 heapq의 사용방법을 알아보자.
# [참고] heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]
def heapsort(iterable_list):
    h = []
    result = []

    # iterable_list: [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

    # 1. 이진트리 만들기
    for value in iterable_list:
        heapq.heappush(h, value)
    print("h: ", h)
    # h: [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]

    # 2. 정렬된 순서대로 꺼낸다.
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    print("result: ", result)
    # result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    return result

iterable_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
result = heapsort(iterable_list)

# 추가로, 파이썬은 최대 힙을 제공하지 않는다.
# 따라서, 최소 힙의 원소를 - 처리하여 정렬시킨 후 마지막에 -를 곱해주면 된다.

def maxHeapSort(iterable_list):
    h = []
    result = []
    for val in iterable_list:
        heapq.heappush(h, -val) # 음수 값 기준으로 넣는다.

    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 가장 작은 음수값부터 꺼낸 뒤 다시 음수처리해서 원래 값을 append해준다.
    return result

maxHeapSortResult = maxHeapSort(iterable_list)
print(maxHeapSortResult)

############### 4. bisect ##################
# 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다.
# '정렬된 배열'에서 특정 원소를 찾아야 할 때 유용하다.
# bisect_left(), bisect_right() 가 O(logN) 시간복잡도에 동작한다. (heappush, heappop과 동일)

# bisect_left(): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(): 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

List = [1, 2, 4, 4, 8]
x = 4

leftIdx = bisect_left(List, x)
rightIdx = bisect_right(List, x)

print(leftIdx)
print(rightIdx)

# 응용
# count_by_range 함수를 구현해서 특정 범위 내 원소에 해당하는 리스트의 원소개수를 O(logN) 만에 구해보자.

def countByRange(list, left_value, right_value):
    leftIdx = bisect_left(list, left_value)
    rightIdx = bisect_right(list, right_value)
    return rightIdx-leftIdx

print(countByRange(List, -1, 5))
print(countByRange(List, 5, 9))

############### 5. collections ##################
# deque, Counter 를 알아보자.
# deque는 popleft(), pop(), appendleft(), append() 함수를 제공하며 스택, 큐 구현에 사용할 수 있다.
# 연속된 자료의 맨 끝에 대한 데이터 추가/삭제가 용이하다. 모두 O(1).

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # deque 객체를 list 자료형으로 변환.

# Counter - iterable 객체를 전달했을 때, 각 원소가 등장 횟수를 세는 기능을 제공한다.
myColorList = ['red', 'red', 'blue', 'green', 'yellow', 'blue', 'green']
counter = Counter(myColorList)
print("red 등장 횟수: ", counter['red'])
print("blue 등장 횟수: ", counter['blue'])
print("green 등장 횟수: ", counter['green'])
print("yellow 등장 횟수: ", counter['yellow'])
print("black 등장 횟수: ", counter['black'])

############### 6. math ##################
# math 라이브러리의 factorial함수
print(math.factorial(10))

# math 라이브러리의 sqrt함수
print(math.sqrt(9))

# math 라이브러리의 gcd함수 - 최대공약수
def lcm(a, b):
    return (a*b) // math.gcd(a, b)

print(math.gcd(15, 10))
print(lcm(15, 10)) # math.lcm은 파이썬 3.9부터 쓸 수 있다.

# math 라이브러리의 pi, 자연상수
print(math.e)
print(math.pi)