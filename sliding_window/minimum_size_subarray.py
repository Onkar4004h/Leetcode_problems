def minimum_size_subarray(target,nums):
    l=0
    answer=len(nums)+1
    current_sum=0
    for r in range(len(nums)):
        current_sum+=nums[r]
        if current_sum>=target:
            while current_sum>=target:
                answer=min(answer,r-l+1)
                current_sum-=nums[l]
                l+=1
        
    if answer<=len(nums):
        return answer
    if answer==(len(nums)+1):
        return 0

print(minimum_size_subarray(11,[1,2,3,4,5]))            