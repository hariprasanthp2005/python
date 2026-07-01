fp= None

try:
    fp=open('user.txt','r')

except FileNotFoundError as error:
    fp=open('emp.txt','r')
    data=fp.read()
    print(data)
