class Burger:
    def __init__(self):
        self.price = 100

    def get_price(self):
        return self.price


class CheeseBurger(Burger):
    def __init__(self):
        super().__init__()
        self.price = 20 + super().get_price()

    def get_price(self):
        return self.price


if __name__ == "__main__":
    cheeseBurger = CheeseBurger()
    print(cheeseBurger.get_price())
