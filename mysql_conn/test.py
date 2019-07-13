from mysql_conn.mysql_conn import Mysql

mysql = Mysql()
# 查询
sql = 'select * from demo;'
re = mysql.getOne(sql)
for row in re:
    print(row)

# 插入
# sql = 'insert into  demo(name,age,address) VALUES ("王五",43,"天津");'
# re = mysql.executeDML(sql)

# 删除
# d = 'delete from demo WHERE id = 3'
# re = mysql.executeDML(d)



