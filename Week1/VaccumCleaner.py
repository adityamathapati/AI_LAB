import random


# Class representing the environment
class Environment:

    # Initialize the environment
    def __init__(self):
        self.rooms = {
            "A": "Clean",
            "B": "Dirty"
        }


# Reflex agent inherits the Environment class
class ReflexAgent(Environment):

    # Initialize the reflex agent
    def __init__(self):
        super().__init__()

        # Randomly select the starting position
        self.position = random.choice(["A", "B"])

    # Display the current state
    def display_state(self):
        print("\nCurrent State:")
        print("Room A:", self.rooms["A"])
        print("Room B:", self.rooms["B"])
        print("Vacuum Position:", self.position)

    # Perform action based on the current room
    def perform_action(self):

        # Check whether the current room is dirty
        if self.rooms[self.position] == "Dirty":

            # Clean the current room
            print("Action: Clean Room", self.position)
            self.rooms[self.position] = "Clean"

        else:

            # Move to the other room
            print("Action: Move from Room", self.position, end=" ")

            if self.position == "A":
                self.position = "B"
            else:
                self.position = "A"

            print("to Room", self.position)

    # Check whether the goal state is reached
    def goal_reached(self):

        return (
            self.rooms["A"] == "Clean"
            and self.rooms["B"] == "Clean"
        )

    # Run the vacuum cleaner
    def run(self):

        print("----- VACUUM CLEANER PROBLEM -----")

        # Display initial state
        self.display_state()

        # Continue until both rooms are clean
        while not self.goal_reached():

            # Perform reflex action
            self.perform_action()

            # Display updated state
            self.display_state()

        # Display final message
        print("\nGoal Reached!")
        print("Both rooms are clean.")


# Create an object of ReflexAgent
vacuum = ReflexAgent()

# Run the vacuum cleaner
vacuum.run()