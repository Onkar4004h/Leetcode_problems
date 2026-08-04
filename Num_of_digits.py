def num_of_digits(num):
    num_array = []
    while num>0:
        r = num%10
        num = num//10
        num_array.insert(0,r)
    return len(num_array)  

print(num_of_digits(987654))  