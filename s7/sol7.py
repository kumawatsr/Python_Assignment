"""The __init__ method is a special method in Python used to initialize objects of a class. It is automatically called when an instance of the class is created and is responsible for setting the initial state of the object. By defining __init__, you can assign values to the object's attributes and perform any necessary setup.

On the other hand, the __main__ block is not a special method but rather a block of code that is executed when the Python script/module is run directly as the main program. It serves as the entry point of the script and is useful for including test code or script-specific statements that should only run when the script is executed independently.

In summary, __init__ is used within a class to initialize object attributes, while the __main__ block is used in scripts/modules to define the entry point and execute script-specific code when the script is run directly.
"""

# Example 

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

if __name__ == "__main__":
    person = Person("Ram")
    person.greet()

