def find_average_ofSubarray(nums,k):
    l=0
    ans_array=[]
    current_sum = 0
    for r in range(len(nums)):
        current_sum+=nums[r]
        if r-l+1>k:
            current_sum-=nums[l]
            l+=1
        if r-l+1==k:
            answer=current_sum/k
            ans_array.append(answer)
    return ans_array

print(find_average_ofSubarray([1, 3, 2, 6, -1, 4, 1, 8],5))        


