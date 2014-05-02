import unittest

from beautiful_strings import max_beauty


class BSTestCase(unittest.TestCase):

    def test_1(self):
        result = max_beauty("ABbCcc")
        exptected = 152
        self.assertEquals(result, exptected)

    def test_2(self):
        result = max_beauty("Good luck in the Facebook Hacker Cup this year!")
        exptected = 754
        self.assertEquals(result, exptected)

    def test_3(self):
        result = max_beauty("Ignore punctuation, please :)")
        exptected = 491
        self.assertEquals(result, exptected)

