import random

# Robot States
states = ["Start", "Step1", "Step2", "Balanced"]

# Actions
actions = ["Forward", "Adjust", "Balance"]

# Policy
policy = {
    "Start": "Forward",
    "Step1": "Forward",
    "Step2": "Balance"
}

# Rewards
rewards = {
    "Start": 0,
    "Step1": 10,
    "Step2": 20,
    "Balanced": 100
}

# Transition Function
transitions = {
    ("Start", "Forward"): "Step1",
    ("Step1", "Forward"): "Step2",
    ("Step2", "Balance"): "Balanced"
}

# Parameters
episodes = 100
learning_rate = 0.1

# Training (Simplified PPO/TRPO Concept)
for episode in range(episodes):

    state = "Start"

    while state != "Balanced":

        action = policy[state]

        next_state = transitions[(state, action)]

        reward = rewards[next_state]

        # Simplified Policy Update
        if reward > 0:
            policy[state] = action
        else:
            policy[state] = random.choice(actions)

        state = next_state

print("Training Completed!")

print("\nLearned Policy")
for s in policy:
    print(s, "->", policy[s])

print("\nHumanoid Robot Walking")

state = "Start"
print(state, end=" ")

while state != "Balanced":

    action = policy[state]

    state = transitions[(state, action)]

    print("->", state, end=" ")

print("\nRobot Achieved Stable Walking and Balance!")