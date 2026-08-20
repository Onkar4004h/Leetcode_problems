nums = [0,3,7,2,5,8,4,6,0,1]
num_map = {x:1 for x in nums}
longest = 0
for x in num_map:
    if (x-1) not in num_map:
        count=1
        while x+count in num_map:
            count+=1
        longest =max(longest,count)                
      