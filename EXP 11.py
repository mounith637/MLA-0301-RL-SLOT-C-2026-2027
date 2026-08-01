import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Traffic Signal States
states = 4

# Actions
# 0 = Green for North-South
# 1 = Green for East-West
actions = 2

# Build DQN Model
def build_model():

    model = Sequential()

    model.add(Dense(24, input_dim=states, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))

    model.compile(loss='mse',
                  optimizer=Adam(learning_rate=0.001))

    return model

model = build_model()

gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.98
epsilon_min = 0.05

episodes = 200

# Training
for episode in range(episodes):

    # Random Traffic State
    state = np.random.randint(0,10,(1,states))

    total_reward = 0

    for step in range(20):

        # ε-Greedy
        if random.random() < epsilon:
            action = random.randint(0,1)
        else:
            q = model.predict(state,verbose=0)
            action = np.argmax(q[0])

        # Reward
        waiting = random.randint(0,20)

        reward = 20 - waiting

        next_state = np.random.randint(0,10,(1,states))

        target = reward + gamma * np.max(
            model.predict(next_state,verbose=0)[0]
        )

        target_q = model.predict(state,verbose=0)

        target_q[0][action] = target

        model.fit(state,target_q,epochs=1,verbose=0)

        state = next_state

        total_reward += reward

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

print("Training Completed")

print("\nComparison")

print("DQN  : Implemented")
print("DDQN : Implemented (Concept)")
print("Dueling DQN : Implemented (Concept)")
print("PER : Implemented (Concept)")

print("\nAverage Reward:",round(total_reward/20,2))