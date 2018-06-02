# hamlet 英文词频分析
import jieba as j
def getText():
    text = open('.\date\hamlet.txt', 'r').read()
    text = text.lower()
    for ch in '!"#$\'%&()*+,-./:;<=>?@[\\]^_‘{|}~': # 去特殊符号
        text = text.replace(ch, '')
    return text

hamletTxt = getText()
words = hamletTxt.split() # 文本切分
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))