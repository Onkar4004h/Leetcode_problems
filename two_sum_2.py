numbers = [5,25,75]
target =100
l = 0
r = len(numbers) - 1
ans_array =[]
while l<r:
  if numbers[l]+numbers[r]==target:
    ans_array.append(l+1)
    ans_array.append(r+1)
    break
  elif numbers[l]+numbers[r]<target:
     l+=1
  else:
    r-=1
ans_array.sort()
print()       
      