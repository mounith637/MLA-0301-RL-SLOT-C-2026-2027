import random

# States
states = ["Start", "Object", "Picked", "Placed"]

# Actions
actions = {
    "Start": ["Move"],
    "Object": ["Pick"],
    "Picked": ["Move"],
    "Placed": []
}

# Policy (Initial Probabilities)
policy = {
    "Start": {"Move": 1.0},
    "Object": {"Pick": 1.0},
    "Picked": {"Move": 1.0}
}

# Transition Function
transitions = {
    ("Start", "Move"): "Object",
    ("Object", "Pick"): "Picked",
    ("Picked", "Move"): "Placed"
}

# Reward Function
rewards = {
    "Start": 0,
    "Object": 10,
    "Picked": 20,
    "Placed": 100
}

state = "Start"
total_reward = 0

print("===== Industrial Robotic Arm =====")

while state != "Placed":

    print("\nCurrent State:", state)

    action = list(policy[state].keys())[0]

    print("Action:", action)

    state = transitions[(state, action)]

    reward = rewards[state]

    total_reward += reward

    print("Next State:", state)
    print("Reward:", reward)

print("\nPick and Place Operation Completed Successfully!")
print("Total Reward:", total_reward)