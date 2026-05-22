# Question 1) Create a student and create an object of that class


# class student:

#     def sample(self,name,age):
#         self.name = name
#         print(f"Name : {name}")
#         self.age = age
#         print(f"Age : {age}")

# obj = student()
# obj.sample("Abhishek",21)

#.     OR.     (solving by constructor method )

# class student:
#     def __init__(self,name,age):
#         self.name = name
#         print(self.name)
#         self.age = age
#         print(self.age)

# obj = student("Abhishek kumar singh",21)

""" NOTe --> yaha constructor method me function ko  call nhi kiya jata apne se object se 
hi call ho jate hai"""


# Question 2) create a Car class and create an object of that class

# class car:
#     def details(self,carName, carPrice):
#         self.carName = carName
#         print(f"CARNAME = {carName}")
#         self.carPrice = carPrice
#         print(f"CARPRICE = {carPrice}")

# store = car()
# store.details("bmw",2000)

# OR [solving by constructor method]

# class car:
#     def __init__(self,carname, carprice):
#         self.carname = carname
#         print(f"CAR NAME => {carname}")
#         self.carprice = carprice
#         print(f"CARPRICE ==> {carprice}")

# store = car("Audii",2000)


# QUESTION 3)) Use self key word create a class named Employee and create a method using self
#  keyword to print .Employee Name . Employee salary

# class Employee:
#     def employeeDetails(self , Employeename , Employeesalary):
#         self.Employeename = Employeename
#         self.Employeesalary = Employeesalary
#         print(f"EMPLOYEE SAlARY : {Employeename}")
#         print(f"Employee sailary : {Employeesalary}")

# obj = Employee()
# obj.employeeDetails("Abhishek ",40000)

# OR [By constructor method]

# class employee:
#     def __init__(self,employeename,employeesalary):
#         self.employeename = employeename
#         self.employeesalary = employeesalary

#         print(f"EMPLOYEE NAME : {employeename}")
#         print(f"EMPLOYEE SALARY : {employeesalary}")

# obj = employee("Abhishek kumar",200000)
# constructr functin me bina function ko call kiye hi print ho jata hai through object

# QUESTION - 4) Mobile class  create a class named Mobile.

# class Mobile:
#     def sample(self,BrandName, Ram):
#         self.BrandName = BrandName
#         self.Ram = Ram

#         print(f"BRAND NAME : {BrandName}")
#         print(f"Ram : {Ram}")

# obj = Mobile()
# obj.sample("MOTO", "5gb")


# QUESTION - 5) create a class named student and create a method show() using self keyword and print .name, .course

# class student:
#     def show(self,name,course):
#         self.name = name
#         self.course = course

#         print(f"Student name : {name}")
#         print(f"course name : {course}")

# obj = student()
# obj.show("Abhishek","python")


# Question 6) create a class named laptop and print laptop brand and proceesor

# class laptop:
#     def details(self , laptopBrand, processor):
#         self.laptopBrand = laptopBrand
#         self.processor = processor
        
#         print(f"laptop brand = {laptopBrand}")
#         print(f"laptop processor : {processor}")

# obj = laptop()
# obj.details("Apple","Apple Silicon")


# Question 7) create a class named Book and create atrribute .Book name .Book price

# class book:
#     def info(self,BookName , BookPrice):
#         self.BookName = BookName
#         self.BookPrice = BookPrice
#         print(f"Book name = {BookName}")
#         print(f"Book price = {BookPrice}")
      
# obj = book()
# obj.info("Dark horse" , 499)
    

# Question 8) create a class named Teacher and create method using self key word  to print

# class Teacher:
#     def show(self,TeacherName,subject):
#         self.TeacherName = TeacherName
#         self.subject = subject

#         print(f"TEACHER NAME : {TeacherName}")
#         print(f"SUBJECT : {subject}")

# details = Teacher()
# details.show("Rahul sir" ,"Math")

#Question 9) create a class named Animal. and create two different objects and print

# class Animal:
#     def info(self,AnimalName):
#         self.AnimalName = AnimalName
#         print(f"Animal Name = {AnimalName}")

# obj1 = Animal()  # OBJect1 
# obj1.info("cat")
# obj2 = Animal()  # object2
# obj2.info("Dog")


# Question 10) create a class named Bank and store Account Holdername , Balance 

# class Bank:

#     def info(self,AccountHolderName,Balance):
#         self.AccontHolderName = AccountHolderName
#         self.Balance = Balance

#         print(f"Account Holder Name ==> {AccountHolderName}")
#         print(f"Balance ==> {Balance}")

# details = Bank()
# details.info("Abhishek kumar singh",400000000)



#.        ----------- -------- COMPLETE --------------------