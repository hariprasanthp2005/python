import mysql.connector

dbcon = None

try:
    dbcon = mysql.connector.connect(
        host='localhost',
        user='root',
        password='hari@2005',
        database='12pm'
    )

    print("Connected to database successfully")

    cursor = dbcon.cursor()

    cursor.execute("SELECT DATABASE()")
    print("Current Database:", cursor.fetchone())

    sql_st = '''
    CREATE TABLE employees(
        eid INT,
        ename VARCHAR(32),
        esal FLOAT,
        age INT
    )
    '''

    cursor.execute(sql_st)
    dbcon.commit()

    print("New Table Created Successfully")

    cursor.execute("SHOW TABLES")
    print("Tables in database:")
    for table in cursor.fetchall():
        print(table)

except Exception as e:
    print("ERROR:", e)

finally:
    if dbcon:
        dbcon.close()