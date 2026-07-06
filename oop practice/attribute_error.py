class Student:

    def __init__(self, name):
        name = "Changed"

hari = Student("Hari")

print(hari.name)

'''
hari = Student("Hari")

Python conceptually does:

Student.__init__(hari, "Hari")

Inside __init__():

self → hari object

name = "Hari"

Memory looks like:

Local Variables

name = "Hari"
Step 2

Next line:

name = "Changed"

Now:

Local Variables

name = "Changed"

Did we change the object?

❌ No.

We only changed the local variable.

Step 3

__init__() finishes.

The local variable disappears.

name ❌ Destroyed
Now look at the object
hari Object

???

Does it have:

self.name

No.

Because we never wrote:

self.name = name

So the object is still empty.

Step 4

Now Python executes:

print(hari.name)

Python looks inside the object.

hari

name ?

Not Found

So Python raises:

AttributeError:
'Student' object has no attribute 'name'
'''