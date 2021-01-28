# 주어진 숫자중에서 최소값을 찾는 프로그램을 작성합니다.
# n이 주어지고, n개의 자연수가 주어지면, 해당 자연수중 가장 작은 값을 찾습니다.
# 예를 들어 n이 5이고, 5개의 자연수가 3, 7, 2, 8, 4 였다면, 2가 가장 작은 수이므로
# 2를 출력합니다.

# [입력] n  ( ≦  ≦   ,  ≦  ≦     ( ≦  ≦ ))
# [출력] 중 가장 작은 값을 출력합니다.

# [예제]

# 입력 출력
# 53
# 7 2 8 4 2


# 풀이 함수 
def solution(input_n, input_list):
    input_list.sort()
    answer = input_list[0]
    return answer

def test():
    # 입력 
    input_n = int(input())
    input_list =list(map(int, input().split()))
    # 풀이
    answer = solution(input_n, input_list)
    # 출력 
    print(answer)
    return answer 

test()