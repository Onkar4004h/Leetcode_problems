#Add a system to calculate years to pay loan
#Add option to just check just balance
principle = int(input("Enter loan amount: "))
print(f"On the loan of {principle} you will get 7% interest")
print(f"your interest is {int(principle*0.07)}") 
while principle != 0:
    pay_amount = float(input("Amount:")) #input to ask amount
    interest = (input("Did you pay your interest? ")).lower() #asking if interest paid or not
    if interest == "yes":
        principle = (principle - pay_amount) #calculate if interest paid
        print(f" your principle amount is {principle:.2f} and interest is {(principle*0.07)/12:.2f}")
    elif interest == "no": 
         principle = (principle + (principle*0.07)/12 - pay_amount) #calculate if interest not paid
         print(f"Your principle amount is {principle:.2f} and interest is {(principle*0.07)/12:.2f}")


        
   