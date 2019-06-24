
import requests
import bs4
import json
from xpinyin import Pinyin

# 第一次打开网页
res = requests.get('https://gaokao.chsi.com.cn/sch/search.do?start=0')
print(res)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# 获取总页数138
page_num = soup.select('.ch-page li')[7].string
th = soup.select('th')
th_herd = []

# 申明汉字转换拼音对象
pin = Pinyin()
field = ""
for item in th:
    field += (","+pin.get_pinyin(item.get_text(), '_')+" varchar(100)")
    th_herd.append(pin.get_pinyin(item.get_text(), '_'))

# 转化数组为逗号分隔的字符串
delimiter = ','
field = delimiter.join(th_herd)
j = 0
m = 1
a = []
with open('/Users/samcao/Desktop/python/school.txt', 'w') as schoolFile:
    while j < int(page_num):
        # 输出数据量
        res = requests.get(
            'https://gaokao.chsi.com.cn/sch/search.do?start=%s' % (j*20))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        tr = soup.select("table tr")
        i = 0
        a1 = ""
        while i < len(tr):
            if i == 0:  # 去除table的抬头标题这一行，从第二行开始
                i += 1
                continue
            b = ''
            for x in tr[i].select('td')[5].select('span'):
                b = b + "    " + str(x.get_text())  # 985 211
            c = (1 if (tr[i].select('td')[6].string) is None else 0)
            d = (";" if (i+1) is len(tr) else ",")

            dictObj = {
                'school': tr[i].select('td')[0].get_text().strip(),
                'city': tr[i].select('td')[1].get_text().strip(),
                'belong': tr[i].select('td')[2].get_text().strip(),
                'type':  tr[i].select('td')[3].get_text().strip(),
                'level': tr[i].select('td')[4].get_text().strip(),
                'schoolType': b,
                'sss': c,
                'ddd': tr[i].select('td')[7].get_text().strip(),
                'fff': d
            }

            # 格式化
            writeObj = json.dumps(dictObj)
            # 写入文件中
            schoolFile.write(writeObj + ',')
        j = j + 1
schoolFile.close()
