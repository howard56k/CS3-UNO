import random
class Player:
    def __init__(self,deck):
        self.deck = deck
    def getAvailableCards(self):
        return (len(self.deck))
    def putDownCard(self):
        return self.deck
    def pickUpCard(self):
        pass
    def getAmountOfCards(self):
        pass


class Uno:
    def __init__(self,playerCount,startingCardCount):
        self.playerCount = playerCount
        self.startingCardCount = startingCardCount
        self.generateAllCards()
        self.generatePlayersandDeck()
    def generatePlayersandDeck(self):
        players = []
        for player in range(self.playerCount):
            player.append(Player(deck))
    def generateAllCards(self):
        cardColors = ['blue','green','yellow','red']
        cards = []
        for i in range(4):
            cards.append(Card('color_changer','wild'))
            cards.append(Card('pick_four','wild'))
        for cardColor in cardColors:
            for i in range(2):
                cards.append(Card('picker',cardColor))
                cards.append(Card('reverse',cardColor))
                cards.append(Card('skip',cardColor))
            for i in range(10):
                if i != 0:
                    cards.append(Card(i,cardColor))
                cards.append(Card(i,cardColor))
        self.allCards = Deck(cards)


class Board:
    def __init__(self):
        pass
    def getDeck(self):
        pass
    def returnCardFromDeck(self):
        pass
    def playerOrder(self):
        pass
    def checkIfWinner(self):
        pass

class Deck:
    def __init__(self,cards):
        self.deck = cards
    def getDeckSize(self):
        return len(self.deck)
    def getCardFromDeck(self,card):
        for cardI in range(len(self.deck)):
            if card == self.deck[cardI]:
                self.removeFromDeck(cardI)
                return card
        return self.deck
    def removeFromDeck(self,index):
        self.deck.pop(index)
    def returnCard(self,card=None):
        if card == None:
            return self.deck.pop()
        else:
            return self.getCardFromDeck(card)
    def addToDeck(self,card):
        return self.deck.append(card)
    def shuffleDeck(self):
        self.deck = random.shuffle(self.deck)

class Card:
    def __init__(self,number,color, placement = None):
        self.number = number
        self.color = color
        self.placement = placement
        self.asset = ('./uno_assets_2d/PNGs/small/{}_{}.png'.format(color,number))
    def __eq__(self, other):
        if (isinstance(other, C)):
            return (self.number == other.number) and (self.color == other.color)
    def getCardNumber(self):
        return self.number
    def getCardColor(self):
        return self.color
    def cardPlacement(self):
        return self.placement
    def cardFileAsset(self):
        return self.asset