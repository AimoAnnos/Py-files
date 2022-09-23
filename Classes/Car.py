class Car:
    def __init__(self, make, model, year, isElectric = False):
        self.make = make # jos käytetään luokan metodeissa, laitetaan self.xxx, isElectric vain parametrina
        self.model = model
        self.year = year
        
        if isElectric == True or self.make == "Tesla":
            if self.make == "Tesla":
                eCar = ElectricCar(self.make,self.model,self.year) # eCar -olio ei tarvii True koska make == "Tesla"   
            else:
                eCar = ElectricCar(self.make,self.model,self.year,False)
        else:
            print(f"{self.make}{self.model}{self.year} is a normal car.")

class ElectricCar:
    def __init__(self, make, model, year, isTesla = True):
        self.make = make
        self.model = model
        self.year = year

        if isTesla:
            self.get_TeslaInfo(True)
        else:
            self.get_TeslaInfo(False)

    def get_TeslaInfo(self,isTesla):
        if isTesla:
            str = "is indeed a Tesla"
        else:
            str = "is an electric car, but not Tesla"
        print(f"{self.make}{self.model}{self.year} is a normal car.")

myCar = Car("Tesla","Model S", 2019)
myCar2 = Car("Electra","Type X", 2000,True)
myCar3 = Car("Ford","Focus",2000)