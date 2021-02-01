# A * 알고리즘 
# 정점들의 개수 n이 주어집니다.
# 다음에는 좌표 평면에 위치하는 n개의 정점값(x,y)들이 주어집니다.
# 다음으로는 k가 주어집니다.
# 다음으로는 k개의 무향 그래프 간선값이 주어집니다.
# 시작 지점(start) 과 끝점(end) 이 주어지면 시작지점부터 끝점까지 가는 최단거리를 A*알고리즘으로 구현합ㄴ디ㅏ. 

# 입력 예)
# 10
# 10 100 
# 30 50 
# 80 20
# 80 110 
# 80 90
# 70 60
# 90 40 
# 20 30
# 50 20
# 60 50 
# # 18
# 1 2
# 1 4
# 2 3
# 2 4 
# 4 5
# 4 6
# 4 7
# 5 6
# 5 7
# 5 9
# 6 7
# 6 8
# 6 10
# 7 8
# 7 9
# 7 10 
# 8 9
# 9 10
# 1 9

import queue

# n = int(input())
# locSet = []
# for _ in range( n) :
#   x, y = list(map(int, input().split()))
#   locSet.append([x,y])

# k = int(input())
# vSet = {}
# for _ in range(k) :
#   s, e = list(map(int, input().split()))
#   if s in vSet.keys():
#     vSet[s].add(e)
#   else : vSet[s] = {e}
#   if e in vSet.keys():
#     vSet[e].add(s)
#   else :  vSet[e] = {s}

# start, end = list(map(int, input().split()))


n = 10
k = 18 
start = 1
end = 9
def heuristic(node, start, end):
  g = ((abs(node[0] - start[0]) **2) + (abs(node[1]-start[1])**2))
  h = ((abs(node[0] - end[0]) **2) + (abs(node[1]-end[1])**2))
  return int(g+h)

locSet = [[10, 100], [30, 50], [80, 20], [80, 110], [80, 90], [70, 60], [90, 40], [20, 30], [50, 20], [60, 50]]

vSet = {1: {2, 4}, 2: {1, 3, 4}, 4: {1, 2, 5, 6, 7}, 3: {2}, 5: {9, 4, 6, 7}, 6: {4, 5, 7, 8, 10}, 7: {4, 5, 6, 8, 9, 10}, 9: {8, 10, 5, 7}, 8: {9, 6, 7}, 10: {9, 6, 7}}

visited = []
hList = [0] * n
for i in range(n):
  print(i)
  hList[i] = heuristic(locSet[i],locSet[start-1],locSet[end-1])



print(hList)

