# 어떤수 n이 주어졌을 때, n의 약수의 개수를 수학에서는  이라고 합니다. 예를 들
# 어서 n이 10인 경우, 10의 약수는 1, 2, 5, 10이고, 약수의 개수는 4가 됩니다.
# 이번에는 n이 주어진 경우 약수의 개수를 구하는 프로그램을 작성합니다.
# [입력] n( ≦ )이 주어집니다.
# [출력] n에 대한 약수의 개수를 출력합니다.
# [예제]
# 입력 출력
# 10 4







def solution(input_n, input_list):
    input_list.sort()
    answer = input_list[0]
    return answer

def test():
    # 입력 
    input_n = int(input())
    yaksu_list = []
    for i in range(1, input_n+1) :
        if input_n % i == 0 :
            yaksu_list.append(i)
    print(len(yaksu_list))

    # 출력 
    
test()