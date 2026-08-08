nums = [-100,-70,-60,110,120,130,160]
ans_array = []
check_array = []
i=0
j=i+1
k=len(nums)-1

while j<len(nums) and k>=0:
    if nums[i]+nums[j]+nums[k]==0:
        if i != j and i != k and j != k:
            # ans_array.append(([nums[i],nums[j],nums[k]]))
            
            x = [nums[i],nums[j],nums[k]]
            x.sort()
            if x not in ans_array:
                    ans_array.append(x)
            i+=1
            j+=1
            k=len(nums)-1
    if k==0:
     i+=1
     j+=1
    else:        
     k-=1
    
print(ans_array)
          

