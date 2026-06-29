b=bytes([10,20,30,40])   
for element in b:     #bytes is immutable . cannot be changed after creation.
    print(element)

ba=bytearray([10,20,30,40])
ba[3]=100     #bytearray is mutable

for element in ba:
    print(element)