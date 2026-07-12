import pymongo

try:
    data=pymongo.MongoClient("mongodb://localhost:27017/")
    db=data["student"]
    emp_col=db["emp"]
    emp_col.insert_one({"eid":'01',"ename":'hari'})
    print("data transferred")

except Exception as e:
    print(e)