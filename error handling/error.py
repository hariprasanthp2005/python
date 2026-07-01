
try:
    a= int(input("enter no 1:"))
    b= int(input("enter no 2:"))
    print(a+b)
    print(a/b)

except ValueError as err:
    print(err)

except ZeroDivisionError as err:
   print("cannot divide by zero")    

print("gm")


