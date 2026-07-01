fp=None

try:
    fp=open('.txt','r')
    data=fp.read()
    print(data)

except FileNotFoundError:
    print("file not found")
  
