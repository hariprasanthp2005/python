import requests
import json
import csv
try:
    emp=requests.get("https://dummyjson.com/products1")
    emp1=emp.json()["products"]
except requests.exceptions.RequestException:
    emp=requests.get("https://dummyjson.com/products")
    emp1=emp.json()["products"]
    
emp_json=[]
for e in emp1:
    emp_json.append({
                     "product_id":e["id"],
                     "product_name":e["title"],
                     "category":e["category"],
                     "price":e["price"],
                     "rating":e["rating"]
                     })
    
f1=open("emp.json","w")
json.dump(emp_json,f1)
print("data transferred")  

