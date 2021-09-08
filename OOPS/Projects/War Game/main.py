from deck import Deck
from player import Player
from game import WarCardGame


player = Player("Sujeeth",Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = WarCardGame(deck, player, computer)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats

    ans = input("Please enter to continue or 'X' to exit the game:")
    if ans.lower() == 'x':
        break