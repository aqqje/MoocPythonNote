# 基本统计值计算
'''
-总个数： len()
-求和： for...in
-平均值： 求和/总个数
-方差：各数据与平均数差的平方的和的平均数
-中位数：排序，然后... 奇数找中间1个，偶数打中间2个取平均

'''

def getNum():# 获取用户不定长度的输入
    nums=[]
    isNumStr = input('请输入数字（回车退出）：')
    while isNumStr != '':
        nums.append(eval(isNumStr))
        isNumStr = input('请输入数字（回车退出）：')
    return nums

def mean(nums):# 平均值
    s = 0.0
    for num in nums:
        s += num
    return s / len(nums)

def dev(nums, mean):# 求方差
    sdev = 0.0
    for num in nums:
        sdev += (num - mean)**2
    return pow(sdev/(len(nums) - 1), 0.5)

def median(nums):# 计算中位数
    sorted(nums) # 使用 sorted 函数 进行列表类型的排序
    size = len(nums)
    if size % 2 == 0:
        med = (nums[size // 2 - 1] + nums[size// 2]) / 2
    else:
        med = (nums[size // 2 ])
    return med

n = getNum()
m = mean(n)
print("平均值:{}, 方差:{:.2}, 中位数:{}.".format(m, dev(n, m), median(n)))