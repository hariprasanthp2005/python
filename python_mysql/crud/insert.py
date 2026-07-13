import mysql.connector

dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="hari@2005",database="database")
    cursor=dbcon.cursor()
    sql_st='''
            insert into emp(eid,name,esal,loc,gender)
            values(001,"hari",1000000.5,"banglore","male");
        '''
    cursor.execute(sql_st)
    dbcon.commit()
    print(cursor.rowcount,"records inserted")

except mysql.connector.Error as err:
    print(err)


