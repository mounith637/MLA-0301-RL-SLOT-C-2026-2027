import random

# Grid Environment
grid = [
    ['S', '.', '.'],
    ['.', 'D', '.'],
    ['.', '.', 'G']
]

# Actions
actions = ['Up', 'Down', 'Left', 'Right']

# Parameters
episodes = 500
gamma = 0.9

# Value Table
V = {}

for i in range(3):
    for j in range(3):
        V[(i, j)] = 0

returns = {}

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

    reward = -1

    if grid[x][y] == 'D':
        reward = 10

    if grid[x][y] == 'G':
        reward = 100

    return (x, y), reward

# Monte Carlo Training
for ep in range(episodes):

    state = (0, 0)
    episode = []

    while state != (2, 2):

        action = random.choice(actions)

        next_state, reward = move(state, action)

        episode.append((state, reward))

        state = next_state

    G = 0

    for state, reward in reversed(episode):

        G = gamma * G + reward

        if state not in returns:
            returns[state] = []

        returns[state].append(G)

        V[state] = sum(returns[state]) / len(returns[state])

# Display Learned Values
print("State Values")

for key in sorted(V):
    print(key, ":", round(V[key], 2))

# Simple Greedy Test
print("\nRobot Cleaning Path")

state = (0, 0)

print(state, end=" ")

while state != (2, 2):

    best_state = state
    best_value = -999

    for action in actions:

        next_state, reward = move(state, action)

        if V[next_state] > best_value:
            best_value = V[next_state]
            best_state = next_state

    state = best_state
    print("->", state, end=" ")

print("\nCleaning Completed Successfully!")