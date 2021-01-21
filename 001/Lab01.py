# 주어진 수 n 이하의 자연수의 합을 구하도록 합니다.


# [입력] n (최대값은 1,000,000,000)이 주어집니다.

# [출력] 1부터 n까지의 합을 출력합니다.

# [예제]

# 입력 출력
# 10 55

testCase1 = [10,55]
def Test(test_case):
    if test_case[1] == Solution(test_case[0]):
        print("Correct Solution")
    else :
        print("Wrong Solution")

def Solution(input_n) :
    answer = 0 
    for  i in range(1, input_n+1):
        answer += i
    return answer 

Test(testCase1)