# 피보나치 수열은 전항과 전전항의 합이 현재항이 되는 수열입니다.
# 1 1 2 3 5 8 13 21 34 55 ...
# 이번 문제는 피보나치 수열의 n번째 항을 구하는 것입니다.
# [입력] n(최대값은 2,000,000,000)이 주어집니다.
# [출력] n번째 피보나치값을 1,000,000,009로 나눈 값을 출력합니다.
# 입력 출력
# 10 55

# 입력 

n = int(input())

# 재귀함수로 구현 

def pivo(n ):
    if n == 1:
        return 1
    elif n== 2:
        return 1
    else :
        return pivo(n-1)+pivo(n-2)

print(pivo(n))


# 리스트로 구현 
pivo_array = []
for i in range(n):
    if i == 0 :
        pivo_array.append(1)
    elif i == 1 :
        pivo_array.append(1)
    else :
        pivo_array.append(pivo_array[i-1]+pivo_array[i-2])
print(pivo_array.pop())


# 반복문으로 구현 

def fibo(n):
    if n < 2:
        return n
    a, b = 0 , 1
    for i in range(n-1):
        a, b = b, a+b 
    return b 

print(fibo(n))

def fivo(n):
    sqrt_5 = 5 ** (1/2)
    ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )
    return int(ans)

print(fivo(n))