import random
class Player:

    def __init__(self, marker="X", is_human=True):
        self._marker = marker
        self._is_human = is_human

    @property
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._is_human

    def get_player_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        move = input("Please enter the player's move : ")
        return move

    def get_computer_move(self):
        row = random.choice([1, 2, 3])
        column = random.choice(["A", "B", "C"])
        move = str(row) + column
        print("Computer's Move : ", move)
        return move