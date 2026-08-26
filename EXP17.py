import random

# Environment states
tasks = ["Clean Room", "Pick Object", "Deliver Object"]

# Rewards
rewards = {
    "Clean Room": 10,
    "Pick Object": 8,
    "Deliver Object": 12
}

# MAXQ hierarchy
hierarchy = {
    "Complete Household Tasks": [
        "Clean Room",
        "Pick Object",
        "Deliver Object"
    ]
}

# Q-values
q_values = {task: 0.0 for task in tasks}

alpha = 0.1
gamma = 0.9
episodes = 100


def choose_task():
    # HAM: High-level action selection
    return random.choice(tasks)


for episode in range(episodes):

    total_reward = 0

    # MAXQ root task
    for subtask in hierarchy["Complete Household Tasks"]:

        task = subtask

        reward = rewards[task]

        # Q-value update
        q_values[task] = q_values[task] + alpha * (
            reward + gamma * q_values[task] - q_values[task]
        )

        total_reward += reward

    if episode % 10 == 0:
        print("Episode:", episode,
              "Reward:", total_reward)

print("\nLearned Q-values:")

for task, value in q_values.items():
    print(task, ":", round(value, 2))

print("\nRobot completed all household tasks.")