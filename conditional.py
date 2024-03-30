cre = input("Enter your credit score? ")
cri = input("Have you done any crime in the past?(yes/no) ")

crime = False

if crime == 'yes':
    crime = True
else:
    crime = False
amount = input("Please enter loan amount? ")

credit = int(cre)

if credit > 800 and not crime:
    print(f"No paper work need, you will get the loan amount {amount}")
elif 650 < credit <= 800 and not crime:
    # credit >=650 and credit<=800
    # credit >=650 or credit<=800
    # credit >=650 not credit<=800
    print(f"Need to submit papers, you will get the loan amount {amount}")
else:
    print(f"You don't get the loan of amount {amount}")
