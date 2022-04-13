"""
    Create a class World.
    The representation of the World is a grid (matrix).
    public attributes:
        - map_height - int
        - map_width - int
        - world_map - Matrix[int] or List[List[int]]
            - you can represent this using numpy's matrix or just basic
            python list of lists of integers
    public methods:
        - init_world() - returns nothing
            - creates the matrix of size map_height X map_width and all the
            elements of the matrix are initially 0
        - see_world() - returns nothing
            - this PRETTY prints the current map
        - update world(world_entity) - returns nothing
            - this updates the world_map with the entity_id of the world_entity
            passed as a parameter
"""

import numpy as np

class World():
    
    map_height: int = 10
    map_width: int = 10
    world_map = np.empty(shape=[map_height, map_width])


    def __init__(self):
        pass


    def init_world(self):
        self.world_map[self.map_height][self.map_width] = 0
        print(self.world_map)

    def see_world(self):
        pass

    def update_world(self, world_entity):
        pass


c = World()
print(c.init_world())
print(World.world_map)