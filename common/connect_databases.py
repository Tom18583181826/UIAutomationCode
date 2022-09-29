import pymysql
from pymysql import cursors


class ConnectDatabases:
    # 创建数据库连接
    def __init__(self, host="127.0.0.1", user="root", password="mima=1509957150", database="guest", charset="utf8",
                 port=3306):
        self.connect = pymysql.connect(
            # connect():建立数据库连接
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )

    # 查询数据
    def query_data(self, sql, query_type, args=None):
        try:
            # 创建游标对象每次使用完可以自动关闭
            with self.connect.cursor() as cursor:
                if query_type == all:
                    cursor.execute(sql, args)
                    all_data = cursor.fetchall()
                    return all_data
                else:
                    cursor.execute(sql, args)
                    one_data = cursor.fetchone()
                    return one_data
        finally:
            self.connect.close()

    # 执行sql语句
    def execute_sql(self, sql, args=None):
        try:
            with self.connect.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                try:
                    # 执行SQL语句
                    rows = cursor.execute(sql, args)
                    if rows == 0:
                        raise Exception("受影响的行数为0，执行失败")
                    # 提交事务
                    self.connect.commit()
                    return True
                # 捕获异常说明执行失败
                except Exception as e:
                    # 回滚数据
                    self.connect.rollback()
                    print("执行失败！", e)
                    return False
        finally:
            # 关闭数据库连接
            self.connect.close()


if __name__ == '__main__':
    sql1 = 'select * from sign_event;'
    test1 = ConnectDatabases().query_data(sql1, all)
    print(test1)
