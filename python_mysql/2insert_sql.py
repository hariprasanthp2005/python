import mysql.connector

dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='hari@2005',
                                  database='tabel' 
                                )

    cursor=dbcon.cursor()
    sql_st = '''
    INSERT INTO employees
    VALUES (101, 'Hari', 21, 50000),
           (102, 'cheeku', 22, 10000)
'''
    cursor.execute(sql_st)
    dbcon.commit()
    print("value inserted")

except Exception as e:
    print(e)

finally:
    pass    