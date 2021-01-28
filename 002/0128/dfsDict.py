# n = int(input())
# k = int(input())
# adj = {}
# for x in range(1,n+1):
#     adj[x] = []
# for i in range(n):
#     x, y = list(map(int, input().split()))
#     if adj[x] :
#         adj[x] += [y]
#         adj[y] += [x]
#     else :
#         adj[x] = [y]
#         adj[y] = [x]
# print(adj)

n = 4
k = 4 

adj = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}

checkList = [0] * n
stack = []
def dfs(root):
    checkList[root-1] = 1
    print(root)
    for i in adj[root]:
        if not checkList[i-1]:
            dfs(i)

dfs(1)