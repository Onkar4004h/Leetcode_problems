def fact_count(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    print(count)

def fact_sum(num):
    count = 0  
    for i in range(1,num+1):
        if num%i==0:
            count = count + i       
    print(count) 

def perfect_fact(num):
    count = 0  
    for i in range(1,num):
        if num%i==0:
            count = count + i    
    if count == num:
     print(True)  
    else:
        print(False)

# def prime_num(num):
#     count = 0 
#     x = "" 
#     for i in range(1,num):
#         if num%i==0:
#             count = count + i 
#         else:
#             count = 2     
#     if count > 2:
#         x = "not prime"
#     elif count == 2:
#         x = "prime" 
#         print(x)   
#     return x       

# print(prime_num(4))
import math             
def fact_prim(num):
    if num == 2:
        return True
    if num < 2 or num%2==0:
        return False
    for i in range(2,num):
            if num%i == 0:
                return False
    return True  



def prime_nums(num):

    for i in range(2,num):
        if fact_prim(i):
            print(i)



def largest_prim(n):
   i = 2
   while i <n:
       if n%i ==0:
           n = n//i 
       else:
           i +=1   
   print(n)  

def greatest_divisor(num1,num2):
    factorsOfNumber1= []
    factorsOfnumber2 = []
    for i in range(2,num1+1):
        if num1%i == 0:
            factorsOfNumber1.append(i)
    for j in range(2,num2+1):
        if num2%j == 0:
            factorsOfnumber2.append(j) 

    smallesr_arr = smallest_Of2arr(factorsOfNumber1,factorsOfnumber2)
    bigger_arr = biggest_Of2arr(factorsOfNumber1,factorsOfnumber2)
    while len(smallesr_arr) > 0:
        biggest_noinSmallestArr = largestof_nums(smallesr_arr) 
        if biggest_noinSmallestArr in bigger_arr:
            return biggest_noinSmallestArr
        else:
            smallesr_arr.remove(biggest_noinSmallestArr)
            

     
    


def largestof_nums(arr):
    max = 0
    for num in arr:
        if num>max:
            max = num
    return max

      

def smallest_Of2arr(small,big):
    small_arr = len(small)
    big_arr = len(big)
    if small_arr < big_arr:
        return small
    else:
        return big

          
  
def biggest_Of2arr(small,big):
    small_arr = len(small)
    big_arr = len(big)
    if small_arr > big_arr:
        return big
    else:
        return small 



def gcd(num1,num2):
   arr = []
   for i in range(2,num2):
       if num1%i==0 and num2%i==0:    
           arr.append(i)
   return max(arr) 

def Egcd(a,b):
    while b > 0:
        q = a//b
        r = a -(b*q)
        a = b
        if r == 0:
            return b
        b = r
       

def lcm(num1,num2):
    small_table =[]
    large_table =[]
    for i in range(1,num1+1):
        small_table.append(num1*i)
    for j in range(1,num2+1):
        large_table.append(num2*j)
    for num in small_table:
        if num in large_table:
            return num

def rev_num(num):
    i = 1
    rev_numArr = []
    while num>0:
        r = num%10
        num = num//10
        rev_numArr.insert(0,r)
    print(rev_numArr)    
    result = 0
    for item in rev_numArr:
        item = item*i
        i = i*10
        result = result +item
    return result
rev_num(321)
def armstrong(num):
    orginial_num = num
    num_array = []
    result = 0
    while num>0:
        r = num%10
        num = num//10
        num_array.insert(0,r)
    for x in num_array:
        x = x**3
        result = result+x
    if result == orginial_num:
        
        return True    
    return False

   

        

       
            

                    


    

              