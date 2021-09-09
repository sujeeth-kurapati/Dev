class Suit:

    SYMBOLS = {"clubs":"♣", "hearts":"♥", "spades":"♠", "diamonds":"♦"}

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SYMBOLS[description]

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol