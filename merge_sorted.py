nums1 = [4,5,6,0,0,0]

m = 3
nums2 = [1,2,3]
n = 3
for x in range(n):
    nums1[m+x]=nums2[x]
l = 0
r = m
length = len(nums1)
while l<length and r<length:
    if n==0:
        break
    if l==r:
        break 
    if nums1[l]>nums1[r]:
        nums1[l],nums1[r]=nums1[r],nums1[l]
        if nums1[l]>nums1[l+1]:
            nums1[l],nums1[l+1]=nums1[l+1],nums1[l] 

        if n!=1 and (r+1) < length:
            if nums1[r]!=nums1[r+1]:
                r+=1
                     
    l+=1
          
    


    
      
  


print(nums1)    