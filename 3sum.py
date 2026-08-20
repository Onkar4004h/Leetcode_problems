nums = [0,0,0]
nums.sort()
ans_array = []
x = 0
check_prev = None
for x in range(len(nums)):
    if nums[x]==check_prev:
        continue

    l=x+1
    r = len(nums)-1
    while l<r:
        total = nums[x]+nums[l]+nums[r]
        if total==0:
            
            ans_array.append([nums[x],nums[l],nums[r]])
            l+=1
            r-=1
            while l<r and nums[l]==nums[l-1]:
                l+=1
            while l<r and nums[r]==nums[r+1]:
                r-=1    
        elif total<0:
            l+=1
        else:
            r-=1
               
    check_prev=nums[x]    
           

print(ans_array)             

    
     
    
       
