# Q5
credit = int(input("Enter your credit score: "))
payment = input("Do you have late payemnts? YES or NO:  ")

if credit > 700 and payment == "no":
    print("eligible")
elif credit <= 700 and payment == "no":
    print("Not eligible due to low credit.")
elif credit > 700 and payment == "yes":
    print("Not eligible due to late payments.")