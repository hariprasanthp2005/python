import mysql.connector

dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="hari@2005",database="database")
    cursor=dbcon.cursor()
    sql_st='''
            insert into emp(eid,name,esal,loc,gender)
            values(%s,%s,%s,%s,%s);
        '''
    data=[(102,"hari",1000000.5,"banglore","male"),
          (103,"cheeku",200000.5,"banglore","male"),
          (104,"veeru",300000.5,"banglore","male"),
          (105,"kholi",400000.5,"banglore","male"),
          (106,"abd",500000.5,"banglore","male"),
          ]
    cursor.executemany(sql_st,data)
    dbcon.commit()
    print(cursor.rowcount,"records inserted")

except mysql.connector.Error as err:
    print(err)