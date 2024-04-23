class TwoNumbersSum:
    num1: float
    num2: float

    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def mean(self) -> float:
        return (self.num1 + self.num2) / 2

    def __str__(self):
        return f"A média entre {self.num1} e {self.num2} é {self.mean():2.f}"
    
def main(num1: float, num2: float) -> float:
    two_numbers = TwoNumbersSum(num1, num2)
    return two_numbers.mean()