# 두 개의 수 n, k가 주어집니다. 다음으로 k개의 자연수가 주어집니다. n 이하의 자연
# 수 중, 주어진 k개의 자연수의 배수들의 합을 계산합니다. 예를 들어서 10 3 2 3 4란
# 수가 주어지면 2, 3, 4의 배수들 중 10 이하의 수들의 합을 구합니다. 2는 2의 배수이
# 고, 3은 3의 배수이고, 4는 2와 4의 배수입니다. 6, 8, 9, 10가 2, 3, 4의 배수가 됩
# 니다. 합은 2+3+4+6+8+9+10을 계산한 것으로 42가 됩니다..
# [입력] n k  ( ≦  ≦   ,  ≦  ≦ ,  ≦   ≦  ≦ )
# [출력] n 이하의 자연수 중 주어진 k개 자연수의 배수들 합을 출력합니다.


# [예제]
# 입력 출력
# 10 3
# 2 3 4 42




# input_n 까지의 input_a 의 배수를 반환하는 함수 정의 
def get_besu(input_n, input_a):
    besu = []
    temp = input_a
    while temp <= input_n:
        besu.append(temp)
        temp += input_a
    
    return besu

# 풀이 함수 
def solution(input_n, input_list):
    besu_list = set()
    # 집합 자료형으로 해결 
    for i in input_list:
        besu_list = besu_list.union(set(get_besu(input_n,i)))
    answer = sum(besu_list)

    return answer

def test():
    # 입력 
    input_n, input_k = map(int, input().split())
    input_list = map(int, input().split())
    # 풀이
    answer = solution(input_n, input_list)
    # 출력 
    print(answer)
    
    return answer 

test()