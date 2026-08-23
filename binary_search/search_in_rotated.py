def search_in_rotated(nums,target):
    l=0
    r = len(nums)-1
    mid = (l+r)//2

    if l==r:
        if nums[l]==target:
            return l
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==target:
            return mid
        if nums[l]<=nums[mid]:
            if nums[l]<=target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if nums[r]>=target>nums[mid]:
                l=mid+1
            else:
                r=mid-1            
                  
    return -1

print(search_in_rotated([5,1,2,3,4],0))
def two_pointer_search(nums,target):
    l=0
    r=len(nums)-1
    mid1=(l+r)//2
    mid2 = mid1
    if l==r:
        if nums[l]==target:
            return l
    while l<=r:
        if nums[l]==target:
            return l
        if nums[r]==target:
             return r
        if nums[mid1]==target:
             return mid1
        if nums[mid2]==target:
             return mid2
        l+=1
        r-=1
        mid2+=1
        mid1-=1
        
    return -1 
# print(two_pointer_search([6,7,8,1,2,3,4,5],3))   
             