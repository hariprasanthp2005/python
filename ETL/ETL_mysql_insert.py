'''
invoke Rest API and write User data to users table
Usage: fetch all users
Rest API URL:https://jsonplaceholder.typicode.com/users
Method Type:GET
Required Fiels:None 
Access Type:Public
'''
#extract
import requests
req_data=requests.get("https://jsonplaceholder.typicode.com/users")
users=req_data.json()
print(len(users))

#transfer
mysql_data=[]
for user in users:
    mysql_data.append((
        user['id'],
        user['name'],
        user['address']['city'],
        user['email']
    )
    )
#print(mysql)

#load
import mysql.connector
dbcon=None
try:
    dbcon=mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='hari@2005',
                                database='practice'
                                )
    cursor=dbcon.cursor()
    sql_st='''
               insert into emp(user_id,name,city,email)
               values(%s,%s,%s,%s);
               '''
    cursor.executemany(sql_st,mysql_data)
    dbcon.commit()
    print("data transfered")
except Exception as e:
    print(e)



