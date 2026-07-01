import requests
import json
import csv

try:
    emp=requests.get("https://dummyjson.com/products1")
    emp1=emp.json()["products"]
except requests.exceptions.RequestException:
    emp=requests.get("https://dummyjson.com/products")
    emp1=emp.json()["products"]


emp_csv=[]
for e in emp1:
    emp_csv.append([e["id"],e["title"],e["price"],e["rating"],e["category"]])

f1=open("emp.csv","w",newline="")
emp2=csv.writer(f1)
emp2.writerow(["product id","product name","price","rating","category"])
emp2.writerows(emp_csv) 
print("data transfered") 