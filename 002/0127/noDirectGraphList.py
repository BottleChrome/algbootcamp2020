


n = int(input())
k = int(input())
adj = [[] for y in range(n)]
for i in range(n):
    x, y = list(map(int, input().split()))
    adj[x-1] += [y]
    adj[y-1] += [x]

for i in range(n):
    s = str( i+1  )  + " : "
    for k in adj[i]:
        s += str(k)+ " "
    print(s)

