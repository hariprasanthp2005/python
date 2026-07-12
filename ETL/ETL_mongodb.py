import requests, pymongo
#extract
req_data=requests.get('https://dummyjson.com/products')
data=req_data.json()
data1=data['products']

#transfer
mongodb_data = []
for emp in data1:
    if emp['category']=='beauty':
        mongodb_data.append(
        {
            'pid':emp['id'],
            'pname':emp['title'],
            'price':emp['price'],
            'category':emp['category'],
            'rating':emp['rating']
        }
    )
#print(emp) 
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client["student1"]
    db_col=db["beauty"]
    db_col.insert_many(mongodb_data)
    print("data transferred successfully")

except Exception as e:
    print(e)
