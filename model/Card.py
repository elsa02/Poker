'''Represents a card with color and value'''

class Card:
    '''Attributs for print card'''
    color_name = ['trefle', 'carreau', 'coeur', 'pique']
    value_name = ['2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'valet', 'dame', 'roi','as']

    '''Constructor'''
    def __init__(self, color, value):
        self.color = color
        self.value = value

    '''Comparison of value and color'''
    def __lt__(self, other):
        t1 = self.value
        t2 = other.value
        return t1 < t2

    def __gt__(self, other):
        t1 = self.value
        t2 = other.value
        return t1 > t2

    def __eq__(self, other):
        return self.color != other.color and self.value == other.value

    def __neg__(self, other):
        return self.color == other.color or self.value != other.value

    '''Method toString'''
    def __str__(self):
        return '%s de %s' % (Card.value_name[self.value],
                             Card.color_name[self.color])

