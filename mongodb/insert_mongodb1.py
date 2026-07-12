import pymongo

try:
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client["students"]
    db_col=db["emp"]
    db_col.insert_one({"eid":"02","ename":"hp"})
    print("data transferred successfully")

except Exception as e:
    print("print data transferred successfully")