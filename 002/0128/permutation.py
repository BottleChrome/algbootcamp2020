# 숫자 n과 r을 입력받는다
# n이하의 자연수를 가지고 중복없이 r개의 숫자를 배열하는 모든 경우를 표시합니다.
# 예를들어 4하고 2를 입력받으면
# 12
# 13
# 14
# 23
# 24
# 34
# 를 출력하는 프로그램을 작성하시요

n = [1,2,3,4]
r = 2

result = []

def permutation(node,r):
    node.sort()
    used = [0 for _ in range(len(node))]
    
    def generate(chosen, used):
        if len(chosen)==r :
            print(chosen)
            return
        for i in range(len(node)):
            if not used[i]:
                chosen.append(node[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([],used)


permutation(n, r)
    