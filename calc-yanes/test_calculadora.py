import unittest

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(0, 0), 0)
        self.assertEqual(subtracao(-1, -1), 0)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(2, 3), 6)
        self.assertEqual(multiplicacao(0, 5), 0)
        self.assertEqual(multiplicacao(-2, -3), 6)

    def test_divisao(self):
        self.assertEqual(divisao(6, 3), 2)
        self.assertEqual(divisao(0, 5), 0)
        self.assertEqual(divisao(-6, -2), 3)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divisao(5, 0)

if __name__ == '__main__':
    unittest.main()
