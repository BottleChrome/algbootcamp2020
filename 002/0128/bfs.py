# 1월 28일 
# BFS vs DFS 
# 정점의 개수 (N) 을 입력 받고
# 간선의 개수 (K) 를 입력받습니다.
# 정점 2개를 K번 입력 받아서 그것을 간선으로 하는 그래프를 생각합니다. 
 
# 1) 첫번째 정점(1)에서 출발하여 DFS 알고리즘으로 이동했을 때 정점 방문 순서를 출력합니다.
# 2) 첫번째 정점(1)에서 출발하여 BFS 알고리즘으로 이동했을 때 정점 방문 순서를 출력합니다. 


# 4
# 4
# 1 2
# 1 3
# 2 3
# 3 4

n = int(input())
k = int(input())
adj = {}
for x in range(1,n+1):
    adj[x] = []
for i in range(n):
    x, y = list(map(int, input().split()))
    if adj[x] :
        adj[x] += [y]
        adj[y] += [x]
    else :
        adj[x] = y
        adj[y] = x
print(adj)

checkList = [0 for _ in range(n)]


def bfs(root) :
    queue = [root]
    while True :
        if len(queue) == 0 :
            print('All node Searched')
            return None
        node = queue.pop(0)
        if checkList[node-1]:
            continue
        children = adj[node] 
        queue.extend(children)
        checkList[node] = 1
        print(node)

bfs(1)

checkList = [0 for _ in range(n)]
stack = []
def dfs(root):
    stack = [root]
    while True :
        if len(stack) == 0 :
            print('All node Searched')
            return None
        node = stack.pop()
        if checkList[node]:
            continue
        children = adj[node]
        stack.extend(children)
        checkList[node] = 1 
        print(node)
dfs(1)