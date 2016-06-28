import sqlite3

global conn, cursor

try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('drop table user')
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user values (\'1\', \'王明辉\')')
    cursor.execute('insert into user (id, name) values (\'2\', "周兰")')
    cursor.execute('insert into user (id, name) values (\'3\', "王周")')
    print(cursor.rowcount)
    conn.commit()


    cursor.execute('select * from user where name = ?', ('王周',))
    values = cursor.fetchall()
    print(values)

except Exception as e:
    print(e)
finally:

    if cursor is sqlite3.Cursor:
        cursor.close()
        print('cursor close ok')
    if conn is sqlite3.Connection:
        conn.close()
        print('connection close ok')
