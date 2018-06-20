from model.Table import Table
from model.Pack import Pack
from model.Player import Player
from model.Hand import Hand

''''Init game'''
def game():

    #init table with players
    print "Welcome! Game is started"
    number_players = ask_number_of_player()
    table = init_table(number_players)

    #Distribute cards to players
    print 'Distribution des cartes aux joueurs'
    print table

    #Do Flop, turn and river
    print 'Tirage Flop, turn et river'
    draw(table)
    print table

    #Get who is/are winners
    players = table.get_players()
    winners = get_winners(players, table)
    print "Winners [" + ' , '.join(map(str, winners)) + "]"
    return winners


'''init pack of cards'''
def init_pack():
    pack = Pack()
    pack.shuffle()
    return pack

'''init table with players'''
def init_table(number_players):
    #initialise pack of card"""
    pack = init_pack()
    #initialise players"""
    i = 1
    players = []
    while  i <= number_players :
        players.append(Player("Player "+str(i), Hand(remove_cards(2,pack))))
        i += 1
    return Table(players,pack)

'''remove x cards from pack of cards'''
def remove_cards(x,pack):
    removed_cards = []
    i = 0
    while i < x:
        removed_cards.append(pack.remove_card())
        i += 1
    return removed_cards

'''random draw'''
def draw(table):
    pack = table.get_pack()
    pack.remove_card()
    cards = remove_cards(3,pack)
    nbr = 0
    while nbr < 2 :
        pack.remove_card()
        cards.append(pack.remove_card())
        nbr += 1
    table.set_cards(cards)

'''function that return list of winner'''
def get_winners(players, table):
    winners = []
    tuple_in_winners = ()
    for player in players :
        '''Case of first'''
        if winners == [] :
            winners.append(player)
            tuple_in_winners = player.get_hand().get_better_cards(table.get_cards())
        else :
            '''Compare player and player in winner'''
            tuple_player = player.get_hand().get_better_cards(table.get_cards())
            if tuple_player>tuple_in_winners :
                del (winners[:])
                winners.append(player)
                tuple_in_winners=tuple_player
            elif tuple_player==tuple_in_winners :
                winners.append(player)

    return winners

'''Get number of players'''
def ask_number_of_player():
    players = 0
    while True:
        try:
            players = int(raw_input("Enter number of players : "))
        except ValueError:
            print "Oups!  That was no valid number.  Try again..."
        else:
            if players in range(2, 10):
                break
            else:
                print "Oups! Out of range, should be from 2-10 players. Try again..."

    return players

if __name__ == "__main__":
    game()