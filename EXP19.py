import random

robots = ["Robot 1", "Robot 2", "Robot 3"]

tasks = [
    "Pick Package",
    "Move Package",
    "Deliver Package"
]

q_table = {}

# Initialize Q-values
for robot in robots:
    q_table[robot] = {}

    for task in tasks:
        q_table[robot][task] = 0

alpha = 0.1
gamma = 0.9
episodes = 100

for episode in range(episodes):

    total_reward = 0

    assigned_tasks = random.sample(
        tasks,
        len(robots)
    )

    for i, robot in enumerate(robots):

        task = assigned_tasks[i]

        # Cooperative reward
        reward = random.randint(5, 15)

        old_q = q_table[robot][task]

        new_q = old_q + alpha * (
            reward +
            gamma * old_q -
            old_q
        )

        q_table[robot][task] = new_q

        total_reward += reward

    if episode % 10 == 0:
        print(
            "Episode:",
            episode,
            "Team Reward:",
            total_reward
        )

print("\nLearned Robot Policies:")

for robot in robots:

    best_task = max(
        q_table[robot],
        key=q_table[robot].get
    )

    print(
        robot,
        "->",
        best_task
    )