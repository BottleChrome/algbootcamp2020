

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
    if i == sumYaksu(i)-i:
        # print(i)
        count += 1
print(count)