def contains_duplicate(nums):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x]+=1
            if freq[x]==2:
                return True
        else:
            freq[x]=1
    return False
print(contains_duplicate([1,2,3,4]))