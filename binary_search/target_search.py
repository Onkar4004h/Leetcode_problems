def target_search(nums,target):
    l = 0
    r = len(nums)-1
    mid = (l+r)//2
    if l == r:
        if nums[l] == target:
            return l
    while l<=r:
        mid = (l+r)//2
    
        if nums[mid]<target:
            l = mid + 1
        if nums[mid]> target:
            r = mid - 1
        if nums[mid]==target:
            return mid
    return -1 

nums = [-1,0,3,5,9,12]
print(target_search(nums,2))                    

    