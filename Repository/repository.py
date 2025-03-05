from Domain.entity import Car
import string
import random


class Repository:
    def __init__(self, file_name):
        self.cars = {}
        self.file_name = file_name

    def read_from_file(self):
        self.cars = {}
        with open(self.file_name, 'r') as f:
            for line in f:
                new_line = line.strip().split(' ')
                car = Car(new_line[0], new_line[1], new_line[2], new_line[3], new_line[4])
                self.cars[car.get_token()] = car

    def get_all(self):
        return self.cars

    def print_all_cars(self):
        self.read_from_file()
        return list(self.cars.values())

    def save_to_file(self):
        with open(self.file_name, 'w') as f:
            for car in self.cars.values():
                line = f'{car.get_brand()} {car.get_model()} {car.get_token()} {car.get_buy_price()} {car.get_sell_price()}'
                f.write(line)
                f.write("\n")

    def __generate_token(self, length=6):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def generate_cars(self, nr_cars):
        brands = ["Audi", "BMW", "Mercedes", "Toyota", "Ford", "Volkswagen", "Honda", "Tesla", "Hyundai"]
        models = ["Seria_3", "A4", "C-Class", "Focus", "Golf", "Civic", "A-Class", "Rio"]
        tokens = []
        while len(self.cars) < nr_cars:
            token = self.__generate_token()
            if token not in tokens:
                tokens.append(token)
                brand = random.choice(brands)
                model = random.choice(models)
                buy_price = random.randint(15000, 30000)
                sell_price = random.randint(3000, 12000)
                car = Car(brand, model, token, buy_price, sell_price)
                self.cars[token] = car
        self.save_to_file()
