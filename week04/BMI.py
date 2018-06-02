'''
BMI:对身体质量的刻画
BMI: Body Mass Index
国际上常用的衡量人体肥胖的健康程序的重要标准, 主要用于统计分析
定义： BMI = 体重(kg) / 身高^2(m^2)

分类|国际BMI(kg/m^2)|国内BMI(kg/m^2)
偏瘦|<18.5|<18.5
正常|18.5~25|18.5~24
偏胖|25~30|24~28
肥胖|≥30|≥28

需求：
    输入：给定体重和身高值
    输出：BMI指标分类信息(国际和国内)
'''
height, weight = eval(input('请输入身高(米)和体重(公斤)[逗号隔开]:'))
bmi = weight / pow(height, 2)
print('BMI 数值为：{}'.format(bmi))
who = ''
if bmi < 18.5:
    who = '偏瘦'
elif 18.5 <= bmi < 25:
    who = '正常'
elif 25 <= bmi < 30:
    who = '偏胖'
elif bmi >= 30:
    who = '肥胖'
print('BMI 指标为：国际"{0}"'.format(who))
