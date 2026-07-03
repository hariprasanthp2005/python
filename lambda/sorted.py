#sorted() → custom sorting
marks=[
    ("hp",98),
    ("vk",89),
    ("ab",95),
    ("cg",70)
]

marks1=sorted(marks,key=lambda x:x[1],)
print(marks1)

jobs = [
    ("TCS", 30000),
    ("Infosys", 50000),
    ("Wipro", 25000)
]

sorted_jobs = sorted(jobs, key=lambda x: x[1])
print(sorted_jobs)