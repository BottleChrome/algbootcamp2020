


n = int(input())
k = int(input())

matrix = [[0 for x in range(n)] for y in range(n)]
for i in range(k):
    x, y = list(map(int, input().split()))
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1

print(matrix)






