import random

# Advertisements (Arms)
ads = ["Ad A", "Ad B", "Ad C", "Ad D"]

# True click probabilities (hidden from the agent)
true_prob = [0.3, 0.5, 0.8, 0.6]

# Parameters
epsilon = 0.1        # Exploration rate
iterations = 1000

# Initialize
counts = [0] * len(ads)
values = [0.0] * len(ads)

# Epsilon-Greedy Algorithm
for i in range(iterations):

    # Exploration
    if random.random() < epsilon:
        action = random.randint(0, len(ads) - 1)

    # Exploitation
    else:
        action = values.index(max(values))

    # Simulate User Click
    if random.random() < true_prob[action]:
        reward = 1
    else:
        reward = 0

    # Update Statistics
    counts[action] += 1
    values[action] += (reward - values[action]) / counts[action]

# Display Results
print("Advertisement Results\n")

for i in range(len(ads)):
    print(ads[i])
    print("Times Selected :", counts[i])
    print("Average Reward :", round(values[i], 2))
    print()

best = values.index(max(values))
print("Best Advertisement:", ads[best])