import calculator
Calculator = calculator.Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        # arrange
        a = 123
        b = 321
        cal = Calculator()

        # act
        result = cal.subtract(b,a)

        # assert
        expected = 198
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 12
        b = 21
        cal = Calculator()

        # act
        result = cal.multiply(a,b)

        # assert
        expected = 252
        assert result == expected

    def test_divide(self):
        # arrange
        a = 2020
        b = 20
        cal = Calculator()

        # act
        result = cal.divide(a,b)

        # assert
        expected = 101
        assert result == expected
