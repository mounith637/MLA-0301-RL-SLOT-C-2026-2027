import numpy as np
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Environment
grid_size = 4
goal = (3, 3)

# Parameters
battery = 10
episodes = 300
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.99
epsilon_min = 0.1

# Actions
actions = ["Up", "Down", "Left", "Right"]

# Build DQN Model
model = Sequential()
model.add(Dense(24, input_dim=2, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(4, activation='linear'))

model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))

# Move Function
def move(state, action):

    x, y = state

    if action == 0:
        x = max(0, x - 1)
    elif action == 1:
        x = min(grid_size - 1, x + 1)
    elif action == 2:
        y = max(0, y - 1)
    elif action == 3:
        y = min(grid_size - 1, y + 1)

    reward = -1

    if (x, y) == goal:
        reward = 100

    return (x, y), reward

# Training
for episode in range(episodes):

    state = (0, 0)
    battery_left = battery
    done = False

    while not done and battery_left > 0:

        state_input = np.array([[state[0], state[1]]])

        # ε-Greedy Policy
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            q = model.predict(state_input, verbose=0)
            action = np.argmax(q[0])

        next_state, reward = move(state, action)

        next_input = np.array([[next_state[0], next_state[1]]])

        target = reward

        if next_state != goal:
            next_q = model.predict(next_input, verbose=0)
            target = reward + gamma * np.max(next_q)

        target_q = model.predict(state_input, verbose=0)
        target_q[0][action] = target

        model.fit(state_input, target_q, epochs=1, verbose=0)

        state = next_state
        battery_left -= 1

        if state == goal:
            done = True

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

print("Training Completed!")

# Testing
print("\nDrone Delivery Route")

state = (0, 0)
battery_left = battery

print(state, end=" ")

while state != goal and battery_left > 0:

    state_input = np.array([[state[0], state[1]]])

    action = np.argmax(model.predict(state_input, verbose=0)[0])

    state, reward = move(state, action)

    print("->", state, end=" ")

    battery_left -= 1

if state == goal:
    print("\nDelivery Successful!")
else:
    print("\nBattery Exhausted!")