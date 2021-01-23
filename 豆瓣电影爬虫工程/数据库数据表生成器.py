import pymysql


class Creater:
    def __init__(self):
        self.create_db = 'create database DoubanFilm;'

        self.create_table = '''CREATE TABLE IF NOT EXISTS `DoubanFilm`(
                          `number` varchar(100) not null,
                          `name` varchar(100),
                          `year` varchar(100),
                          `type` varchar(100),
                          `source` varchar(100),
                          `people` varchar(100)
                        )ENGINE=InnoDB DEFAULT CHARSET=utf8;'''

        self.cha = 'select * from DoubanFilm;'

    def create_database(self):
        db = pymysql.connect("localhost", "root", "123456")
        cursor = db.cursor()
        cursor.execute(self.create_db)
        cursor.close()
        db.close()

    # 生成数据表
    def create_tables(self):
        db = pymysql.connect("localhost", "root", "123456", "DoubanFilm")
        cursor = db.cursor()
        cursor.execute(self.create_table)
        self.data = str(cursor.fetchall())
        cursor.close()
        db.close()

    def chaxun(self):
        db = pymysql.connect("localhost", "root", "123456", "DoubanFilm")
        cursor = db.cursor()
        cursor.execute(self.cha)
        cursor.rowcount
        get_row = cursor.fetchall()
        # 取结果集剩下所有行
        print(get_row)
        cursor.close()
        db.close()


if __name__ == '__main__':
    do = Creater()
    a = input('1:生成数据库，2：生成数据表，3：查询数据表，4：一键生成数据库和数据表\n')

    if int(a) == 1:
        do.create_database()
        print('已生成数据库')
    elif int(a) == 2:
        do.create_tables()
        print('已生成数据表')
    elif int(a) == 3:
        do.chaxun()
    elif int(a) == 4:
        do.create_database()
        print('已生成数据库')
        do.create_tables()
        print('已生成数据表')