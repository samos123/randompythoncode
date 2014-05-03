import unittest

from math import ceil

def mult(x, y):
    """ Recursive multiplication using
    x = 10^n/2 * a + b
    y = 10^n/2 * c + d
    x * y = 10^n * ac + 10^(n/2) (ad+bc) + bd
    """
    if x == 1:
        return y
    if y == 1:
        return x
    if x == 0 or y == 0:
        return 0

    str_x, str_y = str(x), str(y)
    n = max(len(str_x), len(str_y))
    if n <= 2:
        return x * y

    n_2 = int(ceil(n/2.0))

    if len(str_x) <= 2:
        a , b = 0, x
    else:
        a, b = int(str_x[:n_2 - 1] or 0), int(str_x[n_2 - 1:] or 0)
    if len(str_y) <= 2:
        c , d = 0, y
    else:
        c, d = int(str_y[:n_2 - 1] or 0), int(str_y[n_2 - 1:] or 0)

    ac = mult(a, c)
    ad_bc = mult(a, d) + mult(b, c)
    bd = mult(b, d)

    print "a: %s, b: %s, c: %s, d: %s" % (a, b, c, d)
    print "ac: %s, ad + bc: %s, bd: %s" %(ac, ad_bc, bd)

    # Still can't see why 10^(n+1)
    return (10**(n+1) * ac)  + (10**n_2 * ad_bc) + bd


class MultiplicationTestCase(unittest.TestCase):
    __test__ = False # Tell nosetests not to run this test case by itself

    def test_small_numbers(self):
        self.assertEqual(self.func(5, 5), 25)

    def test_different_size(self):
        self.assertEqual(self.func(5, 155), 775)

    def test_two_digits1(self):
        self.assertEqual(self.func(50, 50), 2500)

    def test_two_digits2(self):
        self.assertEqual(self.func(19, 21), 399)

    def test_three_digits1(self):
        self.assertEqual(self.func(500, 500), 250000)

    def test_three_digits2(self):
        self.assertEqual(self.func(256, 652), 166912)

    def test_seven_digits(self):
        self.assertEqual(self.func(5000000, 5000000), 25000000000000)


class RecursiveMultiplicationTestCase(MultiplicationTestCase):
    __test__ = True
    def setUp(self):
        self.func = mult

