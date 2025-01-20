import random

class Card:
    def __init__(self, name, rank):
        self._name = name
        self._rank = rank

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if not isinstance(value, int):
            raise ValueError("Rank must be an integer.")
        self._rank = value

    def __str__(self):
        return f"{self.name} (Rank: {self.rank})"


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


POSSIBLE_CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
MAX_NUM_OF_CARDS_IN_DECK = 52
#There 4 suites but in this case suits are irrelevent so we just make 4 duplicates of each rank
MAX_NM_OF_CARDS_OF_EACH_RANK = 4
NUMBER_OF_DIFFERENT_CARD_TYPES = len(POSSIBLE_CARDS)

def main():
    deck = initialize_deck()
    player = create_player("Player")
    computer = create_player("Computer")
    distribute_cards(deck, player, computer)
    play_game(player, computer)

def play_game(player, computer):
    while True:
        player_card = draw_card(player)
        computer_card = draw_card(computer)

        if player_card > computer_card:
            take_cards(player, computer)
        elif computer_card > player_card:
            take_cards(computer, player)
        else:
            war(player, computer)

        winner = validate_game_status(player, computer)

        if isinstance(winner, Player):
            game_end(winner)
            break

def initialize_deck():
    new_deck = []

    for i in range(NUMBER_OF_DIFFERENT_CARD_TYPES):
        for _ in range(MAX_NM_OF_CARDS_OF_EACH_RANK):
            new_card = Card(POSSIBLE_CARDS[i], i)
            new_deck.append(new_card)

    random.shuffle(new_deck)

    return new_deck

def distribute_cards(deck, player, computer):
    index = 0
    while index < MAX_NUM_OF_CARDS_IN_DECK:
        player.add_card(deck[index])
        index += 1
        computer.add_card(deck[index])
        index += 1


def create_player(name):
    return Player(name)

if __name__ == "__main__":
    main()