# Global variables  
a, b = 10, 20  

class A:  
    a, b = 30, 40  # Class variables  

class B(A):  
    a, b = 11, 11  # Class variables  

class C(B):  # Class C inherits from Class B  
    a, b = 50, 60  # Class variables  
    def add(self, a, b):  # Local variables  
        print(a + b)  # Local variables: 1 + 2  
        print(self.a + self.b)  # Class variables of Class C: 50 + 60  

        # Access global variables  
        print(globals()['a'] + globals()['b'])  # Global variables: 10 + 20  

        # Access Class A's class variables  
        print(A.a + A.b)  # Accessing class variables directly: 30 + 40

        # Access Class B's class variables  
        print(B.a + B.b)  # Accessing class variables directly: 11 + 11  

# Creating an instance of class C  
objc = C()  

# Calling the add method  
objc.add(1, 2)  