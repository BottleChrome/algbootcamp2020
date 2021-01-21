

# 네 개의 수 n, a, b, c가 주어집니다. n 이하의 자연수 중, a의 배수이거나 b의 배수이
# 거나 c의 배수들의 합을 출력합니다. 예를 들어서 n이 10이고, a는 2, b는 3이면, c는
# 4이면 10 이하의 수중에 조건에 해당하는 수들을 2 3 4 6 8 9 10 이므로 42를 출력하
# 면 됩니다.

# [입력] n a b c ( ≦  ≦    ,    ≦ )

# [출력] n 이하의 자연수 중 a 또는 b 또는 c의 배수들의 합을 출력합니다.

# [예제]
# 입력 출력
# 10 2 3 4 42


testCase1 = [10, 2 ,3,4, 42]

def get_besu(input_n, input_a):
    besu = []
    for i in range(1,input_n+1) :
        if i % input_a == 0:
            besu.append(i)
    return besu

def solution(input_n, input_a, input_b, input_c):
    besu_a = get_besu(input_n, input_a)
    besu_b = get_besu(input_n, input_b)
    besu_c = get_besu(input_n, input_c)
    answer = sum(list(set(besu_a)| set(besu_b) | set(besu_c)))
    # answer = sum(besu_a) + sum(besu_b) + sum(besu_c) - sum(cd)
    return answer

def test(testCase):
    if testCase[4] == solution(testCase[0],testCase[1],testCase[2],testCase[3]):
        print("Correct Answer! ")
    else :
        print("Wrong Answer! ")

test(testCase1)