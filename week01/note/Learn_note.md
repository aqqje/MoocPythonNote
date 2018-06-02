1.print()函数可以同时输出多个信息，采用如下方法可以使用空格对多个输出结果进行分割：(python 2.x 不换行)
    print(3.14, 1024, 2048)

2.python 3.x 使用 print(x, end="")  end="" 可使输出不换行

3.if TempStr[-1] in ['F', 'f']: 中使用in判断TempStr[-1] 是否包含'f', 'F'字符

4.if CurStr[0: 3] == 'RMB':使用str[int index : int end]来进行字符串的分割

5.R = (eval(CurStr[3:]) * 6.78)  中使用eval()函数把  字符型  -->  数字型

6.Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

7.Python如何进行幂运算
    三种方式：1 import math
                math.pow(x, y)

              2 x**y

              3 x * x
