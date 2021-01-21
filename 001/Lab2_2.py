# 주어진 숫자중에서 최소값과 최대값을 찾는 프로그램을 작성합니다.
# n이 주어지고, n개의 자연수가 주어지면, 해당 자연수중 가장 작은 값을 찾습니다.
# 예를 들어 n이 5이고, 5개의 자연수가 3, 7, 2, 8, 4 였다면, 2가 가장 작은 수이고, 7
# 이 가장 큰 수이므로 2 7을 출력합니다.
# [입력] n  ( ≦  ≦   ,  ≦  ≦     ( ≦  ≦ ))
# [출력] 중 가장 최소값과 최대값을 출력합니다.
# [예제]
# 입력 출력
# 53
# 7 2 8 4 2 7


def solution(input_n, input_list):
    input_list.sort()
    answer = input_list[0]
    return answer

def test():
    # 입력 
    input_n = int(input())
    input_list =list(map(int, input().split()))
    # 풀이
    input_list.sort()
    print(input_list[0])
    print(input_list[-1])
    # 출력 
    
test()