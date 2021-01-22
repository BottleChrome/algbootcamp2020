
n = int(input())

# 리스트로 구현하는 법 
pivo = [0 for x in range(10000)]
pivo[1] = 1
pivo[2] = 2
for i in range(3,10000) :
    pivo[i] = pivo[i-1] + pivo[i-2]
print(pivo[n])


# 재귀 함수로 구현하는 법
def fib(n):
    if n == 1 :
        return 1 
    elif n == 2 :
        return 1 
    else :
        return fib(n-1) + fib(n-2)

# 반복문으로 구현 
def fibo(n):
    if n == 1 : return 1
    elif n == 2 : return 2
    elif n == 3 : return 2 

    f = [1,2]
    for i in range(2,n,2):
        f[0] += f[1]
        f[1] += f[0]
    return f[n%2]
# print(fibo(n))
print(pivo[n])


def fibo_general(n):
    sqrt_5 = 5 ** (1/2)
    ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )
    return int(ans)


print(fibo_general(n))

