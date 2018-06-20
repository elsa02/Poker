"""Represents a pack of 52 cards"""
from Card import Card
import random

class Pack:

    def __init__(self):
        self.cards = []
        for color in range(4):
            for value in range(12):
                card = Card(color, value)
                self.cards.append(card)

    """Remove card to pack"""
    def remove_card(self):
        return self.cards.pop()

    '''Shuffle pack'''
    def shuffle(self):
        return random.shuffle(self.cards)

    def get_cards(self):
        return self.cards