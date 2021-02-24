class Crypto:
    def __init__(self, quantity):
        self.quantity = quantity
        self.value = 100

    def coni_to_dollar(self):
        return self.quantity * 100

conicoin = Crypto(int(input()))
print(f"I have {conicoin.quantity} conicoins.")
print(f"{conicoin.quantity} conicoins cost {conicoin.coni_to_dollar()} dollars.")
print("I am rich! Yippee!")