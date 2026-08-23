def find_min(nums):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]<nums[l] and nums[mid]<nums[r] and nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
            return nums[mid]
        if nums[mid]>=nums[l]:
            if nums[l]>nums[r]:
                l =mid+1   
            else:
                r=mid-1        
        else:
            if nums[l]<nums[r] or nums[mid]<nums[mid+1]:
                r=mid-1        
            else:
                l=mid+1
    return  nums[mid]            
print(find_min([5,1,2,3,4]))                
                                  