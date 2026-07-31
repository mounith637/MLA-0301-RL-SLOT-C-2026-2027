# Dynamic Programming for Autonomous Taxi Routing

# States (Locations)
states = ["Start", "Road1", "Road2", "Destination"]

# Rewards (Negative cost for travel)
rewards = {
    "Start": 0,
    "Road1": -2,
    "Road2": -3,
    "Destination": 100
}

# Transitions
transitions = {
    "Start": {"Go_Road1": "Road1", "Go_Road2": "Road2"},
    "Road1": {"Drive": "Destination"},
    "Road2": {"Drive": "Destination"},
    "Destination": {}
}

# Discount Factor
gamma = 0.9

# Initialize Value Function
V = {
    "Start": 0,
    "Road1": 0,
    "Road2": 0,
    "Destination": 100
}

# Dynamic Programming (Value Iteration)
for i in range(10):

    new_V = V.copy()

    for state in states:

        if state == "Destination":
            continue

        values = []

        for action in transitions[state]:

            next_state = transitions[state][action]

            value = rewards[next_state] + gamma * V[next_state]

            values.append(value)

        new_V[state] = max(values)

    V = new_V

# Display Optimal Values
print("Optimal State Values")

for state in states:
    print(state, ":", round(V[state], 2))

# Find Optimal Policy
print("\nOptimal Taxi Route")

current = "Start"

print(current, end=" ")

while current != "Destination":

    best_action = None
    best_value = -999

    for action in transitions[current]:

        next_state = transitions[current][action]

        value = rewards[next_state] + gamma * V[next_state]

        if value > best_value:
            best_value = value
            best_action = action

    current = transitions[current][best_action]

    print("->", current, end=" ")

print("\nTaxi Reached Destination Successfully!")