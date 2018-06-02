'''
读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：

第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。
'''
N = eval(input())
lines = N // 2 + 1  # 行数
for i in range(lines):
    blankNumber = N // 2 - i  # 空格数
    print((" " * blankNumber) + ("*" * (i * 2 + 1)))