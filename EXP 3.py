# Markov Decision Process (MDP) for Warehouse Robot

# States
states = ["Start", "Shelf", "Pickup", "Delivery", "Goal"]

# Actions
actions = {
    "Start": ["Move"],
    "Shelf": ["Pick", "Move"],
    "Pickup": ["Move"],
    "Delivery": ["Deliver"],
    "Goal": []
}

# Transition Function
transition = {
    ("Start", "Move"): "Shelf",
    ("Shelf", "Pick"): "Pickup",
    ("Shelf", "Move"): "Delivery",
    ("Pickup", "Move"): "Delivery",
    ("Delivery", "Deliver"): "Goal"
}

# Reward Function
rewards = {
    "Start": 0,
    "Shelf": 5,
    "Pickup": 10,
    "Delivery": 20,
    "Goal": 100
}

# Initial State
state = "Start"

print("===== Warehouse Robot MDP =====")

while state != "Goal":
    print("\nCurrent State:", state)
    print("Available Actions:", actions[state])

    action = input("Enter Action: ")

    if (state, action) in transition:
        state = transition[(state, action)]
        print("Next State:", state)
        print("Reward:", rewards[state])
    else:
        print("Invalid Action!")

print("\nRobot Successfully Delivered the Package!")
print("Final Reward:", rewards["Goal"])