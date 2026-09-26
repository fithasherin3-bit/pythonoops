#this python file is used to craete a student class
  

from modules.student.student import StudentClass


email=input("Enter email: ")
password=input("Enter password: ")


s1=StudentClass
s1.setusernameandpassword(email, password)