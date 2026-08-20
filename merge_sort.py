def merge_sort(nums):
    if len(nums)==1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    l = 0
    r=0
    ans_array = [0]*len(nums)
    k=0
    while len(left)>l and len(right)>r:
        if left[l]>right[r]:
            ans_array[k]=right[r]
            r+=1
        else:
            ans_array[k]=left[l]
            l+=1
        k+=1
    while len(left)>l:
        ans_array[k]=left[l]
        l+=1
        k+=1
    while len(right)>r:
        ans_array[k]=right[r]
        r+=1
        k+=1        
    return ans_array

print(merge_sort([8,4,3,6]))
