'''This class define Table
    Table is composed of - a pack of cards
                        - five cards (Flop, turn et river)
                        - liste of players

'''
class Table:

    def __init__(self, players, pack):
        self.cards = []
        self.players = players
        self.pack = pack

    def add_card(self,card):
        return self.cards.append(card)

    def get_players(self):
        return self.players

    def get_pack(self):
        return self.pack

    def get_cards(self):
        return self.cards

    def set_pack(self, pack):
        self.pack = pack

    def set_cards(self, cards):
        self.cards = cards

    def __str__(self):
        return "Tapis [" + ' , '.join(str(card) for card in self.cards) + "]" +"\n" + '\n'.join(str(player) for player in self.players)