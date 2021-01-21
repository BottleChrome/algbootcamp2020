

# 세 개의 수 n, a, b가 주어집니다. n 이하의 자연수 중, a의 배수이거나 b의 배수들의
# 합을 출력합니다. 예를 들어서 n이 10이고, a는 2, b는 3이면, 10 이하의 수중에 조건
# 에 해당하는 수들을 2 3 4 6 8 9 10 이므로 42를 출력하면 됩니다.


# [입력] n a b ( ≦  ≦    ,   ≦ )
# [출력] n 이하의 자연수 중 a 또는 b의 배수들의 합을 출력합니다.


# [예제]
# 입력 출력
# 10 2 3 42

testCase1 = [10, 2 ,3, 42]

def get_besu(input_n, input_a):
    yaksu = []
    i = 0
    num = 1 
    while num < input_n :
        i += 1
        num = i*input_a
        if num > input_n :
            break
        yaksu.append(num)
        
    print(yaksu)
    return yaksu


def solution(input_n, input_a, input_b):
    yaksu_a = get_besu(input_n, input_a)
    yaksu_b = get_besu(input_n, input_b)
    cd = []
    for a in yaksu_a :
        if a in yaksu_b:
            cd.append(a)
    answer = sum(yaksu_a) + sum(yaksu_b) - sum(cd)
    return answer

def test(testCase):
    if testCase[3] == solution(testCase[0],testCase[1],testCase[2]):
        print("Correct Answer! ")
    else :
        print("Wrong Answer! ")

test(testCase1)