import time
import json
from pyecharts import Bar

jsontxt = open('.\date\wordjson.json', 'r', encoding='utf-8').read()
txt = dict(json.loads(jsontxt))
def changlist(jsondict, savepath='.\date\pycs', title='水浒传人物出场统计(50)'):# dict 数据 -> list(dict.keys()), list(dict.values())
    attr = []
    value = []
    for i in range(30):
        attr.append(list(jsondict.keys())[i])
    for i in range(30):
        value.append(list(jsondict.values())[i])
    attr = ['{}'.format(i) for i in attr]
    value = ['{}'.format(i) for i in value]
    bar = Bar(title)
    bar.add('', attr, value, is_label_show=True, is_datazoom_show=True)
    bar.render(path=savepath + str(time.time())[-3:] + '.html')
changlist(txt)