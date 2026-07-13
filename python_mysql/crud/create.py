import mysql.connector

dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="hari@2005",database="database")
    cursor=dbcon.cursor()
    sql_st='''
            create table emp(
            eid int primary key,
            name varchar(20) not null,
            esal float,
            loc varchar(30) default 'banglore',
            gender varchar(10)
        
        );
        '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("tabel created successfully")

except mysql.connector.Error as err:
    print(err)


