import requests
from lxml import etree
import time
import pymysql
from fake_useragent import UserAgent
import random
import re
import numpy as np
import matplotlib.pyplot as plt


def Film():

    for a in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(a)
        ua = UserAgent(use_cache_server=False)
        ip = ['175.148.79.101', '114.220.29.95', '222.190.217.156']

        print("开始爬取数据")
        html = requests.get(url, proxies={'http': random.choice(ip)}, headers={'User-Agent': ua.random})

        selector = etree.HTML(html.text)
        infos = selector.xpath('//ol[1][@class="grid_view"]')

        for info in infos:
            number = info.xpath('//div[@class="pic"]/em/text()')
            name = info.xpath('//span[1][@class="title"]/text()')
            messages = info.xpath('//div[@class="bd"]/p/text()[2]')
            # print(messages)
            a = 0
            typelist = []
            yearlist = []
            peoplelist = []

            while a < len(messages):
                m = messages[a]

                year = m.split('/')[0]
                year = re.findall(r"\d+", year)
                years = ''.join(year)

                type = m.split('/')[-1]
                type = (type.split(' ')[1])
                type = (type.split('\n')[0])

                yearlist.append(years)
                typelist.append((type))
                a += 2
            # print(yearlist)
            # print(typelist)

            source = info.xpath('//span[@class="rating_num"]/text()')
            peoples = info.xpath('//div[@class="star"]/span[4]/text()')

            for i in peoples:
                people = re.findall(r"\d+", i)
                people = ''.join(people)
                peoplelist.append(people)

            time.sleep(random.randint(1, 3))

        list = []

        for (i1, i2, i3, i4, i5, i6) in zip(number, name, yearlist, typelist, source, peoplelist):
            list.append((i1, i2, i3, i4, i5, i6))
        for i in list:
             print(i)
        SQ = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             passwd='123456',
                             db='doubanfilm',
                             charset='utf8')

        L = SQ.cursor()
        L.executemany("INSERT INTO doubanfilm(number, name, year, type, source, people) VALUES "
                      "(%s,%s,%s,%s,%s,%s)", list)
        SQ.commit()

    print('传入数据库完成')


def data_deal():
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

    angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'ro-', linewidth=2)
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties="SimHei")
    ax.set_title("豆瓣电影TOP250数据分布雷达图", va='bottom', fontproperties="SimHei")

    ax.grid(True)
    plt.savefig('雷达图.png')
    plt.show()
    pass


if __name__ == '__main__':
    try:
        Film()
        data_deal()
    except:
        print("fail")