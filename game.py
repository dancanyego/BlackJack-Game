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
                
#function for taking hits

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
  
    
#Prompting players to hit or stand

def hit_or_stand(deck,hand):
    
    global playing 
    
    while True:
        
        x = input("hit or Stand ??  Enter 'H' or 'S' ")
        
        if x[0].lower() == 'h':
            hit(deck, hand)
            
        elif x[0].lower == 's':
                print("Player Stands, Dealers Turn")
                playing = False
                
        else:
            print("I did not understand your prompt, Please Enter H or S only")
            
        break
    
# Functions to display Cards

def show_some(player,dealer):
    #Show only one of the dealers hand
    
    print("\n Dealers hands::  ")
    print("First Cards Hidden!!")
    
    print(dealer.card[1])
    
    
    #Show all of the Two Players Card
    
    print("\n Players Hand ::> ")
    
    for card in player.Cards:
        print(card)
    
    

def show_all(player,dealer):
    
    # Show All dealers Card
    
    print("\n Dealers Hand ::> ")
    
    for card in dealer.Cards:
        print(card)
    
    # Calculate and display The Value
    
    print(f"Value of Dealers Card is :> {dealer.value}")
    
    # Show The players Cards 
    
     
    print("\n Players Hand ::> ")
    
    for card in player.Cards:
        print(card)
        
##End Of Game scenarios

def player_bursts(player,dealer,chips):
    print("BUST!! PLAYER !!")
    chips.lose_bet
    
def player_win(player,dealer,chips):
    print("PLAYER Wins!! DEALER LOST")
    chips.win_bet

def dealer_burst(player,dealer,chips):
    print("DEALER BURSTED !! PLAYER WINS!! ")
    chips.lose_bet
def dealer_wins(player,dealer,chips):
    print("PLAYER LOST!! DEALER WINS")
    chips.win_bet

def push(player,dealer):
    print("Dealer and Player Tied !! PUSH !")
    

## AND NOW THE GAME PLAY LOGIC

while True:
    
    print("Welcome to Black Jack")
    
    # Create and shuffle deck and  deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal()) # This is One card added
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    ## Set Up The Player Chips
    
    player_chips = Chips()
    
    # Prompt Player For their Bet
    
    take_bet(player_chips)
    
    #Show Cards
    
    show_some(player_hand, dealer_hand)
    
    while playing():
        pass
    
    


    