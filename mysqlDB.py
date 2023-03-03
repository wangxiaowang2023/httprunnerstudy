# 第五步，连接数据库及实行数据库文件 mysqlDB.py
# 先导包
import pymysql
from env.dev.readConfig import ReadConfig

# 连接数据库及执行数据库文件
# 实例化之前定义的读取配置文件类，用mysql这个字去接收 留的下面用
mysql = ReadConfig()


# 创建MysqlDb这个类
class MysqlDb:
    def __int__(self, DBname):  # 用私有方法定义连接 等下给下面引用
        self.host = mysql.DateBase(DBname + "host")  # 获取具体的host地址
        self.user = mysql.DateBase(DBname + "user")  # 获取具体的user账号
        self.passwd = mysql.DateBase(DBname + "passwd")  # 获取具体的数据库密码
        self.port = mysql.DateBase(DBname + "port")  # 获取具体的端口号
        # self.database = mysql.DateBase("database")  # 获取具体的对应的数据库 这里注释是暂时不用
        # # db = pymysql.connect()这里是组建连接
        # self.db = pymysql.connect(host=self.host, user=self.user,
        #                           password=self.passwd, port=3306,
        #                           database=self.database, charset="utf8")

        self.Dbname = DBname  # 要传库名进来才能用

    def connect(self):  # 上面的代码是为这里做铺垫，connect是建立连接
        import pymysql
        self.db = pymysql.connect(host=self.host, user=self.user,
                                  password=self.passwd, port=3306,
                                  database=self.Dbname, charset="utf8")
        self.cursor = self.db.cursor()  # cursor=cursor 老套路创建游标

    def execute(self, sql, data):  # 创建连接
        connect = self.db  # 连接等于上面定义的私有方法里面的连接
        cursor = connect.cursor()  # cursor等于cursor
        cursor.execute(sql % data)
        connect.commit()

    def execute_read(self, sql, data):  # 创建读数据 fetchone
        connect = self.db
        cursor = connect.cursor()
        cursor.execute(sql % data)
        for row in cursor.fetchone():
            return row

    def user_name(self):  # 创建用户名
        sql = mysql.Mysql("user_name")
        data = self.execute_read(sql, ())
        return data

    def user_code(self):  # 获取code
        sql = mysql.Mysql("user_code")
        data = self.execute_read(sql, ())
        return data

    # 新的 可用的 获取查询结果的方法
    def get_one_value(self, sql, args=None):
        connect = self.db  # connect建立连接，连接等于self的db连接
        cursor = connect.cursor()  # 创建游标cursor，cursor等于连接connectd的cursor
        cursor.execute(sql, args=args)  # 执行查询
        connect.commit()  # commit关闭连接，必须要的，建立连接创建游标执行语句关闭游标关闭连接一套
        return cursor.fetchone()  # 把cursor的单条查询结果fetchone返回出去

    def get_values(self, sql, args=None):
        connect = self.db
        cursor = connect.cursor()
        cursor.execute(sql, args=args)
        connect.commit()
        return cursor.fetchall()

    def close(self):
        connect = self.db
        cursor = connect.cursor()
        cursor.close()
        connect.close()


if __name__ == '__main__':
    test_sql = "SELECT * from  ejy_ucs.member_coupon where member_id='103969997';"

    mysql_data = MysqlDb.get_values(sql=test_sql)
    print(mysql_data)
