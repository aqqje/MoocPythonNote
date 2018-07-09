"""
描述
斐波那契数列如下：

F(0) = 0, F(1) = 1

F(n) = F(n-1) + F(n-2)

编写一个计算斐波那契数列的函数，采用递归方式，输出不超过n的所有斐波那契数列元素

调用上述函数，完成如下功能：

用户输入一个整数n，输出所有不超过n的斐波那契数列元素、输出数列的元素和及平均数，输出按照顺序，用英文逗号和空格分割

此题目为自动评阅，请严格按照要求规范输入和输出。



输入
示例1：5

输出
示例1：

0, 1, 1, 2, 3, 5, 12, 2
"""


from operator import itemgetter
queue = eval(input())

queue.sort(key = itemgetter(1))
queue.sort(key = itemgetter(0), reverse = True)

output = []
for item in queue:
    output.insert(item[1], item)
print(output)