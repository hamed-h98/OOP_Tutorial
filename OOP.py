#!/usr/bin/env python
# coding: utf-8

# ## Object-Oriented Programming (OOP): 
# 
# - Attributes & Objects 
# - Abstract Classes
# - Polymorphism
# - Abstraction 
# - Encapsulation 
# - Inheritance 
# - Method Kinds
# 
# ## Sources: 
# 
# https://www.youtube.com/watch?v=iLRZi0Gu8Go
# 
# https://www.youtube.com/watch?v=Ej_02ICOIgs&t=1054s
# 
# OpenAI
# 

# In[1]:


# General Example: 

class Shape: 
    def __init__(self, area):
        self.area = area
    
    def update_area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side 
        self.update_area()
        self.name = "Square"
    
    def update_area(self):
        self.area = self.side * self.side

class Rectangle(Shape):
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2
        self.update_area()
        self.name = "Rectangle"
    
    def update_area(self):
        self.area = self.side1 * self.side2
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        self.update_area()
        self.name = "Circle"
    
    def update_area(self):
        self.area = self.radius**2 * 3.14

shapes = []
shapes.append(Square(4))
shapes.append(Rectangle(4,5))
shapes.append(Circle(3))

for shape in shapes:
    shape.update_area()
    print(f"Area of {shape.name}:",shape.area)


# ## Attributes & Objects
# 
# Object: A specific instance of a class (e.g., a real dog, a real car).
# 
# Attributes: Variables that belong to an object (e.g., color, age).
# 
# 

# In[1]:


class Dog:
    def __init__(self, name, age):
        self.name = name    # Attribute
        self.age = age      # Attribute

# Create object
dog1 = Dog("Buddy", 3)

print(dog1.name)  # Buddy
print(dog1.age)   # 3


# ### Abstract Classes
# 
# A class that cannot be instantiated.
# 
# It defines methods that child classes must implement.
# 
# 

# In[20]:


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

dog = Dog()
print(dog.sound())  # Woof


# ### Polymorphism
# 
# Same method name behaves differently depending on the class.
# 

# In[21]:


class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

# Polymorphism in action
animals = [Cat(), Dog()]

for animal in animals:
    print(animal.sound())


# ### Abstraction
# 
# Hiding complex details and only showing the essential features.
# 
# In Python, usually done using abstract classes or simple method hiding.
# 

# In[22]:


class Car:
    def start_engine(self):
        print("Engine started")
        
    def drive(self):
        self.start_engine()  # Hidden detail
        print("Car is moving")

my_car = Car()
my_car.drive()


# ### Encapsulation
# 
# Restricting access to internal variables and methods.
# 
# Done by using private attributes (_var or __var).
# 

# In[23]:


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
# print(account.__balance)    # Error! Private attribute


# ### Inheritance
# 
# A class inherits attributes and methods from another class.
# 

# In[24]:


class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.move()  # Inherited
my_dog.bark()  # Own method


# ### Method Kinds
# 
# | Method Type      | Decorator Used      | Purpose                               |
# |------------------|----------------------|---------------------------------------|
# | Instance Method  | (default, no decorator) | Works with object attributes         |
# | Class Method     | @classmethod         | Works with the class itself, not object |
# | Static Method    | @staticmethod        | Utility method, doesn’t access class or object |
# 

# In[25]:


class MathOperations:
    def add(self, a, b):            # Instance method
        return a + b
    
    @classmethod
    def description(cls):           # Class method
        return "This class performs math operations."

    @staticmethod
    def multiply(a, b):             # Static method
        return a * b

math = MathOperations()
print(math.add(2, 3))         # 5
print(MathOperations.description())  # Math operations
print(MathOperations.multiply(4, 5)) # 20


# ### super()
# 
# Used to call methods from the parent class inside a child class.
# 
# Helps reuse code from the parent without repeating.
# 

# In[26]:


class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):
    def move(self):
        super().move()  # Call parent method
        print("Dog walks on four legs")

dog = Dog()
dog.move()


# ### Magic Methods (Dunder Methods)
# 
# Special methods with double underscores (__) to control built-in behavior.
# 
# > Examples: `__init__, __str__, __len__, __eq__, __add__,` etc.
# 

# In[27]:


class Book:
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return f"Book: {self.title}"

book = Book("Python Programming")
print(book)  # Automatically calls __str__()


# ### Multiple Inheritance
# 
# A class can inherit from more than one parent class.
# 
# 

# In[28]:


class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  # Gardening (because Father is listed first)


# ### Composition ("Has-A" Relationship)
# 
# Instead of "is-a", it’s "has-a".
# 
# Use other classes inside a class.
# 
# 

# In[29]:


class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        self.engine.start()

my_car = Car()
my_car.start()


# ### Private/Protected Members
# 
# _var: Protected, hint: "don't touch outside the class".
# 
# __var: Private, harder to access from outside.
# 
# 

# In[30]:


class Person:
    def __init__(self):
        self._protected = "Protected"
        self.__private = "Private"

p = Person()
print(p._protected)   # Accessible (but should be careful)
# print(p.__private)  # Error


# ### Property Decorators (@property)
# 
# To control access to attributes like a function but behave like a variable.
# 
# 

# In[31]:


class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")

p = Product(100)
print(p.price)  # 100
p.price = 200
print(p.price)  # 200


# ### Operator Overloading
# 
# Operator overloading lets you customize how operators like +, -, *, ==, etc., behave for your own classes.
# 
# Normally, + adds two numbers.
# 
# But you can make + add two vectors, combine two strings in a special way, merge two objects, etc.
# 
# It’s done by defining magic methods like `__add__(), __eq__(), __lt__()`, etc.
# 

# In[32]:


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2   # Calls __add__()
print(v3)      # Output: (4, 6)


# usecases: 
# 
# - Working with mathematical objects: Vectors, Matrices, Complex Numbers
# 
# - Custom string or data merging: Custom text classes, filename generators
# 
# - Custom comparison: Sorting custom objects based on properties
# 
# ### Metaclasses
# 
# Metaclasses are classes that create classes.
# 
# Normally, in Python: classes create objects.
# 
# Metaclasses create classes themselves.
# 
# It gives you control over class creation: you can modify the class, add methods automatically, validate attributes, etc.
# 

# In[33]:


class MyMeta(type): # MyMeta is a class that creates classes.
    def __new__(cls, name, bases, dct):  
        # __new__() is called when a new class is being created, not an object yet.
        # cls: the metaclass (MyMeta itself)
        # name: the name of the class being created ('MyClass')
        # bases: the parent classes (() because MyClass has no parent)
        # dct: dictionary of attributes/methods of the class being created
        dct['say_hello'] = lambda self: print("Hello!")
        # "Hey Python, when you create this class, also add a method called say_hello that prints 'Hello'."
        
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta): 
    # MyClass is built using MyMeta, not normal type.
    pass

obj = MyClass()
obj.say_hello()  # Output: Hello!


# A `lambda` is a small anonymous function.
# 
# It has no name (unlike def my_function():).
# 
# It’s mainly used for quick, simple functions you don’t want to formally define.
# 
# `lambda arguments: expression`
# 

# In[ ]:


add = lambda x, y: x + y
print(add(3, 5))  

# This is equivalent to:

def add(x, y):
    return x + y


# ### Another example for lambda: 

# In[35]:


square = lambda x: x**2

print(square(4))  # Output: 16


# ### Another example for metaclass

# In[36]:


# Define a Metaclass
class RunEnforcerMeta(type):
    def __new__(cls, name, bases, dct):
        if 'run' not in dct:
            raise TypeError(f"Class '{name}' must implement a 'run()' method")
        return super().__new__(cls, name, bases, dct)

# Good Class (Correct)
class Task(metaclass=RunEnforcerMeta):
    def run(self):
        print("Running the task...")

# Bad Class (Missing run())
# This will raise an error immediately
# class BadTask(metaclass=RunEnforcerMeta):
#     def start(self):
#         print("Starting...")

# Example usage
task = Task()
task.run()


# Metaclasses are NOT for everyday use.
# Use them when you are building libraries, frameworks, or enforcing rules across many classes automatically.

# # Practice from Youtube: 
# 
# https://www.youtube.com/watch?v=iLRZi0Gu8Go

# In[11]:


# we wanna create the data type of our own to reuse it in the future easily 

class Item: 
    # functions in the classes are called methods 
    def calculate_total_price(self,x,y): 
        return x*y


item1 = Item()
# creating attributes: 
item1.name = "Phone"
item1.price = 100
item1.quantity = 5 
# each of the attributes are assigned to one instance of the class
item1.calculate_total_price(item1.price,item1.quantity)


print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

item2 = Item() 
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3 
item2.calculate_total_price(item2.price,item1.quantity)


# In[12]:


class Item: 
    def __init__(self):
        print("It Is Created")

    def calculate_total_price(self,x,y): 
        return x*y


item1 = Item()
# creating attributes: 
item1.name = "Phone"
item1.price = 100
item1.quantity = 5 
item1.calculate_total_price(item1.price,item1.quantity)

item2 = Item() 
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3 
item2.calculate_total_price(item2.price,item1.quantity)


# In[13]:


class Item: 
    def __init__(self,name):
        print(f"An instance created: {name}")

    def calculate_total_price(self,x,y): 
        return x*y


item1 = Item("Phone")
# creating attributes: 
item1.name = "Phone"
item1.price = 100
item1.quantity = 5 
item1.calculate_total_price(item1.price,item1.quantity)

item2 = Item("Laptop") 
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3 
item2.calculate_total_price(item2.price,item1.quantity)


# In[14]:


name = "Hamed"  # object
age = 26 # object
# print(type(name)) # it's class str (string object) 
# print(type(age)) # this is class int (integer object)
# # so objects are made from classes 
# # class describes that what the object should be look like 
# print(name.upper()) # manipulating the object and making it all uppecase letters 

# string object is built from string class and we have some method and functions that can be applied to the objects of class str 



# In[15]:


class Dog: 
    def __init__(self,name,breed,owner):   # defining some data fields for the class 
        # self referes to the instance of specific object of the class itself 
        self.name = name
        self.breed = breed 
        self.owner = owner

    # here we can define attributes, methods, and functions
    def bark(self):
        print("Whoof Whoof")
    # self is the reference to the object that we are working with

class Owner: 
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


owner1 = Owner("Hamed","1234 Main St","123-456-7890")
dog1 = Dog("Tommy","German Shepherd",owner1)
# dog1.bark() # accessing the method of the class Dog 
# print(dog1.name)
# print(dog1.breed)
print(dog1.owner.name)


owner2 = Owner("John","1234 Main St","123-456-7890")
dog2 = Dog("freya","Golden Retriever",owner2)
# dog2.bark()
# print(dog2.name)
# print(dog2.breed)
print(dog2.owner.name)

# when we instantiate the dog object, we pass in the variables (name, breed, owner)
# then the self should have the a name attribute assigned to the name we pass in 

# when we create an object from the class, we are instantiating the class and the object is an instance of the class




# In[16]:


class Person: 
    def __init__(self,name,age):
        self.name = name # attributes (stores name of the object)
        self.age = age

    def greet(self): # methods 
        print(f"Hello my name is {self.name} and I am {self.age} years old")

person1 = Person("Hamed","26") # specific instance of a class that gives the object access to its own attributes 
person1.greet() # person1 has its own greet method (specific for person1)

person2 = Person("Bob","42")
person2.greet() # person2 has its own greet method



# In[17]:


class User: 
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def say_hi_to_user(self,user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

user1 = User("Hamed","hamed98.gmail.com","1234")
user2 = User("Batman","bat@outlook.com","abc")

user1.say_hi_to_user(user2)



# In[18]:


class User: 
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def say_hi_to_user(self,user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

user1 = User("Hamed","hamed98.gmail.com","1234")

# we can assign a new value to the email (modify the attribute)
user1.email = "danny@gmail.com"


# In[19]:


# Since the attribute can be changed like this easily, we need to make the attributes private 
# method1: 
# Accessing and modifying data (traditional way, popular in Java and C#), making the attribute protected: 
class User: 
    def __init__(self,username, email, password):
        self.username = username
        self._email = email # protected attribute (adding underscore) 
        self.__password = password 
        # if we add double underscore, it's a private attribute and python won't show it if we try to access it outside the class
        # this means that we shouldn't read the attribute outside the class
    
    # def get_email(self): 
    #     return self._email
    def clean_email(self):
        return self._email.lower().strip()

user1 = User("Hamed","HameD98@gmail.com","1234")

# print(user1._email) # we can still access the attribute in Python 
# # it's just signals to the developers that the email is protected since we used '_'.
print(user1._email)
print(user1.clean_email())

print(user1.__password)




# In[ ]:


from datetime import datetime
class User: 
    def __init__(self,username, email, password):
        self.username = username
        self.email = email 
        self.password = password 

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self.email
    
    def set_email(self,new_email):
        if "@" in new_email:
            self.email = new_email

user1 = User("Hamed","HameD98@gmail.com","1234")

user1.set_email("danny@outlook.com")

print(user1.get_email())


# In[ ]:


# Accessing and Modifying Data: 
# Properties 
class User: 
    def __init__(self,username, email, password):
        self.username = username
        self._email = email 
        self.password = password 
    # a controlled way for getting and seting the data  
    # creating as get property
    @property 
    def email(self):
        print(f"Email accessed")
        return self._email
    
    # set property to update email
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email = new_email

user1 = User("Hamed","HameD98@gmail.com","1234")
print(user1.email)


# In[ ]:


# static attributes (shared among all instances of the class)
# A static attribute (sometimes called a class attribte) is an attribute that belongs to the class itself, 
# not to any specific instance of the class 
# static atribute can be accessed through the class directly 

class User: 

    user_count = 0 # initially zero 

    def __init__(self,username, email):
        self.username = username
        self.email = email 
        User.user_count += 1
    
    def display_user(self):
        print(f"Username:{self.username}, Email: {self.email}")


user1 = User("Hamed","HameD98@gmail.com")
user2 = User("sally123","sally@gmail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)

user1.display_user()


# To define a static method, we use the @staticmethod decorator


# In[ ]:


# Static vs. Instance Method Example 

class BankAccount: 
    MIN_BALANCE = 100 

    def __init__(self,owner,balance = 0):
        self.owner = owner 
        self._balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount 
            print(f"{self.owner}'s new balance: ${self._balance}")
        else: 
            print("Invalid amount")

    @staticmethod 
    def is_valid_interest_rate(rate):
        return 0 <= rate <=5

account = BankAccount("Hamed",1000)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))



# In[ ]:


class BankAccount:
    def __init(self,owner,balance = 0):
        self.owner = owner
        self._balance = balance 
    
    def deposit(self,amount):
        if self._is_valid_amount(amount): 
            self._balance += amount 
            self.__log_transaction("deposit",amount)
            print(f"{self.owner}'s new balance: ${self._balance}")
        else: 
            print("Invalid amount")
    
    def _is_valid_amount(self,amount):
        return amount > 0

    # creating private methods
    def __log_transaction(self,transaction_type,amount):
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")

    @staticmethod 
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    

account = BankAccount("Hamed",1000)
account.deposit(200)
print(BankAccount.is_valid_interest_rate(3))

account.__log_transaction("withdraw",200) # this will give an error since the method is private and can't be accessed outside the class






# In[ ]:


# Encapsulation:
# It involves boundling the data (attributes) and the methods that operate on the data into a single unit (class)
# Hiding the data from the outside world and only exposing the necessary data and methods

#Example with no encapsulation: 
class BankAccount: 
    def __init__(self,balance):
        self.balance = balance 

account = BankAccount(0.0)
account.balance = -1
# print(account.balance)
# we'll see that it prints -1, which is not a valid balance for a bank account


# Example with encapsulation:
class BankAccount: 
    def __init__(self):
        self._balance = 0.0 # making the balance a protected attribute, so we can't access it directly outside of the class 
        # We are encapsulating the balance attribute insdie the class
    
    @property
    # create a get a property for balance
    def balance(self):
        return self._balance 
    
    # deposite method: 
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposite amount must be positive")
        self._balance += amount 
    
    # withdraw method:
    def withdraw(self,amount):
        if amount <= 0: 
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount()
print(account.balance)
# account.balance = -1 # we'll get error 
account.deposit(100)
print(account.balance)
account.withdraw(2)
print(account.balance)
# print(account.withdraw(200)) # we'll get the error "insufficient funds"


        


# In[ ]:


# Abstraction 
# Reduce complexity by hiding unnecessary details 

class EmailService:
    def _connect(slef):
        print("Connecting to the email server")

    def _authenticate(self):
        print("Authenticating")
    
    # sending email does not need to be hidden from the user so we don't need to use '_' for this method
    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()
    
    def _disconnect(self):
        print("Disconnecting from email server")

# All these details are abstracted away from the user 
email = EmailService()
email.send_email() # we only need to call the send_email method and the rest of the details are hidden from the user


# If we don't use abstraction (meaning that not using '_' for some tasks), we have to do all these steps manually:
class EmailService:
    def connect(slef):
        print("Connecting to the email server")

    def authenticate(self):
        print("Authenticating")

    def send_email(self):
        self.connect()
        self.authenticate()
        print("Sending email...")
        self.disconnect()
    
    def disconnect(self):
        print("Disconnecting from email server")

email = EmailService()
email.connect()
email.authenticate()
email.send_email() 
email.disconnect()

 
# encapsulation focuses on boundling data or attributes and methods that operate on the data into a single unit (class) 
#(restricting access to the data)

# abstraction focuses on hiding unnecessary details from the user and only showing the necessary details to the user
# (simplifying usage of the class)




# In[ ]:


# Inheritance 
# It envolves creating new classes (subclasses, or derived classes) based on existing classes (superclasses, or base classes)

# create a base class
class Vehicle: 
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Engine started")
    
    def stop(self):
        print("Engine stopped")
    
# creating subclasses
class Car(Vehicle): # the car class should inherit 
    def __init__(self,brand,model,year,number_of_doors,number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle): # inherit Vehicle
    def __init__(self,brand,model,year,number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_wheels = number_of_wheels

car = Car("Toyota","Corolla",2020,4,4)
bike = Bike("Honda","CBR",2021,2)

print(car.__dict__)

print(bike.__dict__)




# In[ ]:


# Polymorphism
# The word means having multiple forms
# It allows objects of different classes to be treated as objects of a common superclass

# Example that has no polymorphism: 
class Car: 
    def __init__(self,brand,model,year,number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year 
        self.number_of_doors = number_of_doors
    
    def start_car(self):
        print("Car is starting")

    def stop_car(self):
        print("Car is stopping")

class Motorcycle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year 
    
    def start_bike(self):
        print("Motorcycle is starting")
    
    def stop_bike(self):
        print("Motorcycle is stopping")

# creating list of vehicles to inspect:
Vehicles = [
    Car("Toyota","Corolla",2020,4),
    Motorcycle("Honda","CBR",2021)
]

# Loop through the list of vehicles and inspect them 
# note that here we don't have a common class to work with and we have separated classes 
for vehicle in Vehicles: 
    # vehicle.start() # there is no common method in the classes
    if isinstance(vehicle,Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} {type(vehicle).__name__}")
        vehicle.start_car()
        vehicle.stop_car()
    elif isinstance(vehicle,Motorcycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} {type(vehicle).__name__}")
        vehicle.start_bike()
        vehicle.stop_bike()
    else: 
        raise Exception("Unknown vehicle type")

# The above code is not polymorphic since we have to check the type of the vehicle 
# and call the appropriate method based on the type of the vehicle

# if we add more vehicle type, we need to modify the code and add more if conditions to check the type of the vehicle
    





# In[ ]:


# Solving the issue with polymorphism:
# creating a base class for all vehicles: 
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("Engine started")
    
    def stop(self):
        print("Engine stopped")
    

class Car(Vehicle): 
    def __init__(self,brand,model,year,number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors
    
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Motorcycle(Vehicle):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)
    
    def start(self):
        print("Motorcycle is starting")
    
    def stop(self):
        print("Motorcycle is stopping")


# creating list of vehicles to inspect:
Vehicles = [
    Car("Toyota","Corolla",2020,4),
    Motorcycle("Honda","CBR",2021)
]

Vehicles: list[Vehicle] = [
    Car("Toyota","Corolla",2020,4),
    Motorcycle("Honda","CBR",2021)
]

for vehicle in Vehicles: 
    if isinstance(vehicle,Vehicle): 
        print(f"Inspecting {vehicle.brand} {vehicle.model} {type(vehicle).__name__}")
        vehicle.start()
        vehicle.stop()
    else: 
        raise Exception("Unknown vehicle type")





# In[ ]:


# we can also do this: 

# adding another type of vehicle: 
class Plane(Vehicle):
    def __init__(self,brand,model,year,number_of_engines):
        super().__init__(brand,model,year)
        self.number_of_engines = number_of_engines
    
    def start(self):
        print("Plane is starting")
    
    def stop(self):
        print("Plane is stopping")


Vehicles: list[Vehicle] = [
    Car("Toyota","Corolla",2020,4),
    Motorcycle("Honda","CBR",2021),
    Plane("Boeing","747",2021,4)
]

for vehicle in Vehicles: 
    print(f"Inspecting {vehicle.brand} {vehicle.model} {type(vehicle).__name__}")
    vehicle.start()
    vehicle.stop()
    



# ## Vector and Matrix Operations Library
# 

# In[54]:


from abc import ABC, abstractmethod

# ===== Abstract Base Class =====
class MathEntity(ABC):
    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def scale(self, scalar):
        pass

# ===== Vector Class =====
class Vector(MathEntity):
    def __init__(self, x, y, z=0):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y, self._z + other._z)

    def add(self, other):
        return self + other  # reuses __add__

    def scale(self, scalar):
        return Vector(self._x * scalar, self._y * scalar, self._z * scalar)  # FIXED: scaling z also

    def __str__(self):
        return f"Vector({self._x}, {self._y}, {self._z})"

# ===== Matrix Class =====
class Matrix(MathEntity):
    def __init__(self, rows):
        self._rows = rows

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only add two Matrices")
        new_rows = []
        for r1, r2 in zip(self._rows, other._rows):
            new_row = [a + b for a, b in zip(r1, r2)]
            new_rows.append(new_row)
        return Matrix(new_rows)

    def add(self, other):
        return self + other

    def scale(self, scalar):
        new_rows = [[elem * scalar for elem in row] for row in self._rows]
        return Matrix(new_rows)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only multiply two Matrices")
        result = []
        for i in range(len(self._rows)):
            row = []
            for j in range(len(other._rows[0])):
                val = sum(self._rows[i][k] * other._rows[k][j] for k in range(len(other._rows)))
                row.append(val)
            result.append(row)
        return Matrix(result)

    def __str__(self):
        return f"Matrix({self._rows})"

# ===== Utility Functions (Composition) =====
class MathUtils:
    @staticmethod
    def magnitude(vector):
        return (vector._x**2 + vector._y**2 + vector._z**2)**0.5  # Added z for 3D magnitude

    @staticmethod
    def determinant(matrix):
        if len(matrix._rows) != 2 or len(matrix._rows[0]) != 2:
            raise ValueError("Only 2x2 matrices supported for determinant.")
        a, b = matrix._rows[0]
        c, d = matrix._rows[1]
        return a*d - b*c


# ===== Main Program =====
if __name__ == "__main__":
    v1 = Vector(2, 3, 1)
    v2 = Vector(4, 1, 1)

    print(v1)  # Vector(2, 3)
    print(v2)  # Vector(4, 1)
    print("Vector Add:", v1.add(v2))
    print("Vector Scale (2x):", v1.scale(2))
    print("Vector Magnitude:", MathUtils.magnitude(v1))

    m1 = Matrix([[1,2], [3,4]])
    m2 = Matrix([[5,6], [7,8]])

    print(m1)  # Matrix([[1, 2], [3, 4]])
    print(m2)  # Matrix([[5, 6], [7, 8]])
    print("Matrix Add:", m1.add(m2))
    print("Matrix Scale (3x):", m1.scale(3))
    print("Matrix Determinant:", MathUtils.determinant(m1))


# In[63]:


get_ipython().run_cell_magic('writefile', 'math_entities.py', '\nfrom abc import ABC, abstractmethod\n\nclass MathEntity(ABC):\n    @abstractmethod\n    def add(self, other):\n        pass\n\n    @abstractmethod\n    def scale(self, scalar):\n        pass\n\nclass Vector(MathEntity):\n    def __init__(self, x, y, z=0):\n        self._x = x\n        self._y = y\n        self._z = z\n\n    def add(self, other):\n        return Vector(self._x + other._x, self._y + other._y, self._z + other._z)\n\n    def scale(self, scalar):\n        return Vector(self._x * scalar, self._y * scalar, self._z * scalar)\n\n    def __add__(self, other):\n        return self.add(other)\n\n    def __str__(self):\n        return f"Vector({self._x}, {self._y}, {self._z})"\n\n# ===== Matrix Class =====\nclass Matrix(MathEntity):\n    def __init__(self, rows):\n        self._rows = rows\n\n    def __add__(self, other):\n        if not isinstance(other, Matrix):\n            raise ValueError("Can only add two Matrices")\n        new_rows = []\n        for r1, r2 in zip(self._rows, other._rows):\n            new_row = [a + b for a, b in zip(r1, r2)]\n            new_rows.append(new_row)\n        return Matrix(new_rows)\n\n    def add(self, other):\n        return self + other\n\n    def scale(self, scalar):\n        new_rows = [[elem * scalar for elem in row] for row in self._rows]\n        return Matrix(new_rows)\n\n    def __mul__(self, other):\n        if not isinstance(other, Matrix):\n            raise ValueError("Can only multiply two Matrices")\n        result = []\n        for i in range(len(self._rows)):\n            row = []\n            for j in range(len(other._rows[0])):\n                val = sum(self._rows[i][k] * other._rows[k][j] for k in range(len(other._rows)))\n                row.append(val)\n            result.append(row)\n        return Matrix(result)\n\n    def __str__(self):\n        return f"Matrix({self._rows})"\n\n# ===== Utility Functions (Composition) =====\nclass MathUtils:\n    @staticmethod\n    def magnitude(vector):\n        return (vector._x**2 + vector._y**2 + vector._z**2)**0.5  # Added z for 3D magnitude\n\n    @staticmethod\n    def determinant(matrix):\n        if len(matrix._rows) != 2 or len(matrix._rows[0]) != 2:\n            raise ValueError("Only 2x2 matrices supported for determinant.")\n        a, b = matrix._rows[0]\n        c, d = matrix._rows[1]\n        return a*d - b*c\n\n# ===== Main Program =====\nif __name__ == "__main__":\n    v1 = Vector(2, 3, 1)\n    v2 = Vector(4, 1, 1)\n\n    print(v1)  # Vector(2, 3)\n    print(v2)  # Vector(4, 1)\n    print("Vector Add:", v1.add(v2))\n    print("Vector Scale (2x):", v1.scale(2))\n    print("Vector Magnitude:", MathUtils.magnitude(v1))\n\n    m1 = Matrix([[1,2], [3,4]])\n    m2 = Matrix([[5,6], [7,8]])\n\n    print(m1)  # Matrix([[1, 2], [3, 4]])\n    print(m2)  # Matrix([[5, 6], [7, 8]])\n    print("Matrix Add:", m1.add(m2))\n    print("Matrix Scale (3x):", m1.scale(3))\n    print("Matrix Determinant:", MathUtils.determinant(m1))\n')


# In[66]:


import unittest
import importlib
import math_entities
importlib.reload(math_entities)  # Force reloading the updated file!
from math_entities import Vector, Matrix

# ===== Unit Tests =====
class TestVector(unittest.TestCase):
    def test_addition(self):
        v1 = Vector(1, 2, 1)
        v2 = Vector(3, 4, 1)
        v3 = v1 + v2
        self.assertEqual((v3._x, v3._y, v3._z), (4, 6, 2))  # fixed: include z also!

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



# ### Vector and Matrix Operations Library
# 
# A Python library implementing core vector and matrix operations using Object-Oriented Programming (OOP) principles.
# Supports 2D/3D vectors, matrix arithmetic, operator overloading, custom exceptions, and utility functions for common math tasks.
# 
# 
# - Vectors: Addition, scaling, magnitude, 2D/3D support
# 
# - Matrices: Addition, scalar multiplication, matrix multiplication, determinant
# 
# - Operator Overloading: Natural syntax for addition (+), multiplication (*)
# 
# - Encapsulation: Private and protected attributes
# 
# - Inheritance and Abstraction: Abstract base classes (MathEntity)
# 
# - Composition: Utility classes for math operations
# 
# - Containerization: Docker-ready structure
# 
# - Testing: Unit tests for all major components
# 
# - CI/CD Ready: GitHub Actions support for automatic testing (optional)
# 
# 
# 
# ```
# /vector_matrix_library/
# ├── math_entities.py  (Vector, Matrix, MathUtils)
# ├── custom_exceptions.py
# ├── tests/
# │    └── test_math_entities.py
# ├── README.md
# ```
# 
# ### Installation: 
# 
# ```bash
# git clone https://github.com/yourusername/vector-matrix-library.git
# cd vector-matrix-library
# pip install .
# ```
# 
# 
# ### Running Tests: 
# 
# `python -m unittest discover tests/`
# 
# ### Project Structutre: 
# 
# ```
# vector-matrix-library/
# ├── math_entities.py
# ├── custom_exceptions.py
# ├── tests/
# │    └── test_math_entities.py
# ├── Dockerfile  (optional if you want)
# ├── README.md
# └── setup.py   (optional if you package it)
# 
# ```
# 
# ### Create This Directory and File
# 
# Inside your GitHub repo, create:
# 
# ```
# .vector-matrix-library/
# ├── .github/
# │    └── workflows/
# │         └── python-app.yml
# ```
# 
# ## Full python-app.yml File Content
# 
# ```yaml
# name: Python application
# 
# on:
#   push:
#     branches: [ "main" ]
#   pull_request:
#     branches: [ "main" ]
# 
# jobs:
#   build:
# 
#     runs-on: ubuntu-latest
# 
#     steps:
#     - name: Checkout repository
#       uses: actions/checkout@v4
# 
#     - name: Set up Python
#       uses: actions/setup-python@v5
#       with:
#         python-version: '3.12'
# 
#     - name: Install dependencies
#       run: |
#         python -m pip install --upgrade pip
#         pip install -r requirements.txt || true  # Ignore if no requirements.txt
# 
#     - name: Run tests
#       run: |
#         python -m unittest discover tests/
# 
# ```
# 
# In your README.md, you can add at the top:
# 
# `![Python application](https://github.com/yourusername/vector-matrix-library/actions/workflows/python-app.yml/badge.svg)`
# 
# ---
# 

# ## How to Create and Publish a Simple PyPI Package for Your Math Library
# 
# 
# ### 1. Prepare Project Structure
# 
# First, organize your project like this:
# 
# ```
# vector-matrix-library/
# ├── math_entities/
# │    ├── __init__.py
# │    ├── vector.py
# │    ├── matrix.py
# │    ├── math_utils.py
# │    ├── custom_exceptions.py
# ├── tests/
# │    └── test_math_entities.py
# ├── setup.py
# ├── README.md
# ├── LICENSE
# ├── .gitignore
# ├── requirements.txt (optional)
# ```
# 
# Make sure `math_entities/` has an `__init__.py` (even if empty).
# 
# ---
# 
# ### 2. Create `setup.py`
# 
# Inside your root folder (`vector-matrix-library/`), create a file called `setup.py`:
# 
# ```python
# from setuptools import setup, find_packages
# 
# setup(
#     name='math-entities',  # Package name (must be unique on PyPI)
#     version='0.1.0',
#     description='Vector and Matrix operations library using OOP principles',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     author='Hamed Hosseinnejadazad',
#     author_email='your-email@example.com',
#     url='https://github.com/yourusername/vector-matrix-library',
#     packages=find_packages(),
#     install_requires=[],
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#         "Intended Audience :: Developers",
#         "Topic :: Scientific/Engineering :: Mathematics"
#     ],
#     python_requires='>=3.7',
# )
# ```
# 
# Update your `author_email` and `url` correctly.
# 
# ---
# 
# ### 3. Create `LICENSE`
# 
# Example (MIT License):
# 
# ```
# MIT License
# 
# Copyright (c) 2025 Hamed Hosseinnejadazad
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy...
# ```
# 
# Save it as `LICENSE`.
# 
# 
# ---
# ### 4. Create `README.md`
# 
# You can use this template:
# 
# ```markdown
# ## Math Entities
# 
# A Python library for performing basic Vector and Matrix operations using OOP principles.
# 
# ### Features
# - 2D and 3D Vectors
# - Matrix addition, scaling, multiplication
# - Operator overloading
# - Encapsulation, Inheritance
# - Unit tests included
# 
# ### Installation
# 
# ```bash
# pip install math-entities
# ```
# 
# ###  Usage
# 
# ```python
# from math_entities.vector import Vector
# 
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print(v1 + v2)
# ```
# 
# ### License
# 
# MIT License
# 
# 
# Keep README clean and simple for users.
# 
# ---
# 
# ### 5. Install Packaging Tools
# 
# Install these once:
# 
# ```bash
# pip install setuptools wheel twine
# ```
# 
# These packages help you build and upload to PyPI.
# 
# ---
# 
# ### 6. Build Your Package
# 
# From inside your project folder:
# 
# ```bash
# python setup.py sdist bdist_wheel
# ```
# 
# It creates a `dist/` folder with `.tar.gz` and `.whl` files.
# 
# ---
# 
# ### 7. Upload to PyPI
# 
# First, create an account at:  
# [https://pypi.org/account/register/](https://pypi.org/account/register/)
# 
# Then upload your package:
# 
# ```bash
# twine upload dist/*
# ```
# 
# Enter your PyPI username and password when prompted.
# 
# ---
# 
# ### 8. Your Package is Live!
# 
# Users can now install your package directly:
# 
# ```bash
# pip install math-entities
# ```
# 
# ---
# 
# ### Notes
# 
# - **Versioning**: Every time you upload a new version, bump the version number in `setup.py` (e.g., `0.1.1`, `0.2.0`).
# - **PyPI Name**: Must be globally unique. If `math-entities` is taken, try something like `math-entities-hamed`.
# - **Test Upload First**: You can first try uploading to [TestPyPI](https://test.pypi.org/) using:
# 
# ```bash
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# ```
# 
# No risk if you make mistakes.
# 
# ---
# 
# ## Full Example Terminal Workflow
# 
# ```bash
# cd vector-matrix-library
# 
# # Install tools (only first time)
# pip install setuptools wheel twine
# 
# # Build package
# python setup.py sdist bdist_wheel
# 
# # Upload to PyPI
# twine upload dist/*
# ```
# 

# 
