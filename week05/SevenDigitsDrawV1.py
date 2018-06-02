import turtle  as t
def drawLine(draw):# 绘制单数码管
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)

def drawDigit(digit): # 绘制数字
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)

def drawDate(date): # 遍历数字
    for i in date:
        drawDigit(eval(i))

def main(): # 主程序
    t.setup(800, 350, 200, 200)
    t.penup()
    t.fd(-250)
    t.pensize(5)
    drawDate('20181010')
    t.hideturtle()
    t.done()


drawLine(False)
t.done()


