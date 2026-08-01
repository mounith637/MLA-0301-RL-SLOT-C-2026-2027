import random

# Grid Environment
grid = [
    ['S', '.', '.'],
    ['.', 'X', '.'],
    ['.', '.', 'G']
]

actions = ['Up', 'Down', 'Left', 'Right']

alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodes = 500

# Initialize Q-Table
Q = {}

for i in range(3):
    for j in range(3):
        Q[(i, j)] = {a: 0 for a in actions}


# Move Function
def move(state, action):

    x, y = state

    if action == "Up":
        x = max(0, x - 1)
    elif action == "Down":
        x = min(2, x + 1)
    elif action == "Left":
        y = max(0, y - 1)
    elif action == "Right":
        y = min(2, y + 1)

    if grid[x][y] == 'X':
        return state, -100

    if grid[x][y] == 'G':
        return (x, y), 100

    return (x, y), -1


# ε-Greedy Policy
def choose_action(state):

    if random.random() < epsilon:
        return random.choice(actions)

    return max(Q[state], key=Q[state].get)


# ---------------- TD(0) ----------------
V = {}

for i in range(3):
    for j in range(3):
        V[(i, j)] = 0

for ep in range(episodes):

    state = (0, 0)

    while state != (2, 2):

        action = choose_action(state)

        next_state, reward = move(state, action)

        V[state] = V[state] + alpha * (
            reward + gamma * V[next_state] - V[state]
        )

        state = next_state

print("TD(0) State Values")

for state in sorted(V):
    print(state, ":", round(V[state], 2))


# ---------------- SARSA ----------------

for ep in range(episodes):

    state = (0, 0)

    action = choose_action(state)

    while state != (2, 2):

        next_state, reward = move(state, action)

        next_action = choose_action(next_state)

        Q[state][action] += alpha * (
            reward +
            gamma * Q[next_state][next_action] -
            Q[state][action]
        )

        state = next_state
        action = next_action


print("\nSARSA Training Completed")


# ---------------- Q-Learning ----------------

for ep in range(episodes):

    state = (0, 0)

    while state != (2, 2):

        action = choose_action(state)

        next_state, reward = move(state, action)

        best_next = max(Q[next_state].values())

        Q[state][action] += alpha * (
            reward +
            gamma * best_next -
            Q[state][action]
        )

        state = next_state


print("Q-Learning Training Completed")


# Display Best Path

print("\nOptimal Path")

state = (0, 0)

print(state, end=" ")

while state != (2, 2):

    action = max(Q[state], key=Q[state].get)

    state, reward = move(state, action)

    print("->", state, end=" ")

print("\nGoal Reached Successfully!")