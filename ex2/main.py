import numpy as np

class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized!!")

    def hello(self):
        print("Hello" + self.name + "+")

    def goodbye(self):
        print("Goodbye" + self.name + "!!")

m = Man("David")
m.hello()
m.goodbye()
A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A*B)

