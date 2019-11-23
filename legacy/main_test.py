from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
observation = env.reset()
done = False
t = 0
while not done:
    action = env.action_space.sample()  # choose random action
    observation, reward, done, info = env.step(action)  # feedback from environment
    # t += 1
    # if not t % 100:
    #     #print(t, info)
    print(observation)
    print(reward)
    print(done)
    raise Exception("bien")
    env.render()
