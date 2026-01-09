class Person:
 def __init__(self,name,age):
   self.name=name
   self.age=age


 def greet(self):
   print(f"Hello, I'm {self.name} and I'm currently {self.age} years old.")


person1 = Person("Karthi",18)
person1.greet()
