def find_duplicate(nums):
    freq={}
    for x in nums:
        if x in freq:
            freq[x]+=1
            if freq[x]==2:
                return x
        else:
            freq[x]=1
print(find_duplicate([3,1,3,4,2]))            