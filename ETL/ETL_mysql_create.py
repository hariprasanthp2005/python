#Extract
import requests,mysql.connector
req_data=requests.get('https://dummyjson.com/products')
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
    sql_st='''CREATE TABLE emp(
               user_id INT,
               name VARCHAR(100),
               city VARCHAR(100),
               email VARCHAR(100)
            );'''
    cursor.execute(sql_st)
    dbcon.commit()
    print("User Data inserted successfully")
except Exception as err:
    print(err)