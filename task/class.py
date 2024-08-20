class MyClass:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
    
    def method1(self):
        return self.name1
    
    def method2(self, new_value):
        self.name2 = new_value


my_instance = MyClass("hi jerin", "hi nanbu")


print(my_instance.name1) 

print(my_instance.method1())  
my_instance.method2("hi anbu")
print(my_instance.name2)  
