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

# n = int(input())
# k = int(input())
# adj = {}
# for i in range(1,n+1):
#   adj[i] = {}

# for _ in range(k):
#   a, b, w = list(map(int, input().split()))
#   adj[a][b] = w
#   adj[b][a] = w

# print(adj)
n = 7
k = 9
adj = [[1, 2, 8], [1, 4, 9], [1, 5, 11], [2, 3, 10], [4, 3, 5], [4, 7, 12], [5, 4, 13], [5, 6, 8], [6, 7, 7]]

adj = sorted(adj, key = lambda x: x[2])

disjointSet = [i for i in range(1,n+1)]
checkList = [0] * n

sum = 0

def findRoot( x):
  if disjointSet[x-1] == x : return x
  disjointSet[x-1] == findRoot(disjointSet[x-1])
  return disjointSet[x-1]

complete = 0
for i in adj :
  ra = findRoot(i[0])
  rb = findRoot(i[1])
  if ra == rb : continue
  disjointSet[rb-1] = ra
  sum += i[2]
  complete += 1
  if complete == n-1 : break
print(sum)

# 제일 가중치 값이 작은 간선 찾기


