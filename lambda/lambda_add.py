'''
In Python, lambda is a way to create a small anonymous function (a function without a name).

We use lambda when:

The function is small
We need it only once
Writing full def feels unnecessary

'''
addition=(lambda a,b:a+b)
print(type(addition))  #function
add=addition(10,20)
print(add)