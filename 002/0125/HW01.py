# 10 이상의 숫자가 있습니다.
# 예를 들어서 145라는 숫자는, 각 자릿수의 팩토리얼 합이 자신의 수가 되는 아주 특이
# 한 숫자입니다.
#     ≠      
# 10이상의 수 중, 위와 같은 수를 모두 찾는 프로그램을 작성합니다.

def Factorial(n):
    s = 1
    while n > 1 :
        s *= n
        n -= 1 
    return s 

def getDigit(n):
    digitList = []
    while n > 0 :
        digitList.append(n % 10)
        n //= 10
    return digitList

def getDigitFactorial(n):
    sum = 0 
    digits = getDigit(n)
    for i in digits :
        sum += Factorial(i)
    return sum 

for i in range(10, 10000):
    if i == getDigitFactorial(i):
        print(i)