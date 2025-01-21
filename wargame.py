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
        return f"{self.name}"


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
#Adding constraints since this game can run into an infite loop
MAX_NUM_OF_ROUNDS = 10000

def main():
    deck = initialize_deck()
    player = create_player("Player")
    computer = create_player("Computer")
    distribute_cards(deck, player, computer)
    play_game(player, computer)

def play_game(player, computer):
    cards_to_take = []
    round = 0
    while True:
        player_card = player.draw_card()
        computer_card = computer.draw_card()

        if player_card is None:
            game_end(computer, player)
            break
        if computer_card is None:
            game_end(player, computer)
            break
        
        print_played_card(player, player_card)
        print_played_card(computer, computer_card)
        cards_to_take.append(player_card)
        cards_to_take.append(computer_card)

        if player_card.rank > computer_card.rank:
            print_battle_status(player_card, computer_card, player)
            take_cards(player, cards_to_take)
            cards_to_take = []
        elif computer_card.rank > player_card.rank:
            print_battle_status(computer_card, player_card, computer)
            take_cards(computer, cards_to_take)
            cards_to_take = []
        else:
            print("War!")
            player_card_facedown = player.draw_card()
            computer_card_facedown = computer.draw_card()

            if player_card_facedown is None:
                game_end(computer, player)
                break
            if computer_card_facedown is None:
                game_end(player, computer)
                break

            print("Both players place one card face-down!")
            cards_to_take.append(player_card_facedown)
            cards_to_take.append(computer_card_facedown)

        round += 1
        print(round)
        if (round == MAX_NUM_OF_ROUNDS):
            print("It seems that the game has run into an infinite loop! Let's call it a draw!")
            break
        #input("\nPress 'Enter' to continue\n")


def game_end(winner, loser):
     print(f"{winner.name} wins the game! {loser.name} has no cards left.")

def print_played_card(player, card):
    print(f"{player.name} has played {card}")

def print_battle_status(winner_card, loser_card, battle_winner):
    print(f"{winner_card} is stronger than {loser_card}! Therefore {battle_winner.name} wins the battle and takes all the cards!")

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

def take_cards(taker, cards_to_take):
    for card in cards_to_take:
        taker.add_card(card)

if __name__ == "__main__":
    main()