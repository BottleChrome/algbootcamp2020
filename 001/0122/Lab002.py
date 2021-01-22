
def hanoi(n,k) :
    k -= 1
    if k == 0 :
        return n
    if n == 0 :
        return
    if n == 1 :
        return 1
    else :
        hanoi(n+1,k)
    
    if n == 1: return 1 
    else :
        print(2 * hanoi(n-1,k) + 1)
        return 2 * hanoi(n-1,k) + 1
n = 32
k = int(input())
print(hanoi(n,k))