N,M = map(int, input().split())
maze = [[0]*(M+2) for _ in range(N+2)]
for i in range(1,N+1):
    maze[i][1:-1] = list(map(int, list(str(input()))))
check = [[0]*(M+2) for _ in range(N+2)]
stack = []
stack.append((1,1))
check[N][M] = 1
roots = [0]
closes = []
end = [1, 1] 
def isclose(x,y) :
  if maze[x+1][y] == 1 and maze[x-1][y] == 1 and 
while stack:
    x, y = stack.pop()
    # print(x,y)
    if x == end[0] and y == end[1]:
        # 최종 경로 도착
        print(check[x][y])
        break
    open = 0
    if check[x+1][y] == 0 and maze[x+1][y] == 1:
        check[x+1][y] = check[x][y] + 1
        open += 1
        stack.append((x+1, y))
    if  check[x-1][y] == 0 and maze[x-1][y] == 1:
        check[x-1][y] = check[x][y] + 1
        open += 1
        stack.append((x-1, y))
    if  check[x][y + 1] == 0 and maze[x][y + 1] == 1:
        check[x][y + 1] = check[x][y] + 1
        open += 1
        stack.append((x, y + 1))
    if check[x][y - 1] == 0 and maze[x][y - 1] == 1:
        check[x][y - 1] = check[x][y] + 1
        open += 1
        stack.append((x, y - 1))
    if open == 1 : 
        # 막다른 길
        closes.append([x,y])
    elif open == 2: 
        # 단방향 길
        stack.append((x,y))
    elif open == 3 : 
        roots.append(root)
        # 갈래길
    elif open == 4:
        roots.append(root)
        roots.append(root)
        # 4갈래 길
