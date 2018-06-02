# 使用turtle库，绘制一个叠边形，其中，叠边形内角为80度。

import turtle as t
t.setup(600, 600)
t.pu()
#t.seth(225)
#t.fd(300)
#t.seth(0)
t.pd()
for i in range(9):
    t.fd(100)
    t.left(80)
t.done()