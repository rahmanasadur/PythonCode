class A:
    def displayA(self):
        print("Welcome to python world A")

class B:
    def displayB(self):
        print("Welcome to python world B")


class C(A,B):
    def displayC(self):
        print("Welcome to python world C")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()

