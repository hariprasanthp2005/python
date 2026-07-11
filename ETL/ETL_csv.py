import requests, mysql.connector,json,csv
#extract
req_data=requests.get('https://dummyjson.com/products')
data=req_data.json()
data1=data['products']

#transfer
csv_data = []
for emp in data1:
    if emp['category']=='beauty':
        csv_data.append(
        (
            emp['id'],
            emp['title'],
            emp['price'],
            emp['category'],
            emp['rating']
        )
    )
#print(emp)  

#Load
fp1=open("csv_products",'w',newline="")
csv_data1=csv.writer(fp1)
csv_data1.writerow(['id','title','price','category','rating'])
csv_data1.writerows(csv_data)
print("file created successfully")