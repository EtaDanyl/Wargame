# Wargame

Requirements:

  Game Setup:
      Initialize a standard 52-card deck with ranks (suits are ignored).
      Randomly shuffle the deck.
      Distribute the deck evenly between the two players.
  
  Gameplay:
      Players simultaneously reveal the top card of their deck.
      Compare the two cards:
          The player with the higher-ranked card wins the battle and takes both cards, adding them to the bottom of their deck.
          If the cards are of equal rank, a "war" occurs:
              Each player places three cards face-down and one card face-up.
              Compare the face-up cards; the higher card wins all cards in play.
              Repeat the war process if the face-up cards are tied again.
      Continue until one player has no cards left or has won all cards.
  
  Ending the Game:
      Declare the player with all cards as the winner.
      If a player cannot complete a war due to insufficient cards, declare the other player as the winner.
  
  Error Handling:
      Handle cases where a player runs out of cards during a war:
          Allow the player to use their last card as the face-up card (optional rule).
          End the game if the player cannot continue.
