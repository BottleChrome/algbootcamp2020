# Lab. #2
# 숫자 야구는 세 개의 숫자를 이용해서 누가 먼저 생각한 숫자를 맞추는 가입니다.
# 윤선이와 윤영이가 숫자 야구 게임을 하기로 합니다.
# - 윤선이는 1에서부터 9까지의 숫자중 서로 다른 세 개의 숫자를 골라서 세자리 숫자를
# 생각합니다. (예를 들면 437을 생각했다고 합시다.)
# - 윤영이는 1에서부터 9까지의 숫자중 서로 다른 세 개의 숫자를 골라서 세자리 숫자를
# 제시합니다. (예를 들어서 134를 제시했다고 합시다.)
# - 윤선이는 생각한 숫자와 같은 자리의 수가 맞으면, 스트라이크(Strike)를 카운트하고,
# 다른 자리의 수가 맞으면, 볼(ball)을 카운트합니다. 그리고 그 결과를 윤영이에게 알
# 려줍니다. (3은 같은 자리에 맞으니 1S, 4는 다른 자리에 맞으니 1B이 됩니다. 그
# 러면 1S1B 라고 알려줍니다.)
# - 이것을 반복해서 하다가 세 개의 자릿수를 모두 맞추면 3S가 되고, 이 때 몇 번만에
# 맞추었는가를 최종으로 점수가 됩니다.
# 여러분은 윤영이의 역할을 하는 프로그램을 작성하도록 합니다. (검은색은 컴퓨터 출력
# 문이고, 빨간색에 밑줄이 있는 것은 사용자가 입력하는 내용입니다.
# [예제]
# Guess : 134
# 1 1
# Guess : 514
# 0 1
# Guess : 436
# 2 0
# Guess : 437
# 3 0
# Score : 4

import random
import itertools

    
def judge(think, guess):
    strike = 0
    ball = 0 
    for i , n in enumerate(guess):
        if n in think:
            if think[i] == guess[i] : strike += 1
            else : ball += 1
    return strike,ball



def genProbGuess(think, strike, ball):
    all_case = []
    if strike >= 1 :
        for i in itertools.combinations(think, strike):
            case = [0,0,0]
            for k in i:
                case[think.index(k)] = k
            all_case.append(case)
    if ball >= 1:
        for case in all_case:
            for element in case :
                if element.count(0)

genProbGuess([1,2,3],1,0)