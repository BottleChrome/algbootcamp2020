# Lab. #3
# 대칭수(Pelindrome)는, 앞으로 읽나 뒤로 읽나 같은 수가 되는 자연수를 말합니다. 예
# 를 들어서 121 이나 327723 등은 대칭수가 됩니다. 1, 2 와 W은 한자리수는 모두 대
# 칭수입니다. 이러한 대칭수는 무한히 많습니다.
# 우리는 k번째로 작은 대칭수를 얻고자 합니다. 예를 들어서 3번째 작은 대칭수는 3이
# 됩니다. 10번째로 작은 대칭수는 11이 됩니다.
# [입력] k 값이 주어집니다. (  ≦  ≦  )
# [출력] k번째로 작은 대칭수를 출력합니다.
# [예제]
# 입력 출력
# 3 3
# 10 11
import math

def getInterval(k):
    return 2*(math.floor(math.log10((9*k+1)/18)))

def IntervalCount(i):
    i -= 1
    i //= 2 
    return 9 * 10 ** i

def isPelindrome(n):
    r = 0
    a = n
    while a > 0:
        r = r*10 + a%10
        a //= 10
    return n==r 

k = int(input())

countSum = 1
i = 0
while countSum  < k :
     countSum += IntervalCount(i+1)
     i += 1

k -= countSum 
k += IntervalCount(i)
i = 10**(i-1)

while k > 0 :
    i += 1
    if isPelindrome(i):
        k -= 1
print(i)