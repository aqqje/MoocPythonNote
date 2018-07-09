#factTest2
import sys
sys.setrecursionlimit(5000)

def getSum(i):
    sum = 0
    if i==0:
        return 0
    else:
        for x in range(1,i+1):
            sum += fact(x)
        return sum

def fact(m):
    if m==0:
        return 1
    else:
        return m*fact(m-1)

def main():
    n = input()
    if n.isdigit():
        a = eval(n)
        if a>0:
            result = getSum(a)
            print(result)
        else:
            print("输入有误，请输入正整数")
    else:
        print("输入有误，请输入正整数")

main()