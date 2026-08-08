nums = [2,-1,-4]
ans_array = []


x=0
i =0
j = i+1
len_ofNums= len(nums)
while x!=len_ofNums and i<len(nums):
    y = -nums[x]
    if x==j:
         j+=1

    if j==len_ofNums:
        # if x<len(nums):

        i= 0
        j=i+1
         
    if nums[i]+nums[j]==y:
        ans_array.append([nums[x],nums[i],nums[j]])
        x+=1
    i+=1
    j+=1
    
    if (-y) != nums[x]:
        i=0
        j=i+1

print(ans_array)