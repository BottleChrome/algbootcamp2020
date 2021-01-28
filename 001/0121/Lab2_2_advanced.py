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

# 멀티 스레드
# 멀티 프로세싱 
# 멀티 스레드 세이프 



int_n = int(input())
int_list = list(map(int, input().split()))

half = int_n // 2 + 1
min = int_list[0]
max = int_list[half]

for i in range(0,len(int_list)-1, 2):
    if int_list[i] < int_list[i+1]:
        if min >int_list[i]: min = int_list[i]
        if max < int_list[i+1] : max = int_list[i+1]
    else:
        if min >int_list[i+1]: min = int_list[i+1]
        if max < int_list[i] : max = int_list[i]

print("%d %d "%(min,max))


