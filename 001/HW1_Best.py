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

# k 값이 작다면 포함 배제의 원리로 코드를 짜야한다. 
# k 값이 크다면 집합의 원리로 코드를 짜야한다. 
# 상황에 맞게 코드를 짜야하는 것이 중요하다 . 


int_n, int_k = map(int, input().split())
int_list = list(map(int, input().split()))
sum = 0
for i in range(1,int_n+1):
    for j in int_list:
        if i % j == 0:
            sum += i
            break
print(sum)