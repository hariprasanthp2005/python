#Extract
import requests,mysql.connector
req_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=req_data.json()
print(len(users))

#Transform
mysql_data=[]
for user in users:
    mysql_data.append((
                    user['id'],
                    user['name'],
                    user['email'],
                    user['address']['city']
                    ))

#Load
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='hari@2005',
                                  database='practice')
    cursor=dbcon.cursor()
    sql_st='''
            SELECT * FROM emp
            ;'''
    cursor.execute(sql_st)
    emp=cursor.fetchall()
    dbcon.commit()
    print("reading successfully")
except Exception as err:
    print(err)