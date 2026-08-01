import random

# Lane States
states = ["Left", "Center", "Right", "Goal"]

# Possible Actions
actions = ["Steer Left", "Steer Right", "Straight"]

# Initial Policy
policy = {
    "Left": "Steer Right",
    "Center": "Straight",
    "Right": "Steer Left"
}

# Reward Function
rewards = {
    "Left": -5,
    "Center": 10,
    "Right": -5,
    "Goal": 100
}

# Transition Function
transitions = {
    ("Left", "Steer Right"): "Center",
    ("Center", "Straight"): "Goal",
    ("Right", "Steer Left"): "Center"
}

episodes = 100

print("Training Started...\n")

# Simplified Policy Gradient Training
for episode in range(episodes):

    state = random.choice(["Left", "Center", "Right"])

    while state != "Goal":

        action = policy[state]

        next_state = transitions[(state, action)]

        reward = rewards[next_state]

        # Simple Policy Update
        if reward > 0:
            policy[state] = action
        else:
            policy[state] = random.choice(actions)

        state = next_state

print("Training Completed!\n")

# Evaluation
print("Autonomous Lane Keeping Simulation\n")

state = "Left"

print("Initial State :", state)

while state != "Goal":

    action = policy[state]

    print("Action :", action)

    state = transitions[(state, action)]

    print("Next State :", state)

print("\nVehicle Successfully Reached the Goal!")