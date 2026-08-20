n = 4421
num_array=[]
product =  1
sum = 0
while n>0:
        r = n%10
        n = n//10
        num_array.insert(0,r)
for x in num_array:
        product= product*x
        sum = sum+x
difference = product-sum                
print(difference)        