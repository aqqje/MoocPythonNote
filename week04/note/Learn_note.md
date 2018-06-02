## 条件判断

操作符|数学符号|描述
-|-|-
<|<|小于
<=|≤|小于等于
>=|≥|大于等于
>|＞|大于
==|＝|等于
!=|≠|不等于

## 条件组合

用于条件组合的三个保留字

操作符及使用|描述
-|-
x and y|两个条件 x 和 y 的逻辑 与
x or y|两个条件 x 和 y 的逻辑 或
not y|条件 x 的逻辑 非

## 异常处理

异常处理的基本使用

```python
try:
    <语句块1>
except [<异常类型>]:
    <语句块2>
else: # 对应的语句块3不在发生异常时执行
    <语句块3>
finally: # 必定执行
    <语句块4>  
```

## 遍历循环

```python
for <循环变量> in <遍历结构>
    <语句块>
```

## 无限循环

```python
while <条件>：
    <语句块>
```

## 循环保留字

- break 跳出并结束当前整个循环, 执行循环后的语句
- continue 结束当次循环, 继续执行后续次数循环

## 循环的扩展

```python
for <循环变量> in <遍历结构>
    <语句块1>
else:
    <语句块2>
```

## random 库概述

random 库是使用随机数的Pyhon 标准库

- 伪随机数：采用梅森旋转算法生成的(伪)随机序列中元素
- random 库主要用于生成随机数
- 使用 random 库: import random

random 库包括两类函数, 常用共 8 个

- 基本随机数函数：seed(), random()
- 扩展随机数函数：randint(), getrandbits(), uniform(), randrange(), choice(), shuffle()

## 基本随机数函数

函数|描述
-|-
seed(a=None)|初始化给定的随机数种子, 默认为当前系统时间
random()|生成一个[0.0, 1.0]之间的随机小数

## 扩展随机数函数
函数|描述
-|-
randint(a, b)|生成一个 [a, b] 之间的整数 random.randint(10, 100) 结束为  45
getrandbits(k)|生成一个 k 比特长的随机整数 random.getrandbits(16) 结束为 37885
uniform(a, b)|生成一个 [a, b] 之间的随机小数 random.uniform(10, 100) 结束为 13，039353
randrange(m, n [, k])|生成一个 [m, n]之间以 k 为步长的随机整数 random.randrange(10, 100, 10) 结束为 80
choice(seq)|从序列 seq 中随机选择一个元素 random.choice([1,2,3,4,5,6,7,8,9,10])  结束为 8
shuffle(seq)|将序列 seq 中元素随机排列, 返回打乱的序列 random.shuffle([[1,2,3,4,5,6,7,8,9,10]]) 结束为：[3,2,6,7,9,10,1,4,5,8]




