# 최대공약수는 두 개의 수에 대한 공통 약수 중 가장 큰 수를 의미합니다. 예를 들어서
# 12와 30의 각각의 약수는 1, 2, 3, 4, 6, 12와 1, 2, 3, 5, 6, 10, 15, 30의 약수를 공
# 통으로 가집니다. 공약수는 1, 2, 3, 6으로 이중 가장 큰 수는 6이 되며, 이 때 6을
# 12와 30의 최대공약수(GCD)라고 합니다.

# 두 개의 수가 주어지면, 이 두 수의 최대 공약수를 구하도록 합니다.

# [입력] a, b의 두 개의 수가 주어집니다. (최대값 2,000,000,000)

# [출력] a와 b의 최대공약수를 출력합니다.

# [예제]
# 입력 출력
# 12 30 6

testCase1 = [12, 30 ,6]

def get_yaksu(input_n):
    yaksu = []
    for i in range(1,input_n+1) :
        if input_n % i == 0:
            yaksu.append(i)
    return yaksu


def solution(input_a, input_b):
    yaksu_a = get_yaksu(input_a)
    yaksu_b = get_yaksu(input_b)
    cd = 0
    for a in yaksu_a :
        if a in yaksu_b:
            cd = a 
    return cd 

def test(testCase):
    if testCase[2] == solution(testCase[0],testCase[1]):
        print("Correct Answer! ")
    else :
        print("Wrong Answer! ")

test(testCase1)