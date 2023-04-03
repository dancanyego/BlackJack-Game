# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:43:41 2023

@author: danca
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

# Card Class

class Card():
    
    def __init__(self,suit,rank):
        
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return self.rank + " Of " + self.suit

    
# Deck Class To Store The cards

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return " The Deck has : " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
test_deck = Deck()
print(test_deck)

# Hand And Chip class

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        
        
        self.value += values[card.rank]
        
        # Track our aces 
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces:
            self.aces += 1
            
            self.value -= 10
            self.aces -= 1
    
test_deck = Deck()
test_deck.shuffle()

# Deal one card From The Deck card(Suit , rank)
test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)



class Chips():
    
    def __init__(self,total = 100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
# functions for placing a bet

def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input("How Many chips Would You like to bet"))
        
        except:
            print("Please Provide a valid Interger")
            
        else:
            if chips < chips.total:
                print("Sorry You have insuficient chips !! You have {}".format(chips.total))
                
            else: 
                break
                
                
    