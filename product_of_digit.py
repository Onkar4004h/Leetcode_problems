def product_of_digit(num):
    num_array = []
    product = 1
    while num >0:
        r = num%10
        num = num//10
        num_array.insert(0,r)
    for i in num_array:
        product = product*i
    return product

print(product_of_digit(5832))            