pin = 123


attempts =3
while attempts >0:
    pinp=int(input("enter your pin:"))
    if pin== pinp:
        print("attempt succesful")
        break
    else:
        attempts -=1
        print("not succesful")
    if attempts ==0:
        print("no attempts left")

print("------ BANK DETAILS-----")

print("1.current account")
print("2.savings account")

choice =int(input("enter your Account type:"))

if choice==1:
    print("your account type is current")
elif choice==2:
    
    print("your account type is savings")
else:
    print("invalid account type")


balance =5000
print("your bank account balance is :",balance)
print("withdraw money or deposit money?")
choice2=int(input("enter your choice :"))
if choice2==1:
    print("you can withdraw money ")
    withdraw=int(input("enter amount to withdraw"))
    withdraw= balance - withdraw
    print("your desired amount has been withdrawn")
    print("your newbalance is:",withdraw)
elif choice2==2:
    print("you can deposit money")
    deposit=int(input("enter amount to deposit:"))
    deposit = deposit +balance
    print("your desired amount has been deposit")
    print("your newbalance is:",deposit)
else:
    print("not a desired output")