# 使用turtle库，绘制一个同切圆。

import turtle as t
t.setup(600, 600)
t.pu()
t.goto(0, -150)
t.pd()
for i in range(4):
   t.circle((i * 30) + 100)
t.done()