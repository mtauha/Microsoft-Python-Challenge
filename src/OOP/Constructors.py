class Elevator:
#* Always use 'self' when initializing data members of Class in constructors

    def __init__(self,startingfloor):
        self.make = "The Elevator Comapny"
        self.floor = startingfloor

elevator = Elevator(0)
print(elevator.make)
print(elevator.floor)