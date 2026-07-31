import gymnasium as gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import random

# Create Environment
env = gym.make("FrozenLake-v1", is_slippery=False)

# Environment Details
state_size = env.observation_space.n
action_size = env.action_space.n

# Build Neural Network
model = Sequential([
    Dense(24, input_dim=state_size, activation='relu'),
    Dense(24, activation='relu'),
    Dense(action_size, activation='linear')
])

model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))

# Parameters
episodes = 100
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.99
epsilon_min = 0.01

# Training
for episode in range(episodes):

    state, _ = env.reset()
    done = False

    while not done:

        state_input = np.identity(state_size)[state:state+1]

        # ε-Greedy Action Selection
        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            q_values = model.predict(state_input, verbose=0)
            action = np.argmax(q_values[0])

        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        next_input = np.identity(state_size)[next_state:next_state+1]

        target = reward

        if not done:
            next_q = model.predict(next_input, verbose=0)
            target = reward + gamma * np.max(next_q)

        target_q = model.predict(state_input, verbose=0)
        target_q[0][action] = target

        model.fit(state_input, target_q, epochs=1, verbose=0)

        state = next_state

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

print("Training Completed!")

# Evaluation
state, _ = env.reset()
done = False

print("\nRobot Navigation:")

while not done:

    print("Current State:", state)

    state_input = np.identity(state_size)[state:state+1]

    action = np.argmax(model.predict(state_input, verbose=0)[0])

    state, reward, terminated, truncated, _ = env.step(action)

    done = terminated or truncated

print("Goal Reached!")