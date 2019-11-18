from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import sys
import numpy as np
import time
np.set_printoptions(threshold=sys.maxsize)


env = gym_super_mario_bros.make('SuperMarioBros-v0')
state = env.reset()
# DISCRETE_OS_SIZE = np.full((240, 256, 3), 20)
# discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE
# print(env.action_space)
# q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))
done = False
while not done:
    action = env.action_space.sample()  # choose random action
    observation, reward, done, info = env.step(action)  # feedback from environment
    print(action)
    env.render()