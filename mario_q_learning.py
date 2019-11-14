from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
state = env.reset()

done = False
while not done:
    action = env.action_space.sample()
    new_state, reward, done, _ = env.step(action)
    print(reward, new_state)
    env.render()