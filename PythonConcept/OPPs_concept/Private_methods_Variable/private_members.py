
class A:
    myvar1 = 100               # Public variables
    __myvar2 = 200              # Private Variables

    def m1(self):
        print(" its a public method")

    def __m2(self):
        print(" it is a private method")

    def m3(self):
        # print(self.__myvar2())
        self.__m2()                            # Adjustment for calling the private m & v outside the class
        print("private variable", self.__myvar2)



myobj = A()

# Public variable calling
print(myobj.myvar1)

# Private variable calling
# print(myobj.myvar2)           # AttributeError: 'A' object has no attribute 'myvar2 because of it's a private variable

# Calling public method
myobj.m1()

# Calling private method
# myobj.m2()                    # AttributesError throws while accessing the private method


'''Directly we can't access priavte methods and varibles outside the class,
 but we can call it indirectly as below approach'''

myobj.m3()
