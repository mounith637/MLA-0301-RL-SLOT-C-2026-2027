import numpy as np
import random

# Parking Environment
states = ["Start", "Move", "NearParking", "Parked"]

# Actions
actions = ["Forward", "Left", "Right", "Park"]

# Rewards
rewards = {
    "Start": 0,
    "Move": -1,
    "NearParking": 10,
    "Parked": 100
}

# Transition Function
transitions = {
    ("Start", "Forward"): "Move",
    ("Move", "Left"): "NearParking",
    ("Move", "Right"): "Move",
    ("NearParking", "Park"): "Parked"
}

# Policy Probabilities
policy = {
    "Start": {"Forward": 1.0},
    "Move": {"Left": 0.5, "Right": 0.5},
    "NearParking": {"Park": 1.0}
}

gamma = 0.9
episodes = 100

# REINFORCE Training
for episode in range(episodes):

    state = "Start"
    episode_data = []

    while state != "Parked":

        available_actions = list(policy[state].keys())

        action = random.choice(available_actions)

        next_state = transitions[(state, action)]

        reward = rewards[next_state]

        episode_data.append((state, action, reward))

        state = next_state

    # Calculate Returns
    G = 0

    for state, action, reward in reversed(episode_data):

        G = reward + gamma * G

        # Simple Policy Update
        policy[state][action] = min(1.0, policy[state][action] + 0.01)

print("Training Completed!")

# Evaluation
print("\nAutonomous Parking Simulation")

state = "Start"

print("Current State:", state)

while state != "Parked":

    action = max(policy[state], key=policy[state].get)

    print("Action:", action)

    state = transitions[(state, action)]

    print("Next State:", state)

print("\nVehicle Parked Successfully!")