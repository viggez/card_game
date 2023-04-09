# Card Game: War

A simple command-line implementation of the classic card game "War".
Play against a friend or practice on your own to hone your skills.

## Rules

1. The game is played with a standard deck of 52 cards, without the jokers.

2. The deck is shuffled and divided equally between two players.

3. Each player places the top card from their deck face-down on the table.

4. Both players reveal their cards simultaneously, and the player with the
    higher-ranking card wins that round and takes both cards, placing them face-down
    at the bottom of their deck.

5. If the two cards have the same rank, then a "war" is declared.

6. During a "war," each player places three cards face-down on the table, and then
    another card face-up on top of their stack.

7. The player with the higher-ranking card in the "war" wins all the cards that have been placed on the table.

8. If there is another tie during a "war," the process is repeated until one player wins.

9. The game continues until one player has all the cards, and that player is declared the winner.

## Features

- Two-player mode
- Hard mode for an increased challenge
- Colorful player-name interface
- High score tracking
- Secret cheat command for faster gameplay

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/viggez/card_game.git
```

2. In the terminal: Make sure you are in the /card_game directory.

3.
```bash
python3 -m app.game
```

4. Enjoy :D