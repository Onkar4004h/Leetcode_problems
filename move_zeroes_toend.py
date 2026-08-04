nums=[1,2,3,1]

l = 0
r = l+1
while r<len(nums) and l<len(nums):
    if nums[l]!=0:
        l+=1
        
        
    if nums[r]!=0 and nums[l]==0:
        
        nums[r],nums[l]=nums[l],nums[r]
        l+=1

      
    r+=1      




print(nums)        





                       


