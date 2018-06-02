## turtle(海龟)库中 turtle 绘图体系的 Python 实现
>  turtle绘图体系： 1969年诞生，主要用于程序设计入门

# turtle 的原(wan)理(fa)
> turtle(海龟)是一种真实的存在
> 有一只海龟，其实在窗体正中心，在画布上游走
> 走过的轨迹成了绘制的图形
> 海龟由程序控制，可以变换颜色、改变宽度等。

# turtle 绘图窗体
> turtle.setup(width, height, startx, starty)【非必须】 设置窗体大小及位置
[width,height参数是绘图窗体的大小，startx, starty 设置窗体位置，是距离显示器的相对位置（可选）]

## turtle 空间坐标系
> 窗体的正中心为绝对坐标系[向上为y, 向右为x]
> turtle.goto（x, y）[海龟去到达(x, y)的位置]
> turtle.fd(d)[向右方前行]， turtle.bk(d)[向左方前行]， turtle.circle(r, angle)
[以当前位置左侧为圆心，曲线运行]

## turtle 角度坐标体系
> turtle.seth(angle)[改变海龟行进方向，只改变方向但不行进, angle 为绝对度数]
> turtle.left(angle) 向左改变方向, turtle.right(angle) 向右改变方向

## RGB 色彩体系
> 由三种颜色构成的万物色
> RGB 指红蓝绿三个通道的颜色组合
> 覆盖视力所能感知的所有颜色

## turtle 的 RGB 色彩模式
> 默认采用小数值，可切换为整数值
> turtle.colormode(mode)[1.0: RGB 小数值模式 255：RGB 整数值模式]

## 画笔控函数
> 画笔操作后一起， 一般成对出现
> turtle.penup() 别名 turtle.pu()[抬起画笔，海龟在飞行]
> turtle.pendown() 别名 turltle.pd()[抬起画笔， 海龟在爬行]
> 画笔设置一直在效， 直至下次重新设置
> turtle.pensize(width) 别名 turtle.width(width)[画笔的宽度，海龟的腰围]
> trutle.pencolor(color) [color 为颜色字符串或 r, g, b 值， 画笔颜色]

