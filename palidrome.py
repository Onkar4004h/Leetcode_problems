def palidrome(num):
    orignial_num = num
    i = 1 
    rev_numarray = []
    while num >0:
        r = num%10
        num = num//10
        rev_numarray.insert(0,r)
    result = 0 
    for items in rev_numarray:
        items = items*i
        i = i*10
        result = result + items
    if result == orignial_num:
        return True
    return False  

print(palidrome(121))      