import unittest


class UnionQuickfind(object):
    def __init__(self, n):
        self.ids = [i for i in range(0, n)]

    def union(self, p, q):
        pid = self.ids[p]
        qid = self.ids[q]
        for value, id in enumerate(self.ids):
            if id == pid:
                self.ids[value] = qid

    def connected(self, p, q):
        return self.ids[p] == self.ids[q]

class UnionQuickUnion(object):
    def __init__(self, n):
        self.ids = [i for i in range(0, n)]

    def union(self, p, q):
        self.ids[self.root(p)] = self.root(q)
#        self.ids[q] =

    def root(self, value):
        while self.ids[value] != value:
            value = self.ids[value]
        return value

    def connected(self, p, q):
        return self.root(p) == self.root(q)

class UnionQuickUnionWeighted(object):
    def __init__(self, n):
        self.ids = [{'id': i, 'size': 1} for i in range(0, n)]

    def union(self, p, q):
        rootp = self.root(p)
        rootq = self.root(q)
        if self.ids[rootp]['size'] < self.ids[rootq]['size']:
            self.ids[rootp]['id'] = rootq
            self.ids[rootq]['size'] += self.ids[rootp]['size']
        else:
            self.ids[rootq]['id'] = rootp
            self.ids[rootp]['size'] += self.ids[rootq]['size']

    def root(self, value):
        while self.ids[value]['id'] != value:
            value = self.ids[value]['id']
        return value

    def connected(self, p, q):
        return self.root(p) == self.root(q)



class UnionTestCase(unittest.TestCase):
    def setUp(self):
        self.unions = [UnionQuickUnion(10),
                       UnionQuickfind(10),
                       UnionQuickUnionWeighted(10)]

    def test_connected(self):
        for un in self.unions:
            un.union(0, 5)
            connected = un.connected(0, 5)
            self.assertTrue(connected)
            un.union(1, 2)
            un.union(1, 3)
            connected = un.connected(2, 3)
            self.assertTrue(connected)
            connected = un.connected(1, 3)
            self.assertTrue(connected)
            un.union(5, 6)
            un.union(6, 7)
            connected = un.connected(5, 7)
            self.assertTrue(connected)
            connected = un.connected(5, 6)
            self.assertTrue(connected)
            connected = un.connected(6, 5)
            self.assertTrue(connected)
            connected = un.connected(6, 7)
            self.assertTrue(connected)
            connected = un.connected(0, 5)
            self.assertTrue(connected)
            connected = un.connected(0, 6)
            self.assertTrue(connected)
            connected = un.connected(0, 7)
            self.assertTrue(connected)


if __name__ == '__main__':
    unittest.main()


