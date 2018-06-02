from random import random

# 介绍
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")

# 获取数值
def getInputs():
    probA = eval(input("选手A能力值（以0到1之间的小数表示）:"))
    probB = eval(input("选手B能力值（以0到1之间的小数表示）:"))
    n = eval(input("模拟场次："))
    return probA, probB, n

# 判断结束
def gameOver(a, b):
    return a == 15 or b == 15

# 一个比赛
def oneGame(probA, probB):
    scoreA, scoreB = 0, 0
    saving  = "A"
    while not gameOver(scoreA, scoreB):
        if saving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                saving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                saving = 'A'
    return scoreA, scoreB

# 多场比赛
def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = oneGame(probA, probB);
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

# 打印结束
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))

# 主方法
def main():
    printIntro()
    probA, probB, n = getInputs();
    winsA, winsB, = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()