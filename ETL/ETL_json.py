import requests, mysql.connector,json
#extract
req_data=requests.get('https://dummyjson.com/products')
data=req_data.json()
data1=data['products']

#transfer
json_data = []
for emp in data1:
    if emp['category']=='beauty':
        json_data.append(
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
fp1=open("json_products",'w')
json.dump(json_data,fp1)
print("file created successfully")