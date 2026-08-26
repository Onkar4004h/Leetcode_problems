def max_consecutive_one(nums,k):
    l=0
    count=0
    answer = 1
    for r in range(len(nums)):
        if nums[r]==0:
            count+=1
        else:
            while count>k:
                if nums[l]==0:
                    count-=1
                l+=1
            answer=max(answer,r-l+1)           
            
    return answer            
print(max_consecutive_one([1,1,1,0,0,0,1,1,1,1,0],2))                
