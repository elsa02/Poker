import unittest
from model.Pack import Pack
from model.Card import Card
from model.Player import Player
from model.Table import Table
from model.Hand import Hand
from Game import get_winners

class Test(unittest.TestCase):

    def test_one_winner_with_no_multiple_same_value_card(self):
        #init player 1
        cards_player1 = []
        cards_player1.append(Card(0,1))
        cards_player1.append(Card(3,10))
        hand_player1 =  Hand(cards_player1)
        player1 = Player("Player 1",hand_player1)

        # init player 2
        cards_player2 = []
        cards_player2.append(Card(2, 9))
        cards_player2.append(Card(1, 8))
        hand_player2 = Hand(cards_player2)
        player2 = Player("Player 2", hand_player2)

        #init Table
        cards_table = []
        cards_table.append(Card(0,3))
        cards_table.append(Card(1,5))
        cards_table.append(Card(2,4))
        cards_table.append(Card(0,7))
        cards_table.append(Card(0,2))

        players = []
        players.append(player1)
        players.append(player2)

        pack = Pack()

        table = Table(players,pack)
        table.set_cards(cards_table)

        expected_winner = []
        expected_winner.append(player1)
        self.assertEqual(expected_winner, get_winners(players, table))


    def test_one_winner_with_one_multiple_same_value_card(self):
        #init player 1
        cards_player1 = []
        cards_player1.append(Card(0,1))
        cards_player1.append(Card(3,10))
        hand_player1 =  Hand(cards_player1)
        player1 = Player("Player 1",hand_player1)

        # init player 2
        cards_player2 = []
        cards_player2.append(Card(2, 9))
        cards_player2.append(Card(1, 8))
        hand_player2 = Hand(cards_player2)
        player2 = Player("Player 2", hand_player2)

        #init Table
        cards_table = []
        cards_table.append(Card(0,3))
        cards_table.append(Card(1,8))
        cards_table.append(Card(2,4))
        cards_table.append(Card(0,7))
        cards_table.append(Card(0,2))

        players = []
        players.append(player1)
        players.append(player2)

        pack = Pack()

        table = Table(players,pack)
        table.set_cards(cards_table)

        expected_winner = []
        expected_winner.append(player2)
        self.assertEqual(expected_winner, get_winners(players, table))

    def test_two_winner(self):
        #init player 1
        cards_player1 = []
        cards_player1.append(Card(0,1))
        cards_player1.append(Card(3,10))
        hand_player1 =  Hand(cards_player1)
        player1 = Player("Player 1",hand_player1)

        # init player 2
        cards_player2 = []
        cards_player2.append(Card(2, 9))
        cards_player2.append(Card(1, 1))
        hand_player2 = Hand(cards_player2)
        player2 = Player("Player 2", hand_player2)

        #init Table
        cards_table = []
        cards_table.append(Card(0,3))
        cards_table.append(Card(1,1))
        cards_table.append(Card(2,1))
        cards_table.append(Card(0,7))
        cards_table.append(Card(0,2))

        players = []
        players.append(player1)
        players.append(player2)

        pack = Pack()

        table = Table(players,pack)
        table.set_cards(cards_table)

        expected_winner = []
        expected_winner.append(player1)
        expected_winner.append(player2)
        self.assertEqual(expected_winner, get_winners(players, table))