from TDD.src.two_numbers_mean import TwoNumbersMean


class TestTwoNumbersMean:

    def test_mean(self):
        two_numbers = TwoNumbersMean(10, 20)
        assert two_numbers.mean() == 15.0

    def test_mean_negative(self):
        two_numbers = TwoNumbersMean(-10, 20)
        assert two_numbers.mean() == 5.0

    def test_mean_negative_2(self):
        two_numbers = TwoNumbersMean(-10, -20)
        assert two_numbers.mean() == -15.0

    def test_mean_zero(self):
        two_numbers = TwoNumbersMean(0, 0)
        assert two_numbers.mean() == 0.0

    def test_str(self):
        two_numbers = TwoNumbersMean(10, 20)
        assert str(two_numbers) == "A média entre 10 e 20 é 15.0"