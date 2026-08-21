def insert_search(nums,target):

    l = 0
    r = len(nums)-1
    mid = (l+r)//2
    if l==r:
        if nums[l]==target:
            return l  
    while l<=r:
        mid = (l+r)//2
        if nums[mid]>target:
            r=mid-1
        if nums[mid]<target:
            l=mid+1
        if nums[mid]==target:
            return mid
    return l

print(insert_search([1,3,5,6],7))  

                    

            