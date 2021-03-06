## range() 函数用法

range(start, stop[, step])

参数说明：

- start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
- stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
- step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

```python
>>>range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)     # 从 1 开始到 11
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)  # 步长为 5
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)  # 步长为 3
[0, 3, 6, 9]
>>> range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
```

## r 用法
① \r 默认表示将输出的内容返回到第一个指针，这样的话，后面的内容会覆盖前面的内容
```python
import time
for i in range(101):
    print('\r{:3}%'.format(i), end='')
    time.sleep(0.1)
```

② 在转义字符前加上 r ，则表示让这个字符串里面的内容失去转义的意义

```python
s = '\tt'
ns = r'\tt'
print(s)
print(ns)
>>>
	t
\tt
```

- 浮点数0.0和整数0相同性的描述是: 它们具有用相同的值

- 选项描述了字符串.strip()方法的作用:去掉字符串两侧空格或指定字符

- val=pow(2,1000)，请用一行代码返回val结果的长度值:len(str(val))

- Python复数类型的描述:①复数的虚数部分通过后缀 J 或 j 来表示, ②对复数z，使用z.real获得实数部分 ③对复数z，使用z.imag获得虚数部分

- 1.23e+4+9.87e+6j.real:12300.0

- abs(3-4j)的运算结果: 5.0

- 1.23e+4+9.87e+6j.imag: 9882300.0