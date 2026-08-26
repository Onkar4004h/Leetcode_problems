def max_consecutive_one(nums,k):
    l=0
    count=0
    length=0
    answer = 1
    for r in range(len(nums)):
        if nums[r]!=0:
            length+=1
        else:
            if nums[r]==0:
                count+=1
                length+=1
            if count>k:
                l+=1
                length-=1
                count-=1
                answer=max(answer,length)
    return answer            
print(max_consecutive_one([1,1,1,0,0,0,1,1,1,1,0],2))                
