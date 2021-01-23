import re

import numpy as np
import matplotlib.pyplot as plt
import pymysql

db = pymysql.connect("localhost", "root", "123456", "doubanfilm")
cursor = db.cursor()
cursor.execute("SELECT type FROM doubanfilm")
data = cursor.fetchall()
cursor.close()
db.close()


df1 = np.array(data)
data2 = df1.tolist()
# print(data2)
typelist = []

for i in data2:
    type1 = i[0]
    # print(type1)
    typelist.append(type1)

# print(len(typelist))

one = []
two = []
three = []
four = []
five = []
six = []
se = []
ei = []

for i in typelist:
    res = re.findall(r'[\u4e00-\u9fa5]', i)
    res = ''.join(res)

    if res == '犯罪':
        one.append(i)
    elif res == '奇幻':
        two.append(i)
    elif res == '剧情':
        three.append(i)
    elif res == '传记':
        four.append(i)
    elif res == '动画':
        five.append(i)
    elif res == '纪录片':
        six.append(i)
    elif res == '爱情':
        se.append(i)
    elif res == '喜剧':
        ei.append(i)

a = len(one)
b = len(two)
c = len(three)
d = len(four)
e = len(five)
f = len(six)
g = len(se)
h = len(ei)


labels = np.array(['犯罪', '奇幻', '剧情', '传记', '动画', '纪录片', '爱情', '喜剧'])
dataLenth = 8
# data
data = np.array([a, b, c, d, e, f, g, h])

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))


fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'ro-', linewidth=2)
ax.set_thetagrids(angles*180/np.pi, labels, fontproperties="SimHei")
ax.set_title("豆瓣电影TOP250数据分布雷达图", va='bottom', fontproperties="SimHei")

ax.grid(True)
plt.savefig('雷达图1.png')
plt.show()
