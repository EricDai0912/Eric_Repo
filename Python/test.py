from abc import ABC, abstractclassmethod
import Stack
class Car(ABC):
    step = '2'
    def __init__(self, tire = 0, door = 0):
        self.tire = tire
        self.door = door
    
    @abstractclassmethod
    def forword(self):
        pass

    @abstractclassmethod
    def backword(self):
        pass

    
class Turck(Car):
    step = '3'
 
    def __init__(self, tire=0, door=0, capacity=0):
        super().__init__(tire, door)
        self.capacity = capacity

if __name__ == "__main__":
    # porsche = Car()
    # print(porsche.tire)
    # porsche.tire = 4
    # print(porsche.tire)
    # porsche.forword()

    # toyota = Car(6,6)

    Tesla = Turck(4,4,5)
    Tesla.forword()