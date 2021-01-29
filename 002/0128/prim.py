import queue

# 7
# 9
# 1 2 8
# 1 4 9
# 1 5 11
# 2 3 10
# 4 3 5
# 4 7 12
# 5 4 13
# 5 6 8
# 6 7 7

n = 7
k = 9
# adj = {}
# for i in range(1,n+1):
#   adj[i] = {}

# for _ in range(k):
#   a, b, w = list(map(int, input().split()))
#   adj[a][b] = w
#   adj[b][a] = w

# print(adj)

adj = {1: {2: 8, 4: 9, 5: 11}, 2: {1: 8, 3: 10}, 3: {2: 10, 4: 5}, 4: {1: 9, 3: 5, 7: 12, 5: 13}, 5: {1: 11, 4: 13, 6: 8}, 6: {5: 8, 7: 7}, 7: {4: 12, 6: 7}}

checkList = [0] * n
value = [100000] * n
queue = queue.PriorityQueue()
value[0] = 0
queue.put((0,1))
sum = 0
while not queue.empty() :
  s, r = queue.get()
  if checkList[r-1] : continue
  print("Vertex : %d , Value : %d "%(r,s))
  checkList[r-1] = 1
  sum += s
  for i in adj[r].keys() :
    queue.put((adj[r][i], i))



