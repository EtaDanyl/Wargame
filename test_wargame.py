from wargame import initialize_deck, create_player
import pytest
from card_class import Card
from player_class import Player

def test_initialize_deck():
    deck = initialize_deck()
    assert len(deck) == 52

def test_initialize_deck_instance():
    deck = initialize_deck()
    assert isinstance(deck[0], Card)

def test_two_decks():
    deck_one = initialize_deck()
    deck_two = initialize_deck()

    assert not deck_one == deck_two
    assert deck_one == deck_one

def test_create_player():
    player = create_player("John")
    assert isinstance(player, Player)

def test_player_str_with_cards():
    player = Player(name="Alice")  
    player._hand = ["Ace of Spades", "10 of Hearts"]
    expected_output = "Player: Alice, Hand: [Ace of Spades, 10 of Hearts]"
    assert str(player) == expected_output

def test_player_str_without_cards():
    player = Player(name="Bob")  
    player._hand = []
    expected_output = "Player: Bob, Hand: [No cards]"
    assert str(player) == expected_output
