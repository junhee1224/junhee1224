import random

class GridEnv:
    def __init__(self):
        self.gridSize = 4
        self.terminalStates = [(0,0), (self.gridSize-1, self.gridSize-1)]
        self.actions = [(1,0),(0,1),(-1,0),(0,-1)]
        self.states = [(i,j) for i in range(self.gridSize)
                       for j in range(self.gridSize)
                       if (i,j) not in self.terminalStates]
    def reset(self):
        self.current_state = random.choice(self.states)
        return self.current_state
    
    def step(self,action):
        next_state = (self.current_state[0] + action[0], self.current_state[1] + action[1])
        reward = -1
        self.current_state = next_state
        return next_state, reward

env = GridEnv