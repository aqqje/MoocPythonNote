# 自动轨迹绘制

import turtle as t
# 设置画笔
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
# 数据读取
datalines = []
f = open('data.txt', 'rt')
for line in f:
    line = line.replace('\n', '')
    #print(list(line)).
    datalines.append(list(map(eval, line.split(','))))
#print(datalines)
f.close()
# 轨迹绘制
for i in range(len(datalines)):
    t.pencolor(datalines[i][3], datalines[i][4],datalines[i][5])
    t.fd(datalines[i][0])
    if datalines[i][1]:
        t.right(datalines[i][2])
    else:
        t.left(datalines[i][2])

t.done()

