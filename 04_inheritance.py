class Vechicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    def start(self):
        self.started = True
        print("Vehicle started")
    def stop(self):
        self.speed = 0
        self.started = False
        print("Vehicle stopped")
    def increas_speed(self, delta):
        if self.started:
            self.speed += delta
            print(f"Vehicle speed increased by {delta}, current speed: {self.speed}")
        else:
            print("Vehicle is not started, cannot increase speed")


# redifne our class

class Car(Vechicle):
    def __init__(self, started = False, speed = 0, fuel_level = 0):
        super().__init__(started, speed)
        self.fuel_level = fuel_level
    def drive(self, distance):
        if self.started and self.fuel_level > 0:
            if distance <= self.fuel_level:
                self.fuel_level -= distance
                print(f"Vehicle drove {distance} km, fuel remaining: {self.fuel_level}")
            else:
                print(f"Vehicle cannot drive {distance} km, fuel is low")
        else:
            print("Vehicle is not started or has no fuel, cannot drive")

# create instances
car = Car(speed=70, fuel_level=100)
car.start()
car.drive(40)
car.increas_speed(30)
car.stop()