#factTest1
def main():
    a = input()
    sum = 0
    if a.isdigit():
        n = eval(a)
        if n > 0:
            fact = 1
            for i in range(1, n+1):
                fact *= i
                sum += fact
            print(sum)
        else:
            print("输入有误，请输入正整数")
    else:
        print("输入有误，请输入正整数")

main()