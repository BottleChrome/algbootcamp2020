# 두 개의 수 n과 k가 주어집니다. n 이하의 자연수 중 k의 배수들의 합을 계산합니다.
# [입력] n k ( ≦  ≦    ,  ≦ )

# [출력] n 이하의 자연수 중 k의 배수들의 합을 출력합니다.


# [예제]
# 입력 출력
# 10 3 18
testCase1 = [10,3,18]

def solution(input_n, input_k):
    answer = 0
    for i in range(1, input_n+1):
        if i % input_k == 0 :
            answer += i
    return answer 

def test(testcase):
    if solution(testcase[0], testcase[1]) == testcase[2]:
        print("Correct Answer")
    else :
        print("Wrong Answer")

test(testCase1)