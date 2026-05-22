
#.                               DATE ==>   18 may,2026

# class sharmavishnu:
#     def sample(): # method
#         print("This is sample function")
# sharmavishnu.sample()


# class sharmavishnu:
#     a = "lolo" # class ke andar function --> attribute

#     def sample(): # method
#         print("This is sample function")
# sharmavishnu.sample()
# print(sharmavishnu)


# class Animal:
#     # Attribute
#     name = "Animal"

#     #method
#     def greet (self): # ki jab bhi class ke anadr ke function ko object ji ki help se call karoge toh ek PARAMeter set krna hoga
#         print("this is animal class")


# # Object ka namm same as hota hai as name of the variable
# tau = Animal()  # here tau is object
# tau.greet()
# print(tau.name)



# Question ) create a class which willperform 2 taask
#1) greet the user -"this is class"
#2) adding upto two number


# class baggah:
#     def greet(self):
#         print("hello from baggah class ")

#     def add(self):
#         a = 10
#         b = 10
#         print(a+b)

# obj = baggah()  # class ko variable me store kar rahe hai ishi ko object kahte ha
# obj.greet()
# obj.add()




#.                               DATE ==> 19 MAY,2026 


# class sharmavishnu:
#     def greet(self):
#         print("this is a function")

#     def greet(self):
#         print("this is 2nd function")  # latest create pahle chalega jab same anme se function ho
    
# indrapuri = sharmavishnu()
# indrapuri.greet()



#  ToiPIc ==>. [ constructor] --> Represent by __init__ (Dunder method)
"""constructor sabse pehle execute hone wale function hai doesn't matter inke upper ya neeche koi persent hai """

# class sharmavishnu:
#     def __init__(self):
#         print("this is constructor function")

#     def menu(self):
#         print("panner kulche")
# obj = sharmavishnu()
# obj.menu




# class sharmavishnu:
#     def __init__(self,name,age):
#         self.name = name # Instance atrribute (variable)
#         self.age = age
#         print("this is constructor function")
        
#     def menu(self):
#         print(self.name)
#         print(self.age)
#         print("panner kulche")
# obj = sharmavishnu("amit",21)
# obj.menu()



# MAke a class which will take 2 numbers as input create 
#1) 2 instance atrribute
# 2) create a function which will print gratest among them

# class sample:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def greater(self):
#         if self.a > self.b:
#             print(self.a ,"is greater")
#         else:
#             print(self.b,"is greater")

# obj = sample(10,20)
# obj.greater()




#.                              DATE ==> 20 MAY,2026


# Topic ==> 1) classmethod
         # 2) staticmethod

#1) classmethod

# class Animal:
#     name = "dog" # class attribute  # class attribute ko object se call nhi kar sakte hai

#     @classmethod  
#     def change(cls,new):
#         cls.name = new
#         print(cls.name)

# cheeta = Animal()
# cheeta.change("cat")
# print(Animal.name)


# 2) staticmethod
""" independent of objectt ,mtlb object bane ya na bane ghanta fark nhi padta"""

# class sharmavishnu:

#     @staticmethod  # bina parameter ke chale isliye static method ka use karte hai Ex - self
#     def menu():
#         print("paneer kulche")
#         print("paneer tikka ")
#         print("peneer cheese sandwich")
#         print("cold coffee")

# new_market = sharmavishnu()
# new_market.menu()



#.                        DATE ==> 21 MAY,2026

#        TOPIC    ==> Inheritence

"""1. single inheritence --> one parent class and one child calss
 2. multiple inheritence
 3. multilevel inheritance
 4."""

# single inheritance

# class parent:

#     def __init__(self):
#         print("this is parent class constructor")

#     def greet(self):
#         print("this is parent class")

# class child(parent):
#     def show(self):
#         print("this is chald class")


# obj = child()  # ek object se do function ko call karte hai
# obj.greet()
# obj.show()





# class parent:

#     def __init__(self):
#         print("this is parent class constructor")
        
#     def greet(self):
#         print("this is parent class")

# class child(parent):
#     def __init__(self):  # child class constructor
#         print("this is child class constructor")

#     def show(self):
#         print("this is chald class")


# obj = child()  # ek object se do function ko call karte hai
# obj.greet()
# obj.show()


# factory

# class Factory:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color

#     def show(self):
#         print(f"bag has {self.name} and {self.color} color")

# class Bata(Factory):
#     def __init__(self,name,color,zip,pockets):
#         super().__init__(name,color)







# 2 ) multiple inheritance --> 2 parent ,1 child class

class Father: #parent 1
    def __init__(self):
         print("this is father class constructor")

    def greet_father(self):
        print("this is fater class")

class Mother: #parent 2
        
        def __init__(self):
             print("this is mother class constructor")

        def greet_mother(self):
            print("this is mother class")

class child(Father,Mother): # child
     pass

obj = child()
obj.greet_father()
obj.greet_mother()
      



class Father: #parent 1
    def __init__(self):
         print("this is father class constructor")

    def greet_father(self):
        print("this is fater class")

class Mother: #parent 2
        
        def __init__(self):
             print("this is mother class constructor")

        def greet_mother(self):
            print("this is mother class")

class child(Father,Mother): # child
     def __init__(self):
          Father.__init__(self) # sabse pahle father class ka constructor will be run
          Mother.__init__(self) # After father class mother class constructor will be run
obj = child()
obj.greet_father()
obj.greet_mother()
      