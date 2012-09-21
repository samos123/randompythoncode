import unittest

from union import UnionQuickUnionWeighted

class Percolation(object):
    def __init__(self, n):
        self.n = n
        self.union_alg = UnionQuickUnionWeighted((n * n) + 2)
        self.top = (n * n)
        self.bottom = (n * n) + 1

    def _calculate_id(self, row, column):
        """
        Calculates the id which is used in our QuickUnion class.

        Take for example the following grid of n=5
        0   1   2   3   4
        5   6   7   8   9
        10  11  12  13  14
        15  16  17  18  19
        20  21  22  23  24

        To be able to do unions, we need to know the id
        of any given x and y.
        """
        return self.n * (row - 1) + column - 1

    def open(self, row, column):
        if row > self.n or column > self.n:
            raise Exception("out of range")
        id = self._calculate_id(row, column)
        if row == 1:
            self.union_alg.union(self.top, id)
        if row == self.n:
            self.union_alg.union(self.bottom, id)

        # Union with its open neighbours
        up = (row + 1, column)
        down = (row - 1, column)
        left = (row, column - 1)
        right = (row, column + 1)

        if up[0] <= self.n and self.is_open(*up):
            up_id = self._calculate_id(*up)
            self.union_alg.union(id, up_id)

        if row > 1 and self.is_open(*down):
            down_id = self._calculate_id(*down)
            self.union_alg.union(id, down_id)

        if right[1] <= self.n and self.is_open(*right):
            right_id = self._calculate_id(*right)
            self.union_alg.union(id, right_id)

        if column > 1 and self.is_open(*left):
            left_id = self._calculate_id(*left)
            self.union_alg.union(id, left_id)

        # In the union class set it as opened
        self.union_alg.ids[id]['open'] = True

    def percolates(self):
        return self.union_alg.connected(self.top, self.bottom)

    def is_open(self, x, y):
        id_x_y = self._calculate_id(x, y)
        return self.union_alg.ids[id_x_y].get('open', False)

    def is_full(self, x, y):
        id_x_y = self._calculate_id(x, y)
        return self.union_alg.connected(id_x_y, self.top)


class PercolationTestCase(unittest.TestCase):
    def test_is_open(self):
        perc = Percolation(3)
        perc.open(1, 1)
        self.assertTrue(perc.is_open(1, 1))
        self.assertFalse(perc.is_open(1, 2))
        self.assertTrue(perc.union_alg.ids[0]['open'])
        self.assertEqual(perc.union_alg.ids[0]['id'], perc.top)
        print perc.union_alg.ids

        perc.open(3, 3)
        self.assertTrue(perc.is_open(3, 3))
        self.assertTrue(perc.union_alg.ids[8]['open'])
        self.assertEqual(perc.union_alg.ids[8]['id'], perc.bottom)
        print perc.union_alg.ids

    def test_is_full(self):
        perc = Percolation(30)
        perc.open(1, 1)
        perc.open(1, 3)
        perc.open(1, 5)
        self.assertTrue(perc.is_full(1, 1))
        self.assertTrue(perc.is_full(1, 3))
        self.assertTrue(perc.is_full(1, 5))
        perc.open(2, 2)
        self.assertFalse(perc.is_full(2, 2))
        perc.open(1, 2)
        self.assertTrue(perc.is_full(1, 2))
        self.assertTrue(perc.is_full(2, 2))


        neighbours = [
            (5, 1), (5, 2), (4, 2),
            (6, 2), (5, 3), (3, 2)
        ]
        for neighbour in neighbours:
            perc.open(*neighbour)
        for neighbour in neighbours:
            self.assertTrue(perc.is_full(*neighbour))


    def test_percolates(self):
        perc = Percolation(5)
        perc.open(1, 1)
        perc.open(2, 1)
        perc.open(3, 1)
        perc.open(4, 1)
        self.assertFalse(perc.percolates())
        perc.open(5, 1)
        self.assertTrue(perc.percolates())

if __name__ == '__main__':
    unittest.main()

