# Poker

## Presentation

This game is played from 2 players up to 10 players.

Table represents a round.
Table is composed of : - A pack of cards
                       - A list of players (2 to 10 players)
                       - A list of five cards

Pack is composed of 52 cards.
Card is represented by one colour and one number.
Player is represented by a name and a Hand.
Hand is a list of cards that a player has.

## Structure of the project

```bash
|-- Poker/
|   |-- model/
|   |   |-- Card.py
|   |   |-- Hand.py
|   |   |-- Pack.py
|   |   |-- Player.py
|   |   |-- Table.py
|   |   |-- __init__.py
|   |-- Game.py
|   |-- Test.py
|   |-- README.md
|   |-- .gitignore
```

## How to start game

Game.py contains main and some utils methods to calculate winner(s).

To start round, run Game.py

## How to test

Test.py contains three basic tests : 1) case of one winner with no pair
                                     2) case of one winner with a pair
                                     3) case of two winners

There are still plenty of other cases to test

To check test, run Test.py

