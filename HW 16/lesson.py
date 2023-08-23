##Data Abstraction- class Person##
class Person:
    age: int
    _name: str

##Encapsulation- GetName##
    def GetName(self):
        return self._name

##Encapsulation- SetName##    
    def SetName(self, name):
        if name != "":
            self._name = name

    def __init__(self, name: str, age: int = None, occupation: str = None) -> None:
        self._name = name

        self.age = age
        if self.age is None:
            self.age = 18
        
        self.occupation = occupation

##Polymorphism- def __str__##
    def __str__(self) -> str:
        return f"Hello, I'm {self._name}, I'm {self.age} years old."


    def __del__(self):
        print(f"{self._name} says goodbye!")

##Polymorphism- def meet##
    def meet(self, name: str):
        print(f"Hello, nice to meet you, {name}. I'm {self._name}!")

##Data Abstraction-class Worker##
##Inheritance- наследует от class Person##
class Worker(Person):
    occupation: str

    @staticmethod
    def ClockIn(name):
        print(f"{name} has clocked in")
    # ClockIn = staticmethod(ClockIn)

    def __init__(self, name: str, age: int = None, occupation: str = "worker") -> None:
        super(Worker, self).__init__(name, age)
        self.occupation = occupation


    def greet(self):
        return self._name

##Polymorphism- def __str__##   
    def __str__(self) -> str:
        return f"Hello, I'm {self._name}, I'm {self.age} years old. I work as an {self.occupation}."

##Subtype Polymorphism- def Meet##
def Meet(p1, p2):
    print(type(p1), type(p2))
    return str(p1) + " " + str(p2)

if __name__ == "__main__":
    alex = Worker("Alex", 32)
    dima = Person("Dima")
    print(Meet(dima, alex))
    print(Meet(11, True))
##Subtype Polymorphism## 
    Worker.ClockIn("John")