def divisor_sort(num):
    num_array = []
    for i in range(1,num+1):
        if num%i==0:
            num_array.insert(0,i)
    print(num_array) 


divisor_sort(36)           