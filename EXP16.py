import random

# States
states = ["Center", "Left", "Right", "Goal"]

# Actions
actions = ["Steer Left", "Steer Right", "Keep Straight"]

# Policy (Action for each state)
policy = {
    "Center": "Keep Straight",
    "Left": "Steer Right",
    "Right": "Steer Left"
}

# Rewards
rewards = {
    "Center": 10,
    "Left": -5,
    "Right": -5,
    "Goal": 100
}

# Transition Function
transitions = {
    ("Center", "Keep Straight"): "Goal",
    ("Left", "Steer Right"): "Center",
    ("Right", "Steer Left"): "Center"
}

episodes = 100

# Training (Simplified Policy Gradient)
for episode in range(episodes):

    state = random.choice(["Center", "Left", "Right"])

    while state != "Goal":

        action = policy[state]

        next_state = transitions[(state, action)]

        reward = rewards[next_state]

        # Simplified Policy Update
        if reward < 0:
            policy[state] = random.choice(actions)

        state = next_state

print("Training Completed!")

print("\nLearned Policy")
for state in policy:
    print(state, "->", policy[state])

# Testing
print("\nLane Keeping Simulation")

state = "Left"

print("Initial State:", state)

while state != "Goal":

    action = policy[state]

    print("Action:", action)

    state = transitions[(state, action)]

    print("Next State:", state)

print("\nVehicle Successfully Kept in Lane!")