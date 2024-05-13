import random

class SimpleEnvironment:
    def __init__(self):
        self.states = ["s1", "s2"]
        self.actions = ["a1", "a2", "a3"]
        
        self.trans = {
            #(state, action): {(next_state, reward): probability}
            ("s1", "a1"): {("s1", +1): 1},
            ("s1", "a2"): {("s1", +4): 0.7, ("s2", +5): 0.3},
            ("s2", "a1"): {("s2", +1): 1},
            ("s2", "a2"): {("s1", -3): 0.8, ("s2", +2): 0.2},
            ("s2", "a3"): {("s1", 0): 1}
        }
    def reset(self):
        self.current_state = random.choice(self.states)
        return self.current_state
    
    def step(self, action):
        trans_value = self.trans[(self.current_state, action)]
        next_state, reward = random.choice(list(trans_value.items()))[0]
        self.current_state = next_state
        return next_state, reward
