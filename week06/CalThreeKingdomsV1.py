#《三国演义》 人物出场统计
import jieba
def getText():
    txt = open(".\date\三国演义.txt", "r", encoding="utf-8").read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(20):
        man, count = items[i]
        print('{0:<10}{1:>5}'.format(man, count))
getText()