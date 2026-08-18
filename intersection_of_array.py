nums1 = [1,2,2,1]
nums2 = [2,2]
ans_array = []
if len(nums1)>len(nums2):
    
    seen = set(nums2)
    for x in seen:
     if x in nums1:
        ans_array.append(x)

else:
    seen = set(nums1)
    for x in seen:
         if x in nums2:
            ans_array.append(x)
print(ans_array)            
    

