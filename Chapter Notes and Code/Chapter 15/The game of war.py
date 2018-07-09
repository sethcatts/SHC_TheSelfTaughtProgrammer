from random import shuffle

class card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", 
              "8", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """Suite + Value are ints"""
        self.value = v
        self.suit = s
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    def __repr__(self):
        #Start here for debugging index error
        v = self.values[self.value] + " of " \
        + self.suits[self.suit]
        return v

class deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(card(i, j))
        shuffle(self.cards)
    def rmCard(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
    
class Game:
    def __init__(self):
        name1 = input("Player One: ")
        name2 = input("Player two: ")
        self.deck = deck()
        self.p1 = player(name1)
        self.p2 = player(name2)
    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {}, {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            m = "q to quit, press any key to continue play"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rmCard()
            p2c = self.deck.rmCard()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins!").format(win)
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()