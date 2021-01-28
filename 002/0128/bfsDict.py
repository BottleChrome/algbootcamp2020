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


def bfs(root) :
    checkList = [0] * n 
    queue = [root] 
    while True :
        if len(queue)==0:
            print("All Nodes Searched")
            break
        node = queue.pop(0)
        if checkList[node-1] :
            continue
        else :
            checkList[node-1] = 1
        queue.extend(adj[node])
        print(queue)
        print(node)
bfs(1)