# https://www.acmicpc.net/problem/3085
#
# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
#
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
#
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
#
# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
#
# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
#
# 출력
# 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
import sys
n = int(input())
Max = -1
def findMax(Map):
    global n
    maxlen = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if Map[i][j-1] == Map[i][j]:
                cnt += 1
            else:
                cnt = 1

            if cnt > maxlen:
                maxlen = cnt
        cnt = 1
        for j in range(1, n):
            if Map[j-1][i] == Map[j][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > maxlen:
                maxlen = cnt
    return maxlen

# for i in range(n):
#     row = sys.stdin.readline().rstrip()
#     curRow = []
#     for j in range(len(row)):
#         curRow.append(row[j])
#     Map.append(curRow)

Map = [list(input()) for _ in range(n)] # 붙어서 입력받는 문자열들을 각 문자의 리스트로 만들어주는 기법.

for r in range(n):
    for c in range(n):
        if c+1 < n:
            Map[r][c], Map[r][c+1] = Map[r][c+1], Map[r][c]
            result = findMax(Map)
            if result > Max:
                Max = result
            Map[r][c], Map[r][c+1] = Map[r][c+1], Map[r][c]
        if r+1 < n:
            Map[r][c], Map[r+1][c] = Map[r+1][c], Map[r][c]
            result = findMax(Map)
            if result > Max:
                Max = result
            Map[r][c], Map[r+1][c] = Map[r+1][c], Map[r][c]
print(Max)