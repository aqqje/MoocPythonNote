'''
编写一个程序，计算输入数字N的0次方到5次方结果，并依次输出这6个结果，输出结果间用空格分隔。其中：N是一个整数或浮点数。

print()函数可以同时输出多个信息，采用如下方法可以使用空格对多个输出结果进行分割：
'''
import math
N = input()
N = eval(N)
count = 0
sum = 0;
while (count <= 5):
    sum = N ** count
    print(sum,  end = '')
    count += 1
    sum = 0

'''
N = input()
N = eval(N)
print(N**0, N**1, N**2, N**3, N**4 , N**5)
'''