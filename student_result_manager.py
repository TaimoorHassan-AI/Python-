student={}
while True:
    print("\n Student Manager App")
    print("1.add Students")
    print("2.view Students")
    print("3.view Result")
    print("4.exit")

    choice=input("enter your choice:")
    if choice=="1":
        name =input("enter Student name: ")
        marks=int(input("enter marks: "))
        student[name]=marks
        print(f"{name} succesfully added ")
    elif choice=="2":
        if not student:
            print("no Student found") 
        else:
            for name,marks in student.items():
                print(name,":",marks)
    elif choice=="3":
        name =input("enter student name")
        if name in student:
            marks=student[name]

            if marks>=40:
                print("PASS")
            else:
                print("fail")
        else:
            print("student Not found")
    elif choice =="4":
        print("exiting")
        break
    else:
        print("invalid")


