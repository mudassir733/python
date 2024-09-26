class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Car started")
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print(f"Car speed increased to {self.speed} km/h")
        else:
            print("Car must be started before speed can be increased")
    def stop(self):
        if self.started:
            self.speed = 0
            self.started = False
            print("Car stopped")
        else:
            print("Car is already stopped")

# multiple instances of same Class
car = Car()
car1 = Car()

# car1 id
print(id(car1))


car.start()
car.increase_speed(40)