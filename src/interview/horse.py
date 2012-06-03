import sys
import dijkstra
import bfs


class Horse(object):
    """
    The logic for finding the shortest path from a Horse current position
    to the desired position.
    """
    
    def __init__(self, n, x, y):
        """
        Initialize a horse on field of n * n, the field is 1..n and not 0..n-1 important to note!
        x: The position of the horse which should be > 0 and < n
        y: The y position of the horse which should be > 0 and < n
        """
        if (x <= 0 or x > n) or (y <= 0 or y > n):
            raise Exception('X and Y should be greater than 0 but smaller than n')
        self.current_pos = {'x': x, 'y': y}
        self.n = n
        self.graph = {'horse' : 0}
                
    def possible_moves(self, position_x=None, position_y=None):
        # The 8 different steps you can take from a fixed position
        possible_steps = [(1, 2),(2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2) ]
        moves = []
        for step in possible_steps:
            move_x = position_x + step[0]
            move_y = position_y + step[1]
            # You can only move inside the field
            if not move_x > self.n and not move_y > self.n and move_y > 0 and move_x > 0:
                moves.append({'x': move_x, 'y': move_y})
        return moves

        

    def create_smarter_graph(self):
        """
        Create a graph based on the amount of rows and columns based on fields
        """
        self.graph = {}
        
        # Loop through all the fields based on n starting from 1..n
        for x in range(1, self.n+1):
            for y in range(1, self.n+1):
                
                # Get the possible moves for the current position in the field
                possibile_position_ids = []
                for possible_position in self.possible_moves(x,y):
                    if possible_position['x'] == self.current_pos['x'] and possible_position['y'] == self.current_pos['x']:
                        possibile_position_id = 'horse'
                    else:
                        possibile_position_id = 'x{x}_y{y}'.format(x=possible_position['x'], 
                                                               y=possible_position['y'])
                    possibile_position_ids.append(possibile_position_id)
                
                # Add current field position with the neighbors to the graph
                if self.current_pos['x'] == x and self.current_pos['y'] == y:
                    # If the current field equals the current pos of the horse we should name it horse
                    # this is used later to find the shortest path to horse from any position
                    current_position_id = 'horse'
                else:
                    current_position_id = 'x{x}_y{y}'.format(x=x, y=y)
                    
                self.graph[current_position_id] = possibile_position_ids
        
    
    def shortest_path_bfs(self, x=None, y=None):
        self.create_smarter_graph()
        if x == None or y == None:
            x = self.n
            y = self.n
        return bfs.shortest_path(self.graph, 'horse', 'x{x}_y{y}'.format(x=x, y=y))

    def shortest_path_stupid(self, x=None, y=None):
        if x == None or y == None:
            x = self.n
            y = self.n
        self.create_stupid_graph()
        return dijkstra.shortestpath(self.graph, 'x{x}_y{y}'.format(x=x, y=y), 'horse')
    
    def create_stupid_graph(self, previous_moves=None, next_moves=None):
        """
        Method used to create a Graph defining the distances between every move.
        
        We create a graph which has the following direction
        
        Example of output of the graph:
        
        {'horse' : 0,
         'x3_y2' : {'horse': 1}, etc...}
         
        This graph is used to calculate the shortest path with dijkstras algorithm.
        I think its a little stupid how I create the graph so I called it create_stupid_graph,
        there must be a better way to create it efficiently.
        
        """
        first_time = False
        if previous_moves == None:
            previous_moves = []
        if next_moves == None:
            first_time = True
            next_moves = [self.current_pos]
        
        
        # the moves to put in the graph for next recursion
        new_next_moves = []
        
        # loop through the possible next moves
        for next_move in next_moves:
            next_move_id = 'x{x}_y{y}'.format(x=next_move['x'], y=next_move['y'])
            # Get the possible moves of the current move
            possible_moves = self.possible_moves(next_move['x'], next_move['y'])
            
            # For every possible move add it to the graph with the distance of the previous move
            for possible_move in possible_moves:
                possible_move_id = 'x{x}_y{y}'.format(x=possible_move['x'], y=possible_move['y'])
                
                # Only add it to the graph if it wasnt already added
                if possible_move_id not in previous_moves:
                    if first_time:
                        self.graph[possible_move_id] = {'horse': 1}
                    else:
                        if self.graph.has_key(possible_move_id):
                            self.graph[possible_move_id][next_move_id] = 1
                        else:
                            self.graph[possible_move_id] = {next_move_id: 1}
                        
                    # this is really important this prevents it from going to unlimited recursion
                    # it only adds the possible moves which we didnt add to the graph yet
                    new_next_moves.append(possible_move)
            previous_moves.append(next_move_id)
        
        # If we already went through all the possible moves the function wont be called again
        if new_next_moves:
            # rerun the function with next_moves = possible_moves untill there are no new next moves anymore
            return self.create_stupid_graph(previous_moves=previous_moves, next_moves=new_next_moves)
        
            
        

if __name__ == '__main__':
    if (len(sys.argv) > 1):     
        try:
            n = int(sys.argv[1])
            x = int(sys.argv[2])
            y = int(sys.argv[3])
        except:
            print 'Please pass the parameters n x y as follows: horse.py n x y, for example horse.py 10 1 1'
        finally:
            horse = Horse(n,x,y)
            print horse.shortest_path_bfs()


