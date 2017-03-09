import random


class Monty_Hall:

    def __init__(self):
        door_one = False
        door_two = False
        door_three = False
        winner = random.randint(0, 2)
        doors = [door_one, door_two, door_three]
        doors[winner] = True
        self.doors = doors

    def stay(self):
        """This simulates not switching between doors when the option is
         presented. Because the 'player' is not switching, the first door
         that the user opens will be the one they end with regardless of
         which secondary door is revealed. 33 percent win expected."""
        random_door_pick = random.randint(0, 2)
        return self.doors[random_door_pick]

    def switch(self):
        """This simulates not switching between doors when the option is
         presented. Since the secondary door being opened always contains a
         goat, at that point the odds reduce to 50 percent win, 50 percent
         loss. Since the 'player' has predetermined to switch, they will
         always switch to the 'prize' that they did not select at the onset,
         hence if their original random_door_pick was a win they will switch to
         a lose and visa versa. 66 percent win expected."""
        random_door_pick = self.doors[random.randint(0, 2)]
        if random_door_pick is True:
            return False
        elif random_door_pick is False:
            return True

    def rand(self):
        """Using the logic from switch() after the initial random_door_pick and knowing
         that a random choice will be made between the two remaining doors
         which we know to have 50/50, a digital coin flip decices our win
         or loss. 50 percent win expected."""
        return random.choice(True, False)


def main():
    stay_wins = 0
    switch_wins = 0
    random_wins = 0
    # all functions in the following loops return True(1) for win
    count_simulations = 0
    while count_simulations < 1000:
        simulation = Monty_Hall()
        stay_wins += simulation.stay()
        count_simulations += 1
    count_simulations = 0
    while count_simulations < 1000:
        simulation = Monty_Hall()
        switch_wins += simulation.switch()
        count_simulations += 1
    count_simulations = 0
    while count_simulations < 1000:
        random_wins += simulation.rand()
        count_simulations += 1
    # Prints the number of wins out of one thousand.
    print("stay: " + str(stay_wins) + "/1000")
    print("switch: " + str(switch_wins) + "/1000")
    print("random: " + str(random_wins) + "/1000")


main()
