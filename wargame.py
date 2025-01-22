import random
from card_class import Card
from player_class import Player

POSSIBLE_CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
MAX_NUM_OF_CARDS_IN_DECK = 52
#There 4 suites but in this case suits are irrelevent so we just make 4 duplicates of each rank
MAX_NM_OF_CARDS_OF_EACH_RANK = 4
NUMBER_OF_DIFFERENT_CARD_TYPES = len(POSSIBLE_CARDS)
#Adding constraints since this game can run into an infite loop
MAX_NUM_OF_ROUNDS = 3000

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
    #Quite often the game would run into an infinite loop since we always collect cards in the same exact order programmically. 
    #In real life cards would naturally mix up a little, therefore using shuffle method to avoid any infinite loops.
    random.shuffle(cards_to_take)
    for card in cards_to_take:
        taker.add_card(card)

if __name__ == "__main__":
    main()