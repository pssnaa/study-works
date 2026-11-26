import unittest
from Calculator import add, sub, multi, div, exponentiate, square, factorial

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        
    def test_sub(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(4, 10), -6)
        
    def test_multi(self):
        self.assertEqual(multi(3, 4), 12)
        self.assertEqual(multi(-3, 4), -12)
        
    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        with self.assertRaises(ValueError): #проверка при делении на ноль
            div(5, 0)
            
    def test_exponentiate(self): #возведение в степень
        self.assertEqual(exponentiate(2, 3), 8)
        self.assertEqual(exponentiate(5, 0), 1)
        self.assertEqual(exponentiate(2, -3), 0.125) #проверка отрицательной степени
        with self.assertRaises(ValueError):
            exponentiate(0, 0) #проверка нуля в нулевой степени
            
    def test_square(self): #корень
        self.assertEqual(square(9), 3)
        self.assertEqual(square(0), 0)
        self.assertAlmostEqual(square(2), 1.414, places=3) #проверка с погрешностью
        with self.assertRaises(ValueError): #проверка на вычисление корня из отрицательного числа
            square(-4)
            
    def test_factorial(self): #факториал
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-3)
        with self.assertRaises(ValueError):
            factorial(2.5)

if __name__ == '__main__':
    unittest.main()