nums=[1,2,3,4]
l=0
store = 0
n = len(nums)
while l<n:
    i=l+1
    if n%i==0:
       store = store+(nums[l]*nums[l])
       l+=1
    else:
        l+=1
print(store)           