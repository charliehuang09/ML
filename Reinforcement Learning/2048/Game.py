from gym import Env
import numpy as np
import random
from gym.spaces import Discrete, Box
class ShowerEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        # Temperature array
        # Set start temp
        self.state = float(38 + random.randint(-3,3))
        # Set shower length
        self.shower_length = 100
        
    def step(self, action):
        # Apply action
        # 0 -1 = -1 temperature
        # 1 -1 = 0 
        # 2 -1 = 1 temperature 
        self.state += action - 1 
        # Reduce shower length by 1 second
        self.shower_length -= 1 
        
        # Calculate reward
        if self.state >= 37 and self.state <= 39: 
            reward = 1
        else: 
            reward = -1 
        
        # Check if shower is done
        if self.shower_length <= 0: 
            done = True
        else:
            done = False
        
        # Apply temperature noise
        # self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}
        
        # Return step information
        return float(self.state), reward, done, info

    def render(self):
        # Implement viz
        pass
    
    def reset(self):
        # Reset shower temperature
        self.state = float(38 + random.randint(-3,3))
        # Reset shower time
        self.shower_length = 100 
        return float(self.state)
    