emp={'hp','vk','cg','ddp','ab','kp','jh'}

# emp.pop()
print(emp)

emp.remove('cg')
print(emp)

emp.discard('hiii') #no erroe
print(emp) 

emp.remove('hiii')  #key error
print(emp)