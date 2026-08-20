nums1 = [1]

m = 1
nums2 = []
n = 0
if n==0:
     nums1=nums1
elif nums1[m-1]>nums2[0] and nums1[0]<nums2[-1]:
    nums1[m-1],nums2[0]=nums2[0],nums1[m-1]
    for x in range(n):
        nums1[m+x]=nums2[x] 
else:   
    l=0
    r=0
    while r<len(nums2):
        if nums1[l]>nums2[r]:
           nums1[l],nums2[r]=nums2[r],nums1[l]
        l+=1
        r+=1
        for x in range(n):
                nums1[m+x]=nums2[x] 
print(nums1)

      