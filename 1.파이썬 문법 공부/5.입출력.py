###############################
# 5. 입출력
###############################
import sys

myString = input()
print(myString)

for i in myString:
    print(i)

# myString은 "10 20 30" 이라고 가정하자.
# 아래 split함수를 씌우면 공백을 제거한 문자열들의 리스트 형태로 만들어준다.

# myString: "10 20 30"
# myStringWithoutSpace: ['10', '20', '30']

myStringWithoutSpace = myString.split()
print(myStringWithoutSpace)

# split으로 공백을 제거한 문자열들의 리스트를 map으로 원소들을 정수형으로 바꿔준다.
# 아래 결과는 map 오브젝트이다.
myStringWithoutSpaceToIntMap = map(int, myStringWithoutSpace)
print(myStringWithoutSpaceToIntMap)

# 마지막으로 map 오브젝트를 list형태로 바꿔주자.
myIntList = list(myStringWithoutSpaceToIntMap)
print(myIntList)

# 최종 정리하면, 아래 형태로 input() 으로 입력된 공백으로 구분된 문자열을 정수리스트로 바꿀 수 있다.
# list(map(int, input().split()))

# 예시를 갖고 응용해보자.
# 상황가정> 총 입력받을 개수(5)와 5개의 입력을 받는다고 해보자.
# 5
# 10 20 30 40 50

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 만약 3 4 5 처럼 공백을 포함한 입력개수가 적다면 아래처럼 직접 변수에 매핑해줄 수도 있다.
n, m, k = map(int, input().split())
print(n, m, k)

# input()은 사실 성능이 좋지 않아서, 입력이 많은 문제의 경우 시간초과의 원인이 되기도 한다.
# 따라서, input()보다는 아래 방법으로 입력을 받도록 구현하자.

# readline()으로 입력하면 입력 후 엔터가 줄바꿈 기호로 입력된다. 따라서 이 공백 문자를 제거하기 위해 rstrip()을 꼭 붙여줘야 한다.
# 또한 사이에 포함된 공백을 제거하기 위해 split()을 꼭 호출해주자.

intListData = list(map(int, sys.stdin.readline().rstrip().split()))
print(intListData)

# 출력
# 출력은 사실 크게 공부할게 없다.
# 아래 f-string 문법이 Python 3.6부터 지원되니 참고하자.
myAge = 30
print(f"나의 나이는 {myAge}살 입니다.")