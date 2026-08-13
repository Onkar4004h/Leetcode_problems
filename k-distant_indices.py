nums = [2,3,9,3,5,9,2,1]
key =9
k = 1
i = 0
ans_array = []
for j in range(0,len(nums)):
    if nums[j]==key:
        check = j+k
        while i<(check+1) and i<len(nums):
            if abs((i-j))<=k:
                if i not in ans_array:
                    ans_array.append(i)
                    i+=1
            else:
                i+=1       
    if len(ans_array)==len(nums):
        break
print(ans_array)                        
