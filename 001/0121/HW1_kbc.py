# 어떤수 자연수가 주어졌을 때, 해당 자연수 자기자신을 제외한 약수의 합이 자신의 수보
# 다 큰 수를 초과수(과잉수)라고 합니다. 예를 들어서 12의 약수는 1, 2, 3, 4, 6, 12로
# 자기자신을 제외한 약수의 합는 1+2+3+4+6 = 16으로 초과수가 됩니다. 이런 초과수를
# 찾는 프로그램을 작성하도록 합니다.
# [입력] n( ≦ )이 주어집니다.
# [출력] n 이하의 초과수의 개수를 출력합니다.
# [예제]
# 입력 출력
# 15 1
def sumYaksu(n):
    s1 = 1
    if n % 2 == 0:
        s = 1 
        while n%2 == 0:
            s = s*2+1
            n //= 2
        s1 *= s
    i = 3 
    while i*i <= n :
        if n%i != 0 :
            i+=2
            continue
        s = 1
        while n%i == 0:
            s = s*i+1
            n//=i
        s1 *= s
        i+=2
    if n > 1 :
        s1 *= n+1
    return s1

n= int(input())
count = 0
for i in range(1,n+1):
    if i < sumYaksu(i)-i:
        count += 1
print(count)