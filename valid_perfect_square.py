def valid(num):
    l=1
    squares = l*l
    while l*l<(num+1):
        if l*l==num:
            return True
        else:
            l+=1
    return False

print(valid(80))           