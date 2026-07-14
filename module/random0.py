#generate a 4 digit otp number

import random

print(random.randint(1000,9999))

#to print 10 time use while loop

i=0
while i<10:
    print(random.randint(1000,9999))
    i=i+1
