# 使用turtle库，绘制一个六边形。

import turtle as t
t.setup(600, 600)
t.pu()
t.seth(-130)
t.fd(100)
t.seth(0)
t.pd()
for i in range(6):
    t.fd(100)
    t.left(60)
t.done()
