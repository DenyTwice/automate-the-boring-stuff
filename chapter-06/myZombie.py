import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        
        # Bot that stops rolling if it gets 3 brains
        # brains = 0
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']

        #     if brains < 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #         break
        #     else:

        # Bot that randomly decides if it will continue or stop after the first roll
        # while diceRollResults is not None:
            # if random.randint(0,1) == 1:
                # diceRollResults = zombiedice.roll()
            # else:
                # break

        # Bot that stops rolling after it has rolled two brains
        # while diceRollResults is not None:
        #     brains = diceRollResults['brains']

        #     if brains == 2:
        #         break
        #     else:
        #         diceRollResults = zombiedice.roll()

        # Bot that stops rolling after it has rolled two shotguns
        # shotguns = 0
        # while diceRollResults is not None:
            # shotguns += diceRollResults['shotgun']
# 
            # if shotguns == 2:
                # break
            # else: 
                # diceRollResults = zombiedice.roll()

        # Bot that initially decides it’ll roll the dice 
        # one to four times, but will stop early if it rolls two shotguns

        # maxTurns = random.randint(1,4)
        # turn = 1
        # print(f"{maxTurns=}")
        # shotguns = 0
        # while diceRollResults is not None:
        #     print(f"{turn=}")
        #     shotguns += diceRollResults['shotgun']
        #     if shotguns == 2:
        #         print(f'{shotguns=}')
        #         break
        #     if turn == maxTurns:
        #         break
        #     else:
        #         turn += 1
        #         diceRollResults = zombiedice.roll()

        # A bot that stops rolling after it has rolled more shotguns than brains
        # while diceRollResults is not None:
            # shotguns = diceRollResults['shotgun']
            # brains = diceRollResults['brains']
            # if shotguns > brains:
                # break
            # else:
                # diceRollResults = zombiedice.roll()
        
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='Buckethead'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
