def count_dist_primes(num):

    i = 2
    num_array = [] 
    while num>1:
        if num%i == 0:
            num = num//i
            if i not in num_array:
                num_array.append(i)
        else:
            i +=1
    print(num_array)
count_dist_primes(60)  