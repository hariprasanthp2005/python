import mysql.connector

dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='hari@2005',
                                  database='tabel' 
                                )

    cursor=dbcon.cursor()
    sql_st='''
              create table employees(
              eid int,
              name varchar(20),
              age int,
              esal float
              )
            '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("tabel created")

except Exception as e:
    print(e)

finally:
    pass    
