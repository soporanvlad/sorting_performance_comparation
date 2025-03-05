class Car:
    def __init__(self, brand, model, token, buy_price, sell_price):
        self._brand = brand
        self._model = model
        self._token = token
        self._buy_price = buy_price
        self._sell_price = sell_price

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_token(self):
        return self._token

    def get_buy_price(self):
        return self._buy_price

    def get_sell_price(self):
        return self._sell_price

    def get_profit(self):
        return self._buy_price - self._sell_price

    def set_brand(self, new_brand):
        self._brand = new_brand

    def set_model(self, new_model):
        self._model = new_model

    def set_buy_price(self, new_buy_price):
        self._buy_price = new_buy_price

    def set_sell_price(self, new_sell_price):
        self._sell_price = new_sell_price

    def __str__(self):
        return f' Brand: {self._brand} \n Model: {self._model} \n Bought for: {self._buy_price} \n Sold for: {self._sell_price} \n'

    @staticmethod
    def comparator_token(elem1, elem2):
        if elem1.get_token() < elem2.get_token():
            return 1
        elif elem1.get_token() > elem2.get_token():
            return -1
        else:
            return 0

    @staticmethod
    def comparator_brand_model(elem1, elem2):
        if elem1.get_brand() < elem2.get_brand():
            return 1
        elif elem1.get_brand() > elem2.get_brand():
            return -1
        elif elem1.get_brand() < elem2.get_brand():
            return 1
        elif elem1.get_brand() > elem2.get_brand():
            return -1
        else:
            return 0

    @staticmethod
    def comparator_brand_model_token(elem1, elem2):
        if elem1.get_brand() < elem2.get_brand():
            return 1
        elif elem1.get_brand() > elem2.get_brand():
            return -1
        elif elem1.get_model() < elem2.get_model():
            return 1
        elif elem1.get_model() > elem2.get_model():
            return -1
        elif elem1.get_token() < elem2.get_token():
            return 1
        elif elem1.get_token() > elem2.get_token():
            return -1
        else:
            return 0

    @staticmethod
    def comparator_profit(elem1, elem2):
        try:
            profit1 = int(elem1.get_sell_price()) - int(elem1.get_buy_price())
            profit2 = int(elem2.get_sell_price()) - int(elem2.get_buy_price())
            if profit1 < profit2:
                return 1
            elif profit1 > profit2:
                return -1
            else:
                return 0
        except ValueError:
            # Handle the case where the prices are not valid integers
            print("Invalid price format in comparator_profit")
            return 0  # or any other appropriate action

