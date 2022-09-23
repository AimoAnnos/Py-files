class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

class ElectricCar(Car): # Sulkuihin (Car) niin perii Car luokan
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(model)

class Battery:
    def __init__(self,model, battery_size=75):
        self.model = model
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size} kWh Bathory(!).")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 250
        else:
            range = 300
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100