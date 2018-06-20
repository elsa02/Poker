'''
This class define a Hand which is a list of card
'''
class Hand:
    def __init__(self,cards):
        self.cards = cards

    def get_card(self):
        return self.cards

    '''This method take the two cards of players and the five cards of the players
        return a tuple of how times the best cards it appears
        example 1 :
        player hand [valet de pique, 2 de carreau]
        table cards [roi de pique, 10 de trefle, 7 de pique, 4 de carreau, 3 de pique]
        return (1, 11)
        11 is the value of the representation of 'roi'
        example 1 :
        player hand [valet de pique, 2 de carreau]
        table cards [roi de pique, 2 de trefle, 7 de pique, 4 de carreau, 3 de pique]
        return (2, 0)
        0 is the value of the representation of '2'
    '''
    def get_better_cards(self,table_cards):
        newlist = []
        for card in self.cards+table_cards:
            newlist.append(card.value)
        newlist = sorted(newlist,key=lambda x: (2 if newlist.count(x) >2 else newlist.count(x), x), reverse=True)
        return (newlist.count(newlist[0]),newlist[0])


    def __str__(self):
        if self.cards == [] :
            return "[]"
        return "["+ ' , '.join(map(str,self.cards))+"]"