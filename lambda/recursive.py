def rec(num):
    if num==0:
        return 1
    else:
        return num*rec(num-1)
    
print(rec(8))
