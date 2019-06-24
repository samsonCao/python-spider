
import requests
import bs4
# import json
# from xpinyin import Pinyin

# 第一次打开网页
print('Kaishile')
res = requests.get(
    'https://gaokao.chsi.com.cn/gkxx/zcdh/201906/20190618/1799058286.html')
print(res, '----打开了----')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# 获取所有的页面a标签
pageUrlList = soup.select('.pageTable tbody tr td a')
print(pageUrlList)
th = soup.select('a')
th_herd = []

# # 申明汉字转换拼音对象
# pin = Pinyin()
# field = ""
# for item in th:
#     field += (","+pin.get_pinyin(item.get_text(), '_')+" varchar(100)")
#     th_herd.append(pin.get_pinyin(item.get_text(), '_'))

# # 转化数组为逗号分隔的字符串
# delimiter = ','
# field = delimiter.join(th_herd)
# j = 0
# m = 1
# a = []
# with open('/Users/samcao/Desktop/python/school.txt', 'w') as f:
#     while j < int(page_num):
#         # 输出数据量
#         res = requests.get(
#             'https://gaokao.chsi.com.cn/sch/search.do?start=%s' % (j*20))
#         res.raise_for_status()
#         soup = bs4.BeautifulSoup(res.text, 'html.parser')
#         tr = soup.select("table tr")
#         i = 0
#         a1 = ""
#         while i < len(tr):
#             if i == 0:  # 去除table的抬头标题这一行，从第二行开始
#                 i += 1
#                 continue
#             b = ''
#             for x in tr[i].select('td')[5].select('span'):
#                 b = b + "    " + str(x.get_text())  # 985 211
#             c = (1 if (tr[i].select('td')[6].string) is None else 0)
#             d = (";" if (i+1) is len(tr) else ",")

#             dictObj = {
#                 'school': tr[i].select('td')[0].get_text().strip(),
#                 'city': tr[i].select('td')[1].get_text().strip(),
#                 'belong': tr[i].select('td')[2].get_text().strip(),
#                 'type':  tr[i].select('td')[3].get_text().strip(),
#                 'level': tr[i].select('td')[4].get_text().strip(),
#                 'schoolType': b,
#                 'sss': c,
#                 'ddd': tr[i].select('td')[7].get_text().strip(),
#                 'fff': d
#             }

#             # 格式化
#             writeObj = json.dumps(dictObj)
#             # 写入文件中
#             f.write(writeObj + ',')

#             # 获取学校专业
#             # res1 = requests.get('https://gaokao.chsi.com.cn/zyk/pub/myd/specAppraisalTop.action?yxmc=%s' %
#             #                     (tr[i].select('td')[0].get_text().strip()))
#             # res1.raise_for_status()
#             # soup1 = bs4.BeautifulSoup(res1.text, 'html.parser')
#             # url = soup1.select('.check_detail')
#             # 查看全部专业
#         #     u = 0
#         #     for x in url:
#         #         if u > 1:
#         #             break
#         #         u = u + 1
#         #         res1 = requests.get('https://gaokao.chsi.com.cn/%s' % (x['href']))
#         #         res1.raise_for_status()
#         #         soup1 = bs4.BeautifulSoup(res1.text, 'html.parser')
#         #         td = soup1.select(".first_td")
#         #         j1 = 0
#         #         while j1 < len(td):
#         #             if j1 == 0:
#         #                 j1 = j1 + 1
#         #                 continue
#         #             d1 = ','
#         #             a1 = a1 + "(%s, '%s')%s" % (m, td[j1].get_text().strip(), d1)
#         #             j1 = j1 + 1
#             i = i + 1
#             m = m + 1
#         j = j + 1
# f.close()
