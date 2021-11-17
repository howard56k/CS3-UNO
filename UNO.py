import random


class Player:
    def __init__(self, deck):
        self.deck = deck

    def getAvailableCards(self):
        return (len(self.deck.deck))

    def putDownCard(self):
        return self.deck

    def addCard(self, card):
        self.deck.addToDeck(card)

    def pickUpCard(self, card):
        self.deck.returnCardFromDeck

    def getAmountOfCards(self):
        return len(self.deck.deck)



class Board:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.placedDeck = Deck([])

    def getDeck(self):
        return self.deck

    def cardsPlacedDeck(self, card):
        self.placedDeck.addToDeck(card)

    def returnCardFromDeck(self):
        if len(self.deck.deck) == 0:
            self.deck = random.shuffle(self.placedDeck.deck[:-1])
            self.placedDeck.deck = list(self.placedDeck.deck[-1])
        return self.deck.returnCard()

    def playerOrder(self):
        pass


class Deck:
    def __init__(self, cards):
        self.deck = cards

    def getDeckSize(self):
        return len(self.deck)

    def getCardFromDeck(self, card):
        for cardI in range(len(self.deck)):
            if card == self.deck[cardI]:
                self.removeFromDeck(cardI)
                return card
        return self.deck

    def removeFromDeck(self, index):
        self.deck.pop(index)

    def returnCard(self, card=None):
        if card == None:
            return self.deck.pop()
        else:
            return self.getCardFromDeck(card)

    def addToDeck(self, card):
        return self.deck.append(card)

    def shuffleDeck(self):
        random.shuffle(self.deck)


class Card:
    def __init__(self, number, color, special=False, placement=None):
        self.special = special
        self.number = number
        self.color = color
        self.placement = placement
        self.asset = ('./uno_assets_2d/PNGs/small/{}_{}.png'.format(color, number))

    def __eq__(self, other):
        if (isinstance(other, C)):
            return (self.number == other.number) and (self.color == other.color)

    def getCardNumber(self):
        return self.number

    def getCardColor(self):
        return self.color

    def setCardNumber(self, number):
        self.number = number

    def setCardColor(self, color):
        self.color = color

    def cardPlacement(self):
        return self.placement

    def isCardPlaceable(self, card):
        if card.special == True:
            return True
        elif card.color == self.color:
            return True
        elif card.number == self.number:
            return True
        else:
            return False
    def cardFileAsset(self):
        return self.asset


class Uno:
    def __init__(self, playerCount, startingCardCount):
        self.playerCount = playerCount
        self.startingCardCount = startingCardCount
        self.generateAllCards()
        self.generatePlayersandDeck()

    def generatePlayersandDeck(self):
        self.allCards.shuffleDeck()
        self.listOfPlayers = []
        for player in range(self.playerCount):
            playerDeck = Deck([])
            for count in range(self.startingCardCount):
                playerDeck.addToDeck(self.allCards.returnCard())
            self.listOfPlayers.append(Player(playerDeck))
        self.tableDeck = self.allCards
        self.board = Board(self.listOfPlayers, self.tableDeck)

    def generateAllCards(self):
        cardColors = ['blue', 'green', 'yellow', 'red']
        cards = []
        for i in range(4):
            cards.append(Card('color_changer', 'wild',special=True))
            cards.append(Card('pick_four', 'wild', special=True))
        for cardColor in cardColors:
            for i in range(2):
                cards.append(Card('picker', cardColor))
                cards.append(Card('reverse', cardColor))
                cards.append(Card('skip', cardColor))
            for i in range(10):
                if i != 0:
                    cards.append(Card(i, cardColor))
                cards.append(Card(i, cardColor))
        self.allCards = Deck(cards)

    def placeCard(self, card):
        self.board.cardsPlacedDeck(card)

    def checkIfWinner(self):
        for player in self.listOfPlayers:
            if player.getAmountOfCards() == 0:
                return player
            else:
                return None
