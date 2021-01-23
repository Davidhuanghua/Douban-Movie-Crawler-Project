import re

import numpy as np
import matplotlib.pyplot as plt
import pymysql

db = pymysql.connect("localhost", "root", "123456", "doubanfilm")
cursor = db.cursor()
cursor.execute("SELECT type,people FROM doubanfilm")
data = cursor.fetchall()
cursor.close()
db.close()


df1 = np.array(data)
data2 = df1.tolist()
# print(data2)


typelist = []
sourcelist = []

one = []
two = []
three = []
four = []
five = []
six = []
se = []
ei = []

for i in data2:
    type1 = i[0]
    source1 = i[1]

    res = re.findall(r'[\u4e00-\u9fa5]', type1)
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

s_1 = []
s_2 = []
s_3 = []
s_4 = []
s_5 = []
s_6 = []
s_7 = []
s_8 = []

for s in one:
    s_1.append(float(s[1]))
for s in two:
    s_2.append(float(s[1]))
for s in three:
    s_3.append(float(s[1]))
for s in four:
    s_4.append(float(s[1]))
for s in five:
    s_5.append(float(s[1]))
for s in six:
    s_6.append(float(s[1]))
for s in se:
    s_7.append(float(s[1]))
for s in ei:
    s_8.append(float(s[1]))

av_1 = ('%.1f' % np.mean(s_1))
av_2 = ('%.1f' % np.mean(s_2))
av_3 = ('%.1f' % np.mean(s_3))
av_4 = ('%.1f' % np.mean(s_4))
av_5 = ('%.1f' % np.mean(s_5))
av_6 = ('%.1f' % np.mean(s_6))
av_7 = ('%.1f' % np.mean(s_7))
av_8 = ('%.1f' % np.mean(s_8))


labels = np.array(['犯罪', '奇幻', '剧情', '传记', '动画', '纪录片', '爱情', '喜剧'])
dataLenth = 8
# data
data = np.array([av_1, av_2, av_3, av_4, av_5, av_6, av_7, av_8])

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))


fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'ro-', linewidth=2)
ax.set_thetagrids(angles*180/np.pi, labels, fontproperties="SimHei")
ax.set_title("豆瓣电影TOP250评分人数分布雷达图", va='bottom', fontproperties="SimHei")

ax.grid(True)
plt.savefig('雷达图3.png')
plt.show()
