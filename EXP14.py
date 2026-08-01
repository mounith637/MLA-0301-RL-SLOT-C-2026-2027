import random

# Elevator States
states = ["Ground", "Floor1", "Floor2", "Floor3"]

# Actions
actions = ["Up", "Down", "Stay"]

# Actor (Policy)
policy = {}

# Critic (State Values)
value = {}

for state in states:
    policy[state] = random.choice(actions)
    value[state] = 0

# Reward Function
rewards = {
    "Ground": -1,
    "Floor1": 5,
    "Floor2": 10,
    "Floor3": 100
}

# Transition Function
def move(state, action):

    if state == "Ground":
        if action == "Up":
            return "Floor1"

    elif state == "Floor1":
        if action == "Up":
            return "Floor2"
        elif action == "Down":
            return "Ground"

    elif state == "Floor2":
        if action == "Up":
            return "Floor3"
        elif action == "Down":
            return "Floor1"

    elif state == "Floor3":
        if action == "Down":
            return "Floor2"

    return state

# Parameters
alpha = 0.1
gamma = 0.9
episodes = 100

# Training (A2C / A3C Concept)
for episode in range(episodes):

    state = "Ground"

    while state != "Floor3":

        action = policy[state]

        next_state = move(state, action)

        reward = rewards[next_state]

        td_error = reward + gamma * value[next_state] - value[state]

        # Critic Update
        value[state] += alpha * td_error

        # Actor Update
        if td_error > 0:
            policy[state] = action
        else:
            policy[state] = random.choice(actions)

        state = next_state

print("Training Completed!\n")

print("State Values")
for s in states:
    print(s, ":", round(value[s], 2))

print("\nLearned Policy")
for s in states:
    print(s, "->", policy[s])

print("\nElevator Simulation")

state = "Ground"
print(state, end=" ")

while state != "Floor3":

    action = policy[state]

    state = move(state, action)

    print("->", state, end=" ")

print("\nPassengers Reached Destination!")