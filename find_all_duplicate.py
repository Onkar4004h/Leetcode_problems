nums = [4,3,2,7,8,2,3,1]
ans_array = []
freq={}
for x in nums:
    if x in freq:
        freq[x]+=1
        if freq[x]==2:
            ans_array.append(x)
    else:
        freq[x]=1
print(ans_array)        
