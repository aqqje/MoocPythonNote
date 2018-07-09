#快乐的数字
def getSumofSquares(num):
    numStr=str(num) #将待计算的数字转换成字符串类型
    sum=0
    digitls=[int(x) for x in numStr] #从字符串中提取出每一位数字存入一个列表
    #print(digitls)
    for i in digitls:
        sum += i**2
    return sum

def main():
    n = input() #输入一个正整数
    sumofSqrs = eval(n)
    count = 0
    while sumofSqrs != 1:
        sumofSqrs = getSumofSquares(sumofSqrs)
        count += 1
        if count > 2000: #当计算次数超过2000次时，跳出循环结束计算
            print("False")
            break
    else:
        print("True")

main()