def remove_duplicate(nums):
    w = 0
    r = w+1
    up = 1
    while r<len(nums):
        if nums[w]==nums[r]:
            w+=1
            r+=1
        else:
            nums[up]=nums[r]
            up+=1
            r+=1
            w+=1
    return up
            


print(remove_duplicate([0,0,1,1,2,2]))   






   
 

        