

int_n, int_k = map(int, input().split())
int_list = list(map(int, input().split()))
vv= set()
for j in int_list :
    for i in range(j, int_n+1, j):
        vv.add(i)
answer = sum(vv)
print(answer)
