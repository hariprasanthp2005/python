import requests, mysql.connector,json
#extract
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
        create table employees1(
	    id int primary key,
	    name varchar(50) not null,
	    price float,
	    category varchar(32),
	    rating float

''' 
    cursor.execute(sql_st)
    dbcon.commit()
    print("data created successfully")

except Exception as e:
    print(e)




