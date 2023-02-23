"""Implement the game."""


class Game:
    def __init__(self, num_discs):
        self.num_discs = num_discs
        self.stacks = [[i for i in range(num_discs, 0, -1)], [], []]

    def stack(self, stack_num):
        return list(self.stacks[stack_num])
        
        
