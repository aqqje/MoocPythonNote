#《水浒传》 人物出场统计v1

import jieba
import json
from scipy.misc import imread
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

stopwords = stopwordslist('.\date\stopwords.txt')
#print(stopwords)
txt = open('.\date\水浒传.txt', 'r', encoding='utf-8').read();
# 自定義字典
jieba.load_userdict(r".\date\jieba.txt")
# jieba 分詞
words = jieba.lcut(txt, cut_all=False);
# 设置为字典类型
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "宋江道" or word == "宋公明" or word == "宋江便" or word == "宋江见":
        rword = "宋江"
    elif word == "智深" or word == "和尚" or word == "提辖":
        rword = "鲁智深"
    elif word == "军师":
        rword == "吴用"
    elif word == "教头":
        rword == "林冲"
    elif word == "黑旋风":
        rword == "李逵"
    elif word == "戴宗道":
        rword == "戴宗"
    elif word == "柴大官人":
        rword == "柴进"
    else:
        rword = word
    # 利用字典统计词频
    counts[rword] = counts.get(rword, 0) + 1

# 去除无关的词
for word in stopwords:
    del counts[word]
items = list(counts.items());
# 根据词频排序集合
items.sort(key=lambda x: x[1], reverse=True)
# 解析成 json 类型并写文件
wordjson = json.dumps((sorted(counts.items(), key=lambda x:x[1], reverse=True)), ensure_ascii=False)
with open(r'.\date\wordjson.json', 'w+', encoding='utf-8') as f:
    f.write(wordjson)

# 打印
for i in range(50):
    word, count = items[i]
    print('{0:^4}{1:<10}{2:>5}'.format(i + 1, word, count))

# 生成词云
#back_color = imread('F:\MoocPython\week06\image\bg.jpg')  # 解析该图片
imgaepath = '.\image\wcpic' + str(time.time())[-3:] + '.jpg' # 设置图片保存的路径
wcimage = WordCloud(font_path=r".\font\msyh.ttf",
                    max_words=50,
                    height=600,
                    width=1200,
                    background_color='white',
                    #mask=back_color
                     ).generate_from_frequencies(counts)
plt.imshow(wcimage)
plt.axis('off')
plt.show()
wcimage.to_file(imgaepath) # 保存图片
