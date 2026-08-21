def first_last_index(nums,target):
    first = -1
    last = -1
    l=0
    r=len(nums)-1
    mid  = (l+r)//2
    if l==r:
        if nums[l]==target:
          ans_array = [l]*2
          return  ans_array
        else:
           ans_array=[-1]*2
           return ans_array
    while l<=r:
        mid = (l+r)//2
        if nums[mid]>target:
          r=mid-1
        if nums[mid]<=target:
           l=mid+1
        if nums[mid]==target:
           last = mid
    l=0
    r=len(nums)-1
    while l<=r:
            mid = (l+r)//2
            if nums[mid]>=target:
              r=mid-1
            if nums[mid]<target:
               l=mid+1
            if nums[mid]==target:
               first = mid       


    return [first,last]

print(first_last_index([5,7,7,8,8,10],6))          
       

