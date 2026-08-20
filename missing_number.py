nums = [9,6,4,2,3,5,7,0,1]
my_set = set(nums)
for x in range(len(nums)+1):
    if x not in my_set:
        print(x)