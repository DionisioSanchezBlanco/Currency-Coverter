class Crypto:
    def __init__(self, quantity):
        self.quantity = quantity
        self.value = {"RUB": 2.98, "ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}

    def coni_to_cash(self):
        for key, value in self.value.items():
            print(f"I will get {round(self.quantity * value, 2)} {key} from the sale of {self.quantity} conicoins.") 

conicoin = Crypto(float(input()))
conicoin.coni_to_cash()