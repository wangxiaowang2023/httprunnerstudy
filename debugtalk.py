# 六、在 debugtalk.py（必须是这里）中写一个查询数据 sql 的方法
import time
from httprunner import __version__
from mysqlDB import MysqlDb
from util import DbStudy


#
# def sleep(n_secs):
#     time.sleep(n_secs)
#
#
# # 定义查询数据 sql 的方法 并调用
#
# mysqlDB = MysqlDb()
#
#
# def get_user_name():
#     user_name = mysqlDB.user_name()
#     return user_name[0]
#
#
# import handle_mysql
#
#
# # 查询充值前余额
# def before_recharge_amount(inver_user_id):
#     sql1 = "SELECT leave_amount FROM member WHERE id ="
#     sql2 = str(inver_user_id)
#     sql3 = ';'
#     # 拼接sql语句
#     check_sql = sql1 + sql2 + sql3
#     # 创建实例
#     sql_class = handle_mysql.HandleMysql()
#     # 调用实例类中的方法
#     mysql_data = sql_class.get_one_value(sql=check_sql)
#     sql_class.close()
#     return float(mysql_data['leave_amount'])
#
#
# # 计算充值后的余额
# def new_recharge_amount(amount, before_amount):
#     return float(amount) + float(before_amount)

def select_one_data(sql=None):  # 封装一个查询数据库一条返回数据的方法
    s = "select * from ejy_ucs.member_coupon where member_id='2122346538';"
    return list(DbStudy.DB('dev').select_one(sql=s))[1]


if __name__ == '__main__':
    # print(select_one_data("select * from ejy_ucs.member_coupon where member_id='2122346538';")[1])
    print(select_one_data())