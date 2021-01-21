

int_n, int_k = map(int, input().split())
int_list = list(map(int, input().split()))
sum = 0
for i in range(1,int_n+1):
    for j in int_list:
        if i % j == 0:
            sum += i
            break
    
print(sum)