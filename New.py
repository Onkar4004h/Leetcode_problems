"""
#task 1
fruits = ["apple","banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
     break
 
#task 2

name = input("what is your name? ")

print("welcome " + name)

task 3
num1 = 5
num2 = 10
print(num1*num2)
 
 #task 3

num1 = (input("enter first number= "))
num2 = (input ("enter second number= "))


myinput1 = int(num1)
myinput2 = int(num2)
print("The sum is " , myinput1+myinput2)

num = input("Enter your number= ")
x = int(num)
if x%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#chat gpt task 4
  
def myfunc(n):
    return abs(n - 1000)

num1 = input("enter first number")
num2 = input("enter second number")
num3 = input("enter third number")

x = int(num1)
y = int(num2)
z = int(num3)


a = [x, y, z]
a.sort(key=myfunc)
print(a)                                                  

#chatgpt task5            

myin = input("Enter your number= ")

x = int(myin)
num = [1,2,3,4,5,6,7,8,9,10]
for y in num:
    print(x*y)

 #mosh task1

name = input("what is your name? ")                                                                     
color = input("What is your favourite color? ")
print(name + " likes " + color)

#mosh task2

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price

else:
    down_payment = 0.2 * price 

print(f"down payment: {down_payment}")


has_good_income = True
has_good_credit = False

if has_good_income or has_good_credit:
    print("eligible for loan")
else:
    print("Not eligible")

              
name = input("enter your name: ")

if len(name) < 3:
    print("Name must be atleast 3 character")

elif len(name) > 50:
    print("Name must be less than 50 characters")

else:
    print(f"welcome {name}")

     

weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit == "L" or unit == "l":
 print(f"your weight is {int(weight) * 0.453592} kg")

elif unit == "K" or unit == "k":
 print(f"your weight is {int(weight) / 0.453592} pounds")   

   
secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
 guess = int(input("Guess: ")) 
 guess_count += 1
 if guess == secret_num:
  print("you win!")
  break
else:
 print("You failed") 
   
 
Secret_num = 69
guess_count = 0
guess_limit = 10

while guess_count < guess_limit:
    guess = int(input("guess: "))

    guess_count += 1
    if guess == Secret_num:
        print("you win!")
        break 
else:
    print("you failed!")    
    
     

command = ""
started = False

while True:
    command = input(">").lower()
    if command == "start":
         if started:
             print("Car is already started!")
         else:
             started = True                  
             print("car started")
    elif command == "stop":
        if not started:
            print("car is already stop")
        else:
            started = False

            print("Car stopped")
    elif command == "help":
        #print("""
 #start - to start the car
#stop - to stop the car
#quit - to quit 
#              """) 
        
    #elif command == "quit":
     #   break
  #  else:
        #print("sorry, I don't understand  ")
"""       
n = int(input())
x = 0
while x<=10:
    print(n*x)
    x += 1
"""
def show(n):
    if n == 0:
        return 0
    else:
        i = 0
        i+=1
        print(n, i)
        return show(n - 1)
# x = show(5)
# print(x)

def fact(num, i = 2):
    if num == 1:
        return 1
    else:
        if num % i == 0:
            fact(num // i, i)
        else:
            fact(num, i + 1)

def rev(arr):
    arr = list(arr)
    l = 0
    r = len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l+= 1
        r-= 1 
    return arr

arr = 'string' 

def palidrome(word):
    word = list(word)
    l = 0
    r = len(word) - 1
    while l < r:
        if word[l] != word[r]:
            return False
        l+=1
        r-=1
    return True   
### 1. Count the Factors

# Given an integer n, return how many factors it has.

# *Example*


# Input: 36
# Output: 9


# Factors:
# 1 2 3 4 6 9 12 18 36
      
            
                

        

             
    

