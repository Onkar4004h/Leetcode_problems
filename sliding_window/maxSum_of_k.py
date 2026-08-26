def max_sum_ofSizeK(nums,k):
    freq={}
    l=0
    current_sum =0
    answer=0
    for r in range(len(nums)):
            current_sum+=nums[r]
            if nums[r] in freq:
                freq[nums[r]]+=1
            else:
                freq[nums[r]]=1
                      
            if r-l+1>k:
                current_sum-=nums[l]
                freq[nums[l]] -= 1

                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l+=1
            if r-l+1==k and len(freq)==k:
                answer=max(answer,current_sum)       
    return answer        

print(max_sum_ofSizeK([5,3,3,1,1],3))