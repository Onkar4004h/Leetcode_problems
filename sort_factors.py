def sort_factors(num):
    num_array = []
    small_array = []
    large_array = []
    for a in range(1,int(num**0.5)+1):
        for b in range(1,num+1):
            if a*b==num:
                    small_array.append(a)

                    large_array.append(b)
    large_array.reverse()            
                
    small_array.extend(large_array)
    
    for x in small_array:
        if x not in num_array:
            num_array.append(x)
    return num_array

           
        
        
                