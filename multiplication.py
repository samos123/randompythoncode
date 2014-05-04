import unittest
from random import randint

from math import ceil


memory = [[0,0,0,0,0,0,0,0,0,0],
          [0,1,2,3,4,5,6,7,8,9],
          [0,2,4,6,8,10,12,14,16,18],
          [0,3,6,9,12,15,18,21,24,27],
          [0,4,8,12,16,20,24,28,32,36],
          [0,5,10,15,20,25,30,35,40,45],
          [0,6,12,18,24,30,36,42,48,54],
          [0,7,14,21,28,35,42,49,56,63],
          [0,8,16,24,32,40,48,56,64,72],
          [0,9,18,27,36,45,54,63,72,81],
          [0,10,20,30,40,50,60,70,80,90]]


def prepend_zeros(str_x, n):
    diff = n - len(str_x)
    str_x = "0" * diff + str_x
    return str_x


def mult(x, y):
    """ Recursive multiplication using
    x = 10^n/2 * a + b
    y = 10^n/2 * c + d
    x * y = 10^n * ac + 10^(n/2) (ad+bc) + bd
    """
    str_x, str_y = str(x), str(y)
    n = max(len(str_x), len(str_y))
    if n <= 1:
        return memory[x][y]

    str_x = prepend_zeros(str_x, n)
    str_y = prepend_zeros(str_y, n)
    n_2 = n / 2

    a, b = int(str_x[:n_2] or 0), int(str_x[n_2:] or 0)
    c, d = int(str_y[:n_2] or 0), int(str_y[n_2:] or 0)

    ac = mult(a, c)
    ad_bc = mult(a, d) + mult(b, c)
    bd = mult(b, d)

    print "a: %s, b: %s, c: %s, d: %s" % (a, b, c, d)
    print "ac: %s, ad + bc: %s, bd: %s" %(ac, ad_bc, bd)
    print "n: %s, n/2: %s" % (n, n_2)

    # for supporting edge case where n is not a multiple of 2
    n_2 = int(ceil(n / 2.0))
    n = n if n % 2 == 0 else n + 1
    return (10**(n) * ac)  + (10**n_2 * ad_bc) + bd


class MultiplicationTestCase(unittest.TestCase):
    __test__ = False # Tell nosetests not to run this test case by itself

    def test_small_numbers(self):
        self.assertEqual(self.func(5, 5), 25)

    def test_different_size(self):
        self.assertEqual(self.func(2, 21), 42)

    def test_different_size(self):
        self.assertEqual(self.func(103, 3097), 318991)

    def test_two_digits1(self):
        self.assertEqual(self.func(50, 50), 2500)

    def test_two_digits2(self):
        self.assertEqual(self.func(19, 21), 399)

    def test_three_digits1(self):
        self.assertEqual(self.func(500, 500), 250000)

    def test_three_digits2(self):
        self.assertEqual(self.func(223, 321), 71583)

    def test_four_digits1(self):
        self.assertEqual(self.func(1234, 4321), 5332114)

    def test_seven_digits(self):
        self.assertEqual(self.func(5000000, 5000000),
                         25000000000000)

    def test_random_cases(self):
        for i in range(1000):
            x = randint(1,100000)
            y = randint(1,100000)
            expected = x * y
            result = self.func(x, y)
            self.assertEqual(self.func(x, y), expected,
                            ("Failed with x: %s and y: %s. "
                             "Expected: %s but got %s") % 
                             (x, y, expected, result))


class RecursiveMultiplicationTestCase(MultiplicationTestCase):
    __test__ = True
    def setUp(self):
        self.func = mult

