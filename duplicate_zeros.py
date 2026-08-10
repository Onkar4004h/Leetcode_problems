arr = [1,2,3]
i=0
while i<len(arr):
    if arr[i]==0:
       arr.insert(i+1,0)
       i+=2
       del arr[-1]
    else:
        i+=1 
print(arr)



             


           