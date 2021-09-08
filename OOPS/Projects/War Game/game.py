class WarCardGame:

    PLAYER = 0 
    COMPUTER = 1
    TIE = 2

    def __init__(self, deck, player, computer):
        self._deck = deck
        self._player = player
        self._computer = computer
        self.make_initial_deck()

    def make_initial_deck(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def get_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:   
            return WarCardGame.PLAYER
        elif computer_card.value > player_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card, computer_card, cards_won):
        if cards_won:
            return [player_card, computer_card] + cards_won
        else:
            return [player_card, computer_card]

    def add_cards_to_character(self, character, cards_won):
        for card in cards_won:
            character.add_card(card)

    def start_war(self, cards_won):
        
        player_cards = []
        computer_cards = []

        for i in range(3):
            player_cards.append(self._player.draw_card())
            computer_cards.append(self._computer.draw_card())

        list_of_cards = player_cards + computer_cards + cards_won
        self.start_battle(list_of_cards)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("=============================")
            print("|        Game Over          |") 
            print("=============================")
            print("Computer has won the Game!!")
            return True
        elif self._computer.has_empty_deck():
            print("=============================")
            print("|        Game Over          |") 
            print("=============================")
            print("Player has won the Game!!")
            return True
        else:
            return False

    def print_stats(self):
        print("\n",10*"=")
        print("Player Deck Count: ",self._player.deck.size())
        print("Computer Deck Count: ",self._computer.deck.size())
        print(10*"=")

    def print_welcome_message(self):
            print("=============================")
            print("|     War Card Game         |") 
            print("=============================")
          
    def start_battle(self, cards_won=None):
        print("====Let's Begin the Battle===\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print(f"Your Card:")
        player_card.show()

        print(f"\nComputer's Card:")
        computer_card.show()

        winner = self.get_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_won)

        if winner == WarCardGame.PLAYER:
            print("You have won this round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("Computer won this round")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\nIt's a tie. This is war!")
            self.start_war(cards_won)

        return winner