def target_search(nums,target):
    l = 0
    r = len(nums)-1
    mid = (l+r)//2
    if l == r:
        if nums[l] == target:
            return l
    while True:
    
        if nums[mid]<target:
            l = mid
        if nums[mid]> target:
            r = mid
        if nums[mid]==target:
            return mid
        mid = (l+r)//2
    return -1 

nums = [2, 5]
print(target_search(nums,5))                    

    