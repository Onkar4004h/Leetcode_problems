def sum_of_squares(c):
    array_range = int(c**0.5)
    check_array=[]
    for i in range(0,array_range+2):
        check_array.append(i)
    l=0
    r=len(check_array)-1
    while l<len(check_array) and r>-1:
        if (check_array[l]**2)+(check_array[r]**2)==c:
            return True
           
        elif (check_array[l]**2)+(check_array[r]**2)>c:
            r-=1
        else:
            l+=1     
    return False

print(sum_of_squares(5))
