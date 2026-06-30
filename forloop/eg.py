#all employee male name
for emp in employees:
    if emp["gender"]=="male":
        print(emp["ename"],"-",emp["gender"])

        
malecount=0
femalecount=0

for emp in employees:
    if emp['gender']=="Male":
        malecount=malecount+1
    else:
        femalecount=femalecount+1


print(malecount)
print(femalecount)

numbers=[11,20,15,29,366]

i=0
while i<=len(numbers)-1:
    print(numbers[i])
    i=i+1