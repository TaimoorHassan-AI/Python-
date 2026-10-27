import random
import string
passwords={}
try:
    with open("passwords.txt","r")as file:
        for line in file:
            website,pwd=line.strip().split(":")
            passwords[website] =pwd

except:
    pass
def generate_password():
    chars=string.ascii_letters+string.digits +"%$!@#$*"
    password="".join(random.choice(chars) for _ in range(8))

while True:
    print("\n----Personal Password Manager-----") 
    print("1.Save Password")
    print("2.View Password")
    print("3.Generate Password")
    print("4.Exit")

    choice=input("enter Your Choice: ")
    if choice=="1":
        site=input("enter Website: ")
        pwd=input("enter Password: ")

        passwords[site]= pwd 

        with open("passwords.txt","a") as file:
            file.write(f"{site}:{pwd}\n")
        print("saved!")  
    elif choice=="2":
        if not passwords:
            print("No Data")     
        else:
            for site,pwd in passwords.items():
                print(site,":",pwd)   
    elif choice == "3":

        print("Generated password:", generate_password())

    elif choice =="4":
        print("ok bye")
        break
    else:
        print("In-valid Input")                  



