digits = [9]
digits.reverse()
ans_array=[] 
add = 0       
i = 1
for x in range(len(digits)):
    y=digits[x]*i
    add=add+y
    i=i*10
add=add+1
while add>0:
    r=add%10
    add=add//10
    ans_array.insert(0,r)
print(ans_array)    

