def second_largest_fact(num):
    num_array = []
    for i in range(1,num+1):
        if num%i == 0:
            num_array.insert(0,i)
    return num_array[1] 

print(second_largest_fact(60))      