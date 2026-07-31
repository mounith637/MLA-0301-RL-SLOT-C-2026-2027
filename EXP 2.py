import random

# Smart Home Environment (Grid)
grid = [
    ['S', '.', '.'],
    ['.', 'X', '.'],
    ['.', '.', 'G']
]

# Parameters
alpha = 0.8      # Learning rate
gamma = 0.9      # Discount factor
epsilon = 0.2    # Exploration rate
episodes = 500

# Actions
actions = ['up', 'down', 'left', 'right']

# Q-Table
Q = {}

for i in range(3):
    for j in range(3):
        Q[(i, j)] = {a: 0 for a in actions}


# Move Function
def move(state, action):
    x, y = state

    if action == 'up':
        x = max(0, x - 1)
    elif action == 'down':
        x = min(2, x + 1)
    elif action == 'left':
        y = max(0, y - 1)
    elif action == 'right':
        y = min(2, y + 1)

    if grid[x][y] == 'X':
        return state, -100

    if grid[x][y] == 'G':
        return (x, y), 100

    return (x, y), -1


# Training
for episode in range(episodes):

    state = (0, 0)

    while state != (2, 2):

        # Exploration or Exploitation
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = max(Q[state], key=Q[state].get)

        next_state, reward = move(state, action)

        old_value = Q[state][action]
        next_max = max(Q[next_state].values())

        Q[state][action] = old_value + alpha * (
            reward + gamma * next_max - old_value
        )

        state = next_state


# Testing
print("Optimal Path:")

state = (0, 0)
print(state, end=" ")

while state != (2, 2):
    action = max(Q[state], key=Q[state].get)
    state, reward = move(state, action)
    print("->", state, end=" ")

print("\nGoal Reached!")