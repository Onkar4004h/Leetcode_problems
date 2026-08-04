def find_missing_el(nums):
    arr=[]
    small = 0
    large = 10**5
    for x in nums:
        if x ==1:
                large=x
        if x<large:
              large = x        
        if x>small:
            small = x 
              
    for i in range(large,small+1):
        if i not in nums:
             arr.append(i)
    
    return arr 

print(find_missing_el([5,1]))   
