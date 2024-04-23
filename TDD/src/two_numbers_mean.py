class TwoNumbersMean:
    num1: float
    num2: float

    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def mean(self) -> float:
        return round((self.num1 + self.num2) / 2, 1)

    def __str__(self):
        return f"A média entre {self.num1} e {self.num2} é {self.mean()}"