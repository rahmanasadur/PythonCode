class DemoClass:
    a = 10
    def __init__(self):
        print("wel come to python world")

    def product(self):
        self.c = self.a*self.a
        print(self.c)
    
    def add(self,a,b):
        print(a+b)

    


obj = DemoClass()
obj.product()
obj.add(20,20)