"""
Imagine I give you this array:

[4, 7, 2, 9, 1]

Questions like:

What's the largest number?
What's the smallest?
How many even numbers are there?
Reverse the array.
Is it sorted?
Find the index of 9.
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

    """
#to find the largest num
def largest_num(num):
    count = 0
    for x in num:
        if x >count:
            count=x
    return count

#to find number of even numbers present
def even_num(num):
    count = 0
    for x in num:
        if x%2 ==0:
            count += 1
    return count

#to reverse the list
def reverse(num):
    new = []
    for x in range(len(num)-1,-1,-1):
        new.append(num[x]) 
    return new     

#to sort the numbers in a list in ascending order
def sort(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] > num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
    return num

#to find index of a number ,here we use to find index of 9 in a list
def index(num):
    for x in range(len(num)):
        if num[x] ==9:

         return x   

#calculator
def calculator(num1,num2,operator):
 if operator == "+":
    result = num1+num2
 elif operator == "-":
    result = num1-num2
 elif operator == "*":
    result = num1*num2
 elif operator =="%":
    result = num1/num2
 else:
    result ="sorry i cannot do it yet"
 return result

principle = 0      
while True:
 bank_start = input("""how can we assist you sir:
 1.New Loan
 2.check remaining loan amount
 3.calculate interest
 4.Deposit amount                   
 5.quit
                   
""").lower()
 if bank_start == "1":
  principle_input = int(input("Enter loan amount: "))
  principle = principle_input
  print(f"On the loan of {principle} you will get 7% interest")
  print(f"your interest is {int(principle*0.07)}") 
  while principle != 0:
      pay_amount = int(input("Amount:"))
      if pay_amount > 0:
        interest = (input("Did you pay your interest? ")).lower()
        if interest == "yes": 
            principle  = principle - pay_amount
            print(f" your principle amount is {principle:.2f} and interest is {principle*0.07:.2f}")
           
        elif interest == "no":
           principle = principle + (principle*0.07)
           print(f"Your principle amount is {principle:.2f} and interest is {principle*0.07:.2f}")
         
      elif pay_amount ==0:
         break  
 if bank_start =="2":
  if  principle > 0:
     print(principle)
  else:
     print("take a loan first")
 if bank_start == "3":
  if principle > 0:
   print(f"Your interest is {principle*0.07/12:.2f}")
  else:
   print("take a loan first")
 elif bank_start == "4":
    if principle > 0:
        deposit = int(input("Enter amount to deposit: "))

        if deposit <= principle:
            principle = principle - deposit
            print(f"Remaining loan amount: {principle}")
        else:
            print("You cannot deposit more than your remaining loan.")
    else:
        print("Take a loan first.")
 if bank_start =="5":
    break





 





