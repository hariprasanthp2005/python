import mysql.connector

dbcon=None 

try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='hari@2005',
                                  database='12pm'
                                  )
    cursor=dbcon.cursor()
    sql_st='''
          select * from employees

            '''
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    dbcon.commit()
    print("table reading")
  

except Exception as e:
    print(e)

finally:
    pass



