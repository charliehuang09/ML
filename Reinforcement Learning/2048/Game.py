from gym import Env
import numpy as np
import random
import gym.spaces as spaces


class ShowerTestEnv(Env):
    def __init__(self):
        self.action_space = spaces.MultiDiscrete(3)
        self.observation_space = spaces.Box(low=0, high=100, shape=(1,), dtype=np.float32)
        # Set start tempa
        self.state = 38 + random.randint(-3,3)
        # Set shower length
        self.shower_length = 60
        
    def step(self, action):
        # action = action.index(max(action))
        action = 0
        self.state += action -1 
        # Reduce shower length by 1 second
        self.shower_length -= 1 
        
        # Calculate reward
        if self.state >=37 and self.state <=39: 
            reward = 1 
        else: 
            reward = -1 
        
        # Check if shower is done
        if self.shower_length <= 0: 
            done = True
        else:
            done = False
        
        # Apply temperature noise
        self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}
        
        # Return step information
        self.state = max(0, self.state)
        self.state = min(100, self.state)
        return np.array([self.state]), reward, done, info

    def render(self):
        # Implement viz
        pass
    def close(self):
        pass
    
    def reset(self):
        self.state = 38 + random.randint(-3,3)
        self.shower_length = 60 
        return np.array([self.state])

class ShowerEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = spaces.Discrete(3)
        # Temperature array
        self.observation_space = spaces.Box(low=0, high=100, shape=(1,), dtype=np.float32)
        # Set start tempa
        self.state = 38 + random.randint(-3,3)
        # Set shower length
        self.shower_length = 60
        
    def step(self, action):
        # Apply action
        # 0 -1 = -1 temperature
        # 1 -1 = 0 
        # 2 -1 = 1 temperature 
        self.state += action -1 
        # Reduce shower length by 1 second
        self.shower_length -= 1 
        
        # Calculate reward
        if self.state >=37 and self.state <=39: 
            reward = 1 
        else: 
            reward = -1 
        
        # Check if shower is done
        if self.shower_length <= 0: 
            done = True
        else:
            done = False
        
        # Apply temperature noise
        self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}
        
        # Return step information
        self.state = max(0, self.state)
        self.state = min(100, self.state)
        return np.array([self.state]), reward, done, info

    def render(self):
        # Implement viz
        pass
    def close(self):
        pass
    
    def reset(self):
        # Reset shower temperature
        self.state = 38 + random.randint(-3,3)
        # Reset shower time
        self.shower_length = 60 
        return np.array([self.state])

class env2048(Env):
    def __init__(self, size = 4):
        self.size = size
        self.action_space=spaces.Box(0, 1.0, (4,4))
        self.observation_space = spaces.Box(low=0, high=20, shape=(1,), dtype=np.float32)
        self.state = np.zeros(shape=(size, size))
        self.randomBlock()
    
    def filled(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == 0:
                    return False
        return True
    def randomBlock(self):
        x = np.random.randint(0, self.size)
        y = np.random.randint(0, self.size)
        while self.state[x][y] != 0:
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
        self.state[x][y] = random.randint(1, 2)
    def left(self):
        change = False
        for i in range(self.size):
            prev = 0
            for j in range(1, self.size):
                if self.state[i][j] == 0:
                    continue
                if self.state[i][prev] == self.state[i][j]:
                    self.state[i][prev] += 1
                    self.state[i][j] = 0
                    change = True
                    continue
                if self.state[i][prev] == 0:
                    self.state[i][prev], self.state[i][j] = self.state[i][j], self.state[i][prev]
                    change = True
                    continue
                if self.state[i][prev] != self.state[i][j]:
                    self.state[i][prev + 1], self.state[i][j] = self.state[i][j], self.state[i][prev + 1]
                    prev += 1
                    change = True
        return change
    def right(self):
        change = False
        for i in range(self.size):
            prev = self.size - 1
            for j in range(self.size - 2, -1, -1):
                if self.state[i][j] == 0:
                    continue
                if self.state[i][prev] == self.state[i][j]:
                    self.state[i][prev] += 1
                    self.state[i][j] = 0
                    change = True
                    continue
                if self.state[i][prev] == 0:
                    self.state[i][prev], self.state[i][j] = self.state[i][j], self.state[i][prev]
                    change = True
                    continue
                if self.state[i][prev] != self.state[i][j]:
                    self.state[i][prev - 1], self.state[i][j] = self.state[i][j], self.state[i][prev - 1]
                    prev -= 1
                    change = True
        return change
    def up(self):
        change = False
        for i in range(self.size):
            prev = 0
            for j in range(1, self.size):
                if self.state[j][i] == 0:
                    continue
                if self.state[prev][i] == self.state[j][i]:
                    self.state[prev][i] += 1
                    self.state[j][i] = 0
                    change = True
                    continue
                if self.state[prev][i] == 0:
                    self.state[prev][i], self.state[j][i] = self.state[j][i], self.state[prev][i]
                    change = True
                    continue
                if self.state[prev][i] != self.state[j][i]:
                    self.state[prev + 1][i], self.state[j][i] = self.state[j][i], self.state[prev + 1][i]
                    prev += 1
                    change = True
        return change
    def down(self):
        change = False
        for i in range(self.size):
            prev = self.size - 1
            for j in range(self.size - 2, -1, -1):
                if self.state[j][i] == 0:
                    continue
                if self.state[prev][i] == self.state[j][i]:
                    self.state[prev][i] += 1
                    self.state[j][i] = 0
                    change = True
                    continue
                if self.state[prev][i] == 0:
                    self.state[prev][i], self.state[j][i] = self.state[j][i], self.state[prev][i]
                    change = True
                    continue
                if self.state[prev][i] != self.state[j][i]:
                    self.state[prev - 1][i], self.state[j][i] = self.state[j][i], self.state[prev - 1][i]
                    prev -= 1
                    change = True
        return change
    def move(self, action):
        print(action)
        if action == 0:
            return self.left()
        if action == 1:
            return self.right()
        if action == 2:
            return self.up()
        if action == 3:
            return self.down()
    def reward(self):
        reward = 0
        for i in range(self.size):
            for j in range(self.size):
                reward += self.state[i][j]
        return reward
    def done(self):
        for i in range(self.size - 1):
            for j in range(self.size - 1):
                if self.state[i][j] == 0 or self.state[i][j] == self.state[i][j + 1] or self.state[i][j] == self.state[i + 1][j]:
                    return False
        for i in range(self.size):
            if self.state[self.state - 1][i] == 0 or self.state[i][self.state - 1] == 0:
                return False
        return True
    def step(self, inputs):
        action = np.argmax(inputs)
        inputs[action] = -1
        while (self.move(action) == False):
            action = np.argmax(inputs)
            inputs[action] = -1
        self.render()
        self.randomBlock()
        info = {}
        done = self.done()
        reward = 1
        if done:
            reward = -1
        return self.state, reward, done, info
    def render(self):
        print(self.state)
    def close(self):
        pass
    def reset(self):
        self.state = np.zeros(shape=(4, 4))
        self.randomBlock()
        return np.array([self.state])

class test2048(Env):
    def __init__(self, size = 4):
        self.size = size
        self.action_space=spaces.Box(0, 1.0, (3,))
        self.observation_space = spaces.Box(low=0, high=20, shape=(1,), dtype=np.float32)
        self.state = 10
        self.timestep = 0
        self.stop = 50
        
    def step(self, action):
        action = np.argmax(action)
        self.state += action - 1
        if self.state >= 9 and self.state <= 11:
            reward = 1
        else:
            reward = -1
        self.state += np.random.randint(-1, 2)
        self.timestep += 1
        done = False
        if self.timestep >= self.stop:
            done = True
        
        return np.array([self.state]), reward, done, {}


    def render(self):
        # Implement viz
        pass
    def close(self):
        pass
    
    def reset(self):
        self.state = 10
        self.timestep = 0
        return np.array([self.state])
