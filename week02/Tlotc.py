'''
请编写程序，完成米和英寸之间的长度转换，基本需求如下：
输入英寸，转换成米；
输入米，转换成英寸。
英寸采用in标记，放在数值结尾；米采用m标记，放在数值结尾。
1 米 = 39.37 英寸
输入参数请使用input()，不要增加提示字符串信息。
'''
CurStr = input("")
if CurStr[-1] == 'm':
    In = (eval(CurStr[:-1]) * 39.37)
    print("{:.3f}in".format(In))
elif CurStr[-2:] == 'in':
    M = (eval(CurStr[:-2]) / 39.37)
    print("{:.3f}m".format(M))
