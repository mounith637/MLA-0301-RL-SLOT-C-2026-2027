import random

tasks = {
    "Assembly": 10,
    "Welding": 15,
    "Painting": 8
}

learning_rates = {}

episodes = 100

for task in tasks:
    learning_rates[task] = 0.1

performance = {task: 0 for task in tasks}

for episode in range(episodes):

    task = random.choice(list(tasks.keys()))

    reward = tasks[task] + random.randint(-2, 2)

    # Meta-learning:
    # Adapt the learning rate based on performance
    if reward > 10:
        learning_rates[task] += 0.01
    else:
        learning_rates[task] -= 0.005

    learning_rates[task] = max(
        0.01,
        min(1.0, learning_rates[task])
    )

    performance[task] += (
        learning_rates[task] *
        (reward - performance[task])
    )

    if episode % 10 == 0:
        print(
            "Episode:", episode,
            "Task:", task,
            "Reward:", reward
        )

print("\nFinal Performance:")

for task in tasks:
    print(
        task,
        "Performance:",
        round(performance[task], 2),
        "Learning Rate:",
        round(learning_rates[task], 3)
    )