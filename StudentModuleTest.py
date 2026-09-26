#this python file is used to craete a student class
  

from modules.student.student import StudentClass


email=input("Enter email: ")
password=input("Enter password: ")


s1=StudentClass()
s1.setusernameandpassword(email, password)

fullname=input("Enter full name: ")
date_of_birth=input("Enter date of birth: ")
age=input("Enter age: ")
gender=input("Enter gender: ")
mobile_number=input("Enter mobile number: ")
preffered_language=input("Enter preferred language: ")
school_college_name=input("Enter school/college name: ")
class_grade=input("Enter class/grade: ")
board_curriculum=input("Enter board/curriculum: ")
academic_year=input("Enter academic year: ")


s1.setprimarydetails(fullname, date_of_birth, age, gender, mobile_number, preffered_language, school_college_name, class_grade, board_curriculum, academic_year)


print("Student details:")
print("Full Name:", s1.full_name)