class Crypto:
    def __init__(self, quantity, value):
        self.quantity = quantity
        self.value = value

    def coni_to_dollar(self):
        return self.quantity * self.value

quantity = int(input("Please, enter the number of conicoins you have:"))
value = float(input("Please, enter the exchange rate:"))
conicoin = Crypto(quantity, value)
print(f"The total amount of dollars: {conicoin.coni_to_dollar()}")