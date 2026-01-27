class MyClass:
    def printname(self):
        print(" inside printname method")

    def printemail(self, email, id):
        print("email is ", email)


#  To create a object

# MyClass()                       # Object creation
p1 = MyClass()                    # assigning this variable to object
p1.printname()                    # Calling method by using object
p1.printemail("abc@gmail.com", "101")

#  We can create multiple object for same class

p2 = MyClass()
p2.printname()
p2.printemail("ram@gmail.com", 102)