



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
        adj[x] = [y]
        adj[y] = [x]
print(adj)


