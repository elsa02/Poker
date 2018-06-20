'''
This class define player
Player has - name
            - a hand
'''
class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def get_hand(self):
        return self.hand

    def __str__(self):
        return self.name + " : " + str(self.hand)