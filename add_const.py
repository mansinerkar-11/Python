class Addition:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        print("First Number: "+str(self.first))
        print("Second Number: "+str(self.second))
        print("Addition: "+str(self.answer))
    def calculate(self):
        self.answer=self.first + self.second
obj=Addition(1000,2000)
obj.calculate()
obj.display()
    
    
    