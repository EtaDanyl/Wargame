class Player:
    def __init__(self, name):
        self._name = name
        self._hand = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        if not isinstance(value, list):
            raise ValueError("Hand must be a list of cards.")
        self._hand = value

    def add_card(self, card: Card):
        self._hand.append(card)

    def draw_card(self):
        return self._hand.pop(0) if self._hand else None

    def __str__(self):
        hand_representation = ', '.join(str(card) for card in self._hand) if self._hand else "No cards"
        return f"Player: {self._name}, Hand: [{hand_representation}]"