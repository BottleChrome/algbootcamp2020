def isPelindrome(n):
    r = 0
    a = n
    while a > 0:
        r = r*10 + a%10
        a //= 10
    return n==r 
k = int(input())
i = 0 
while k > 0 :
    i += 1
    if isPelindrome(i):
        k -= 1
print(i)