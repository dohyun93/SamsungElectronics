#https://codeup.kr/problem.php?id=1180

# 민호는 발명을 되게 좋아하고, 컴퓨터 프로그램도 되게 좋아한다.
#
# 어느 날 민호는 컴퓨터를 사용하던 중 휴지통이 꽉 차서 불편을 느꼈다.
#
# 그래서 휴지통이 n만큼 차면 알아서 쓰레기를 압축해주는 휴지통을 만들려고 한다.
#
# 이 때 압축하는 알고리즘은 다음과 같다.
#
# 10의 자릿수와 1의 자릿수를 서로 바꾸고, 거기에 2를 곱한다.
#
# 예) 70일 경우 14가 된다.( 70 -> 07 -> 14 )
#
# 이 알고리즘은 때로는 부작용을 일으켜 휴지통의 내용이 더 많아 질지도 모른다.
#
# 만약 이 알고리즘의 심각한 부작용으로 수치가 100이 넘는다면 100의 자릿수는 무시된다.

# 첫째 줄에 휴지통을 압축했을 때 양을 출력한다.
#
# 둘째 줄에 그 양이 50이하이면 GOOD 을 출력하고, 50을 넘으면 OH MY GOD 을 출력한다.

n = int(input())
myResultTen = int(n / 10)
myResultOne = n % 10

myResult = 0
mySaying = ""
LIMIT = 50

if n < 10:
    myResult = (10 * myResultOne) * 2
    if myResult >= 100:
        myResult %= 100

else:
    myResult = 2 * ((10 * myResultOne) + myResultTen)
    if myResult >= 100:
        myResult %= 100

if myResult <= LIMIT:
    mySaying = "GOOD"
else:
    mySaying = "OH MY GOD"

print(myResult)
print(mySaying)