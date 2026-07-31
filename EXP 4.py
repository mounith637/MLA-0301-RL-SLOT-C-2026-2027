# Bellman Equation for Autonomous Delivery Robot

# States
states = ["A", "B", "C", "Goal"]

# Rewards
rewards = {
    "A": -1,
    "B": -2,
    "C": -1,
    "Goal": 100
}

# Transition Model
transitions = {
    "A": {"Right": "B", "Down": "C"},
    "B": {"Right": "Goal"},
    "C": {"Right": "Goal"},
    "Goal": {}
}

# Initialize Value Function
V = {
    "A": 0,
    "B": 0,
    "C": 0,
    "Goal": 100
}

gamma = 0.9      # Discount Factor
iterations = 10

# Bellman Value Iteration
for i in range(iterations):
    new_V = V.copy()

    for state in states:
        if state == "Goal":
            continue

        values = []

        for action in transitions[state]:
            next_state = transitions[state][action]
            value = rewards[next_state] + gamma * V[next_state]
            values.append(value)

        new_V[state] = max(values)

    V = new_V

# Display State Values
print("Optimal State Values")
for state in states:
    print(state, ":", round(V[state], 2))

# Find Optimal Path
print("\nOptimal Path:")

current = "A"
print(current, end=" ")

while current != "Goal":
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

print("\nDelivery Completed Successfully!")