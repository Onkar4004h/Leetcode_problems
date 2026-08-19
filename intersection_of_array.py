nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
ans_array = []
freq={}
for x in nums1:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
for y in nums2:
    if y in freq and freq[y]>0:
        ans_array.append(y) 
        freq[y]-=1
                 


    

