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

tution subjects=input("enter tution sub")
subject levels=input("enter sub lev")
topics needinghelp= input("enter the topics")
preffered communnication method=input("enter the method")


s1.academicrelateddetails(tuition_subjects,subject_levels,preferred_communication_method) 

parent_guardian_name=input("enter parent guardian name")
parent_guardian_relationship=input("enter parent_guardian_relationship")
 