import random
import sys

class Deck():
    CARD_NUM = 13
    CARD_TYPE = ["club", "heart", "spade", "diamond"]

    def __init__(self):
        self.cards = []
        for i in range(1, self.CARD_NUM+1):
            for j in range(len(self.CARD_TYPE)):
                self.cards.append((i, self.CARD_TYPE[j]))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        assert len(self.cards)>0, "deck should not be empty"
        return self.cards.pop(0)

class Player():
    def __init__(self):
        self.cards = []

    def needs_card(self):
        print "cards: "+str(self.cards)
        ans = ""
        while ans != "y\n" and ans != "n\n":
            sys.stdout.write("draw cards?(y/n):")
            ans = sys.stdin.readline()
        if ans == "y\n":
            return True
        elif ans == "n\n":
            return False
        else:
            assert True, "error! this line cannot be reached!"

class DEALER(Player):
    THRESHOLD=20
    def needs_card(self):
        if count_score(self.cards) < self.THRESHOLD:
            return True
        else:
            return False

def judge(player_cards, dealer_cards):
    player_score=count_score(player_cards)
    dealer_score=count_score(dealer_cards)
    if player_score>21:
        return "lose"
    elif dealer_score>21:
        return "win"
    elif player_score>dealer_score:
        return "win"
    elif player_score<dealer_score:
        return "lose"
    else:
        return "draw"

def count_score(cards):
    score=0
    for i in cards:
        if i[0]<10:
            score+=i[0]
        else:
            score+=10
    return score

def test():
    deck = Deck()
    assert hasattr(deck, 'cards'), "deck should have cards"
    assert 52 == len(deck.cards), "number of cards should be 52"

    assert hasattr(deck, 'shuffle'), "deck should have shuffle method"
    deck.shuffle()

    assert hasattr(deck, 'deal'), "deck should have deal method"
    deck.deal()
    assert len(deck.cards) == 51, "number of cards should be 51 after dealing a card"

    player = Player()
    assert hasattr(player, 'cards'), "player should have cards"
    assert hasattr(player, 'needs_card'), "player should return decision"
#    print player.needs_card()

    dealer = DEALER()
    assert hasattr(dealer, 'cards'), "dealer should have cards"
    assert hasattr(dealer, 'needs_card'), "dealer should return decision"

    dealer.cards=[(10, "club"), (1, "heart")]
    assert dealer.needs_card()==True, "dealer should draw cards until score is 20"
    dealer.cards=[(10, "club"), (11, "heart")]
    assert dealer.needs_card()==False, "dealer should not draw cards when score is 20 or more than 20"
    dealer.cards=[(10, "club"), (11, "heart"), (2, "club")]
    assert dealer.needs_card()==False, "dealer should not draw cards when score is 20 or more than 20"

    assert judge([(10, "club"), (11, "heart")], [(1, "club"), (3, "heart")])=="win", "player win"
    assert judge([(10, "club"), (11, "heart")], [(10, "club"), (13, "heart"), (13, "club")])=="win", "player win(dealer burst)"
    assert judge([(10, "club"), (2, "heart")], [(10, "club"), (11, "heart")])=="lose", "player lose"
    assert judge([(10, "club"), (11, "heart")], [(10, "club"), (11, "heart")])=="draw", "draw"
    assert judge([(10, "club"), (11, "heart"), (11, "heart")], [(1, "club"), (3, "heart")])=="lose", "player lose(burst)"

def start_blackjack():
    deck = Deck()
    player = Player()
    dealer = DEALER()
    deck.shuffle()
    player.cards.append(deck.deal())
    dealer.cards.append(deck.deal())
    player.cards.append(deck.deal())
    dealer.cards.append(deck.deal())

    while player.needs_card():
        player.cards.append(deck.deal())
    while dealer.needs_card():
        dealer.cards.append(deck.deal())
    print "player: "+str(player.cards)+", dealer: "+str(dealer.cards)
    print "player score: "+str(count_score(player.cards))+", dealer score: "+str(count_score(dealer.cards))
    print judge(player.cards, dealer.cards)

if __name__ == "__main__":
    test()
    start_blackjack();
