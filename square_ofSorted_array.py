def sort_suqaring(nums):
    num_square = []
    if sum(nums)<0:
           nums.reverse()
          
    for x in nums:
            num_square.append(x**2)
    ans_array=[]
    new_arr = num_square[:]
    l=0
    r = len(num_square)-1
    while l<r:
          if num_square[l]>=num_square[r]:
                ans_array.insert(0, num_square[l])
                new_arr.remove(num_square[l])
                l+=1
          elif num_square[r]>=num_square[l]:
                ans_array.insert(0, num_square[r])
                new_arr.remove(num_square[r])
                r-=1
    if len(new_arr)==1:
        ans_array.insert(0, num_square[l])
    # ans_array.reverse()
    return ans_array            
          
          
                      

    # l = 0
    # r = len(num_square)-1
    # num_square_copy = num_square[:]
    # mins = min(num_square_copy)
    # while l<r:
    #         if num_square[l]>=num_square[r]:
    #             num_square[l],num_square[r]=num_square[r],num_square[l]
                  
    #         r-=1

    #         if num_square[l]==mins:

    #               l+=1
    #               r=len(num_square)-1
    #               num_square_copy.remove(mins)
    #               mins = min(num_square_copy)
                  
            
            

    
nums = [-9, -5, -4,-1,0,3,10]
print(sort_suqaring(nums))


              



    

