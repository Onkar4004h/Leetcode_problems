nums = [-1,0,1,2,-1]
nums.sort()
i = 0
j = len(nums) - 1
x = 0
len_ = len(nums)
while x < len_ and i < len(nums) and j < len(nums):
    y = -nums[x]
    if nums[x] != nums[i] and nums[x] != nums[j]:
        if i!=j:
            if nums[i] + nums[j] == y:
                print(nums[i], nums[j], nums[x])
                x+=1   
                i=0
                j=len_-1
            elif nums[x] < nums[i]:
                j-=1
            elif nums[x] > nums[i]:
                i+=1
        else:
            x+=1
            i=0
            j=len_-1

    else:
        i+=1
    
     
    
       
