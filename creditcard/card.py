from .luhn import Luhn
from .utils import sanitize


class CreditCard:
    def __init__(self, number):
        self.number = sanitize(number)

    def is_valid(self):
        return all([
            len(self.number) in range(13, 19),
            Luhn.checkdigit(self.number)
        ])
