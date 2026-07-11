#extract
import requests, mysql.connector,json
req_data=requests.get('https://dummyjson.com/products')
data=req_data.json()
data1=data['products']

#transfer
mysql_data = []
for emp in data1:
    if emp['category']=='beauty':
        mysql_data.append(
        (
            emp['id'],
            emp['title'],
            emp['price'],
            emp['category'],
            emp['rating']
        )
    )
#print(emp)   

#load
try:
    dbcon=mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='hari@2005',
                                database='dbone'
)
    cursor=dbcon.cursor()
    sql_st='''
            SELECT * FROM employees1
            ;'''
    cursor.execute(sql_st,)
    employee=cursor.fetchall()
    dbcon.commit()
    print("reading successfully")

except Exception as e:
    print(e)