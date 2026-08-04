def sum_of_digits(num):
    num_array = []
    product = 0
    while num >0:
        r = num%10
        num = num//10
        num_array.insert(0,r)
    for i in num_array:
      product = product+i
    return product

print(sum_of_digits(5823))      