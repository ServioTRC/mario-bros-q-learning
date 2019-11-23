import time
import numpy as np
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import gym_super_mario_bros
from agent import DQNAgent

# Build env
env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# Parameters
states = (1, 240, 256, 3)
actions = env.action_space.n

# Agent
agent = DQNAgent(states=states, actions=actions, max_memory=100000, double_q=True)

# Episodes
episodes = 10000

# Timing
start = time.time()
step = 0

# Main loop
for e in range(episodes):

    try:
        # Reset env
        state = env.reset()

        # Reward
        total_reward = 0
        iter = 0

        # Play
        while True:

            # Show env
            # if e % 100 == 0:
            #     env.render()

            # Run agent
            action = agent.run(state=state)

            # Perform action
            next_state, reward, done, info = env.step(action=action)

            # Remember transition
            agent.add(experience=(state, next_state, action, reward, done))

            # Update agent
            agent.learn()

            # Total reward
            total_reward += reward

            # Update state
            state = next_state

            # Increment
            iter += 1

            # If done break loop
            if done or info['flag_get']:
                break

        # Print
        print('Episode {e} - +'
              'Frame {f} - +'
              'Frames/sec {fs} - +'
              'Epsilon {eps} - +'
              'Mean Reward {r}'.format(e=e,
                                       f=agent.step,
                                       fs=np.round((agent.step - step) / (time.time() - start)),
                                       eps=np.round(agent.eps, 4),
                                       r=(total_reward / iter)))
        start = time.time()
        step = agent.step
        agent.save_model()
        # Storing rewards
        if e % 10 == 0:
            with open("rewards.txt", 'a+') as rewards_file:
                rewards_file.write(str(total_reward / iter)+"\n")
    except AttributeError:
        pass
