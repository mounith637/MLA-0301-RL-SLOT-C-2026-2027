import random

locations = ["A", "B", "C"]

# Initial belief about victim location
belief = {
    "A": 0.33,
    "B": 0.33,
    "C": 0.34
}


def observe():

    observations = [
        "Weak Signal",
        "Strong Signal",
        "No Signal"
    ]

    return random.choice(observations)


def update_belief(observation):

    global belief

    if observation == "Strong Signal":

        belief["A"] *= 0.8
        belief["B"] *= 1.2
        belief["C"] *= 1.5

    elif observation == "Weak Signal":

        belief["A"] *= 1.2
        belief["B"] *= 1.1
        belief["C"] *= 1.0

    else:

        belief["A"] *= 0.9
        belief["B"] *= 0.9
        belief["C"] *= 0.9

    # Normalize probabilities
    total = sum(belief.values())

    for location in belief:
        belief[location] /= total


for step in range(10):

    observation = observe()

    update_belief(observation)

    best_location = max(
        belief,
        key=belief.get
    )

    print("\nStep:", step + 1)

    print("Observation:", observation)

    print(
        "Best Search Location:",
        best_location
    )

    print(
        "Belief:",
        {
            k: round(v, 2)
            for k, v in belief.items()
        }
    )

print("\nSearch-and-rescue decision completed.")