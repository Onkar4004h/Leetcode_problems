nums = [-1,0,1,2,-1,-4]
nums.sort()
for j in range(len(nums)-1,-1,-1):
    if nums[j]<1:
        print(j)
        break
index = j    
x=len(nums)-1
i=0
while x!=index:
    if nums[i]+nums[j]!=(-nums[x]):
       j-=1
    elif i==j:
            continue   
     
    elif i ==0 and j ==i+1:
        i+=1
        j = index
    else:
        j=index      
    
       
