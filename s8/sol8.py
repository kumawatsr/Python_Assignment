"""Method Overloading:

Method overloading is a concept in object-oriented programming where multiple methods with the same name but different parameters are defined within a class. The choice of which method to execute is based on the number of parameters, their types, or their order. 
"""
#Example of Method Overloading in Python:

class MathOperations:
    def add(self, x, y):
        return x + y
    
    def add(self, x, y, z):
        return x + y + z

# Creating an instance of MathOperations
math = MathOperations()
print(math.add(2, 3))           # Output: Error - add() takes 3 positional arguments but 4 were given
print(math.add(2, 3, 4))        # Output: 9

'''In this example, we define two `add` methods in the `MathOperations` class with different numbers of parameters. However, when we try to call the `add` method with only two arguments, Python throws an error because it does not support explicit method overloading. The second `add` method can only be called with three arguments.

Method Overriding:

Method overriding is a concept in object-oriented programming where a derived class provides a different implementation of a method that is already defined in its base class. The derived class overrides the behavior of the method inherited from the base class to provide its own implementation.

To override a method in Python, both the base and derived classes should have a method with the same name. This allows the derived class to replace or modify the functionality of the method inherited from the base class.

Example of Method Overriding in Python:
'''

class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

# Creating instances of Animal and Dog classes
animal = Animal()
dog = Dog()

animal.sound()      # Output: Animal makes a sound.
dog.sound()         # Output: Dog barks.

#Note: Method overriding is achieved through inheritance, where a derived class inherits methods from its base class and can override them to customize the behavior.
