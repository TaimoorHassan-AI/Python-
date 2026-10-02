print("-------STUDENT MANAGEMENT SYSTEM---------")

students=[]

name=input("Enter name:")
roll_no=int(input("enter roll no:"))
dept=input("Enter Department:")
attended=int(input("enter no of attended classes:"))

student={
    "name":name,
    "roll_no":roll_no,
    "dept":dept,
    "total_classes":200,
    "attended ":attended

}
students.append(student)
print("ATTENDANCE STATUS:")
attendance =(student["attended "] /student["total_classes"])*100
print("attendance",attendance,"%")
courses = {"pf","applied physics","calculus"}
print("courses of the student Are :",courses)