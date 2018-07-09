#分数转换
import re
orgnScore = input()
pat = re.compile(r'^(0|100|[1-9]\d.?\d*)$')
try:
    if pat.match(orgnScore):
        score = eval(orgnScore)
        if 0 <= score < 60:
            print("输入成绩属于E级别。")
        elif score < 70:
            print("输入成绩属于D级别。")
            print("祝贺你通过考试！")
        elif score < 80:
            print("输入成绩属于C级别。")
            print("祝贺你通过考试！")
        elif score < 90:
            print("输入成绩属于B级别。")
            print("祝贺你通过考试！")
        else:
            print("输入成绩属于A级别。")
            print("祝贺你通过考试！")
    else:
        print("输入数据有误！")
except Exception as e:
    print(e.message)
finally:
    print("好好学习，天天向上！")