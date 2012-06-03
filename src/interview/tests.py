import unittest
from horse import Horse
class HorseTestCase(unittest.TestCase):
    def setUp(self):
        self.horse = Horse(n=300, x=1, y=1)

    def test_shortest_path(self):
        print self.horse.shortest_path_bfs()
        
#        
#    def test_create_graph(self):
#        self.horse.create_graph()
#        print self.horse.graph
    
    def test_possibile_moves(self):
        horse10 = Horse(n=10, x=1, y=1)
        possible_moves = horse10.possible_moves(7, 7)
        self.assertEqual(possible_moves, 
                         [{'y': 9, 'x': 8}, {'y': 8, 'x': 9}, 
                          {'y': 6, 'x': 9}, {'y': 5, 'x': 8}, 
                          {'y': 5, 'x': 6}, {'y': 6, 'x': 5}, 
                          {'y': 8, 'x': 5}, {'y': 9, 'x': 6}])
        
        
        possible_moves = horse10.possible_moves(10, 10)
        self.assertEqual(possible_moves, [{'y': 8, 'x': 9}, {'y': 9, 'x': 8}])
        
        # test the 1 off case that it also is able to move to a position on the 10th row
        possible_moves = horse10.possible_moves(9, 10)
        self.assertEqual(possible_moves, [{'y': 8, 'x': 10}, {'y': 8, 'x': 8}, {'y': 9, 'x': 7}])
        
        possible_moves = horse10.possible_moves(1, 1)
        self.assertEqual(possible_moves, [{'y': 3, 'x': 2}, {'y': 2, 'x': 3}])
        

        


if __name__ == '__main__':
#    t = Timer("""horse.create_graph()""", setup="""from __main__ import Horse \nhorse = Horse(n=10, x=1, y=1)""")
#    print t.timeit()
    unittest.main()