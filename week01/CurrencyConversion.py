'''
人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：

人民币和美元间汇率固定为：1美元 = 6.78人民币。

程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用RMB表示，美元USD表示，符号和数值之间没有空格。
'''
CurStr = input("")
if CurStr[0: 3] == 'RMB':
    U = (eval(CurStr[3:]) / 6.78)
    print("USD{:.2f}".format(U))
elif CurStr[0: 3] == 'USD':
    R = (eval(CurStr[3:]) * 6.78)
    print("RMB{:.2f}".format(R))
