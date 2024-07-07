class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!