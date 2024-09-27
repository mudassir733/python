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






# Another example of classes
class Fruit:
    color = "red"
    weight = 0.6
    price = 55

    def __init__(self, color, weight, price):
        self.color = color
        self.weight = weight
        self.price = price
        print(f"Fruit object created with color {self.color}, weight {self.weight} kg, and price {self.price}$")
    
    def get_info(self):
        return f"Color: {self.color}, Weight: {self.weight} kg, Price: {self.price} $"
    
    def change_price(self, new_price):
        self.price = new_price
        print(f"Price updated to {self.price} $")
    

fruit = Fruit("blue", "0.2", "44")
fruit.change_price(66)

print(fruit.get_info())