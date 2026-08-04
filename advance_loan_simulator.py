while True:
 bank_start = input("""how can we assist you sir:
                   1.New Loan
                   2.check remaining loan amount
                   3.calculate interest
                   4.Deposit loan amount
                   5.quit
                   
                   """).lower()
 principle = 0

 if bank_start == '1':
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
            print(f" your principle amount is {principle} and interest is {principle*0.07}")
           
        elif interest == "no":
           principle = principle + (principle*0.07)
           print(f"Your principle amount is {principle} and interest is {principle*0.07}")
         
      elif pay_amount ==0:
         break
 if bank_start =="2":
   if principle > 0:
     print(f"your principle is {principle:.2f}")
   else:
     print("take a loan first")
 if bank_start == "3":
  if principle > 0:
   print(f"Your interest is {principle*0.07}")
  else:
   print("take a loan first")

 if bank_start =="quit":
    break





 



