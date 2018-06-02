# 使用turtle库，绘制一个正方形
import turtle as t
t.setup(600, 600)
t.pu()
t.seth(225)
t.fd(300)
t.seth(0)
t.pd()
for i in range(4):
    t.fd(400)
    t.left(90)
t.done()

