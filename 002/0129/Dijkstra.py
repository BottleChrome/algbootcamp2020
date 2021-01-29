# Dijkstra Algorithm 
# 다음과 같은 형태의 그래프가 있고, 
# 시작점이 주어졌을 때,
# 모든 정점들이 시작점에서부터 방문하는데 최단 경로의 경로합 값을 출력합니다. 

# 1) 정점들의 개수 n 
# 2) 간선들의 개수 k 
# 3) 간선 정보 a, b, w가 k번 주어집니다. (a에서 b로 가는 방향 있는 간선)
# 4) 시작 정점 s 
# 예시 
# 입력)
# 8
# 14
# 1 2 8 
# 1 4 9 
# 1 3 11
# 2 5 10
# 3 6 8 
# 3 7 8
# 4 2 6
# 4 3 3
# 4 5 1
# 5 8 2 
# 6 7 7
# 7 4 12
# 7 8 5
# 8 6 4 
# 1

# 출력)
# 0 
# 8
# 11
# 9
# 10
# 16
# 19
# 12
import queue

# n = int(input())
# k = int(input())
# edges = {}
# for i in range(k):
#   a,b, w = list(map(int, input().split()))
#   if edges[a] :
#     edges += {b : w}
# s = int(input())

# n = 8
# k = 14
# edges = [[1, 2, 8], [1, 4, 9], [1, 3, 11], [2, 5, 10], [3, 6, 8], [3, 7, 8], [4, 2, 6], [4, 3, 3], [4, 5, 1], [5, 8, 2], [6, 7, 7], [7, 4, 12], [7, 8, 5], [8, 6, 4]]

# s = 1
# values = ['inf' for x in range(n)]
# values[s-1] = 0
# checkList = [0] * n
# stack = []
# stack.append(s)
# while len(stack) != 0 :
#   v = stack.pop()
#   if checkList[v-1]:
#     continue
#   checkList[v-1] = 1
#   if values[v-1] :
#     continue
n = 8
k = 14
adj = {1: {2: 8, 4: 9, 5: 11}, 2: {1: 8, 3: 10}, 3: {2: 10, 4: 5}, 4: {1: 9, 3: 5, 7: 12, 5: 13}, 5: {1: 11, 4: 13, 6: 8}, 6: {5: 8, 7: 7}, 7: {4: 12, 6: 7}}
s= 1
checkList = [0] * (n+1)
value = [1000000] * (n+1)
queue = queue.PriorityQueue()
value[s] = 0
queue.put((0,1))
sum = 0
print("Prim Algorithm")
while not queue.empty() :
  s, r = queue.get()
  if checkList[r] : continue
  # print("Vertex : %d , Value : %d "%(r,s))
  checkList[r] = 1
  for i in adj[r].keys() :
    m = adj[r][i] + s
    # print(m)
    if value[i] > m :
      value[i] = m
    queue.put((adj[r][i], i))

for val in value :
  print(val)


  