# 상호 배타적 집합은 어떤 원소가 A에 속해 있다면,
# 이 원소는 A를 제외한 다른 집합에는 속해있지 않다는 것입니다.
# n을 입력 받고 k를 입력받습니다.
# n개의 원소들이 최초에는 모두 자신들 각자가 1개의 원소를 가지는 집합인 상태가 됩니다..
# k개의 연산을 통해서 연산을 하고 그 결과를 출력하는 프로그램을 작성합니다.
# 연산의 종류는 u는 두개의 집합을 합하고, t는 두개의 집합이 같은 집합이면 true,
# 다른 집합이면 false를 출력하게 합니다.
# 예를 들면
# 4
# 4
# u 1 3 
# t 1 2
# u 3 2
# t 1 2
# 이란 입력이 들어오면
# False
# True
# 를 출력합니다.

n = 4
k = 4 

setList = [x+1 for x in range(n)]
setSet = [{x+1} for  x in range(n)]

# [ 0 1 2 3 ]


def uCal(a,b):
    setSet[b-1].union(setSet[a-1] )
    setSet[a-1].union(setSet[b-1] )
    setList[b-1] = setList[a-1]
    

def dCal(a,b):
    if setList[a-1] == setList[b-1]:
        return True
    else :
        return False

for i in range(k):
    c, a, b = input().split()
    if c == 'u' :
        uCal(int(a),int(b))
    elif c=='t':
        print(dCal(int(a),int(b)))
    

print(setList)
print(setSet)