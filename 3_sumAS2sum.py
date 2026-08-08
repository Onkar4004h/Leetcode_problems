nums = [0,0,0,0]
nums.sort()
l = 0
r = len(nums) - 1
x=len(nums)-1
ans_array =[]
while x!=0:
  target=(-nums[x])
  if x!=l and l!=r and x!=r:
    if nums[l]+nums[r]==target:
        y = [nums[l],nums[r],nums[x]]
        y.sort()
        if y not in ans_array:
           ans_array.append(y)
           l+=1
           r-=1
        else:
           l+=1
           r-=1   
    elif nums[l]+nums[r]<target:
         l+=1 
    else:
     r-=1        
  else:
     r-=1
  if r <= l:
        x -= 1
        l = 0
        r = len(nums) - 1 
 


print(ans_array)    
      
