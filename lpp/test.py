import pymysql

def main():
    connect_sql = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password='L20030316',
        database='company',
        charset='utf8',
    )
    cursor = connect_sql.cursor()
    try:
        create_table = f"""
                    create table if not exists company.employees(
                    id int primary key auto_increment,
                    name varchar(100) not null,
                    department varchar(100) comment '部门',
                    salary float comment '工资');
                    """
        cursor.execute(create_table)
        connect_sql.commit()
        print('创建成功')
    except Exception as e:
        print(f'创建失败{e}')
    try:
        insert_data = f"""insert into company.employees (name,department,salary) values (%s,%s,%s);"""
        data = [
        ('张三','销售部',8000),
        ('李四','技术部',10000),
        ('王五','人事部',7500)
        ]
        cursor.executemany(insert_data, data)
        connect_sql.commit()
        print("插入成功")
    except Exception as e:
        print(f"失败{e}")
    try:
        select_data = f"""select * from company.employees where department = '技术部';"""
        cursor.execute(select_data)
        data = cursor.fetchall()
        connect_sql.commit()
        print(data)
    except Exception as e:
        print(f"失败{e}")
    try:
        update_data = f"""update company.employees set salary = 8500 where name = '张三'; """
        cursor.execute(update_data)
        connect_sql.commit()
        print("成功")
    except Exception as e:
        print(f"失败{e}")
    try:
        delect_data = f"""delete from company.employees where name = '王五';"""
        cursor.execute(delect_data)
        connect_sql.commit()
        print("成功")
    except Exception as e:
        print(f"失败{e}")

        connect_sql.close()
if __name__ == '__main__':
    main()



























