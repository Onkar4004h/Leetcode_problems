def common_fact(a,b):
    num_array = []
    for i in range(1,max(a,b)+1):
        if a%i ==0 and b%i==0:
            num_array.append(i)
    return len(num_array)

print(common_fact(12,6))

            
            