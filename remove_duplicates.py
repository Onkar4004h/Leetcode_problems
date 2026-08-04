
num_array = []
nums = [0,0,1,1,1,2,2,3,3,4]
nums_len = len(nums)
for num in nums:
    if num not in num_array:
        num_array.append(num)
num_array_len = len(num_array)
to_add = nums_len - num_array_len
for x in range(to_add):
    num_array.append("_")    
print(num_array)

