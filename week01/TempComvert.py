'''
(1) 输入输出的摄氏度采用大写字母C开头，温度可以是整数或小数，如：C12.34指摄氏度12.34度；

(2) 输入输出的华氏度采用大写字母F开头，温度可以是整数或小数，如：F87.65指摄氏度87.65度；

(3) 不考虑异常输入的问题，输出保留小数点后两位；

(4) 使用input()获得测试用例输入时，不要增加提示字符串。

转换算法如下：（C表示摄氏度、F表示华氏度）

         C = ( F - 32 ) / 1.8

         F = C * 1.8 + 32
'''
TempStr = input()
if TempStr[: 1] == 'F':
    C = ((eval(TempStr[1: ]) - 32)  / 1.8)
    print("C{:.2f}".format(C))
elif TempStr[: 1] == 'C':
    F = 1.8 * eval(TempStr[1: ]) + 32
    print("F{:.2f}".format(F))