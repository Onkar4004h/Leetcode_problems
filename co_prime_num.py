def co_prime(num1,num2):
    num_array = []
    for x in range(1,min(num1,num2)):
        if num1%x==0 and num2%x==0:
            num_array.append(x)
    if len(num_array)>1:
        return False        
    return True         

print(co_prime(14,25))