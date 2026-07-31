# Simplified Chess Game using Markov Decision Process (MDP)

# States
states = ["Start", "Middle", "NearWin", "Win"]

# Actions
actions = {
    "Start": ["Attack", "Defend"],
    "Middle": ["Attack", "Retreat"],
    "NearWin": ["Checkmate", "Mistake"],
    "Win": []
}

# Transition Model
transition = {
    ("Start", "Attack"): "Middle",
    ("Start", "Defend"): "Start",
    ("Middle", "Attack"): "NearWin",
    ("Middle", "Retreat"): "Start",
    ("NearWin", "Checkmate"): "Win",
    ("NearWin", "Mistake"): "Middle"
}

# Reward Function
rewards = {
    "Start": 0,
    "Middle": 5,
    "NearWin": 10,
    "Win": 100
}

# Initial State
state = "Start"

print("=== Simplified Chess Game (MDP) ===")

while state != "Win":
    print("\nCurrent State:", state)
    print("Possible Actions:", actions[state])

    action = input("Enter Action: ")

    if (state, action) in transition:
        state = transition[(state, action)]
        print("Moved to:", state)
        print("Reward:", rewards[state])
    else:
        print("Invalid Action!")

print("\nGame Over!")
print("You Reached:", state)
print("Final Reward:", rewards[state])