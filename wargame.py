class Card:
    pass


class Player:
    pass

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

if __name__ == "__main__":
    main()