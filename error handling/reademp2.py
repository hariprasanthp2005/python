fp= None

try:
    fp=open('emp.txt','r')

except FileNotFoundError as error:
    fp=open('user.txt','r')
    
data=fp.read()
print(data)