import pymongo

try:
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client["students"]
    db_col=db["emp"]
    employees=[
                {"eid":"01","ename":"hp"},
                {"eid":"02","ename":"vk"},
                {"eid":"03","ename":"cheeku"},
                {"eid":"04","ename":"veeru"},
                {"eid":"05","ename":"rp"}
            ]
    db_col.insert_many(employees)
    print("data transferred successfully")

except Exception as e:
    print(e)